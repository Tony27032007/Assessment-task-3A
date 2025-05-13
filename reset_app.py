from flask import Flask, request, render_template_string, redirect, url_for, flash
from supabase import create_client

SUPABASE_URL = "https://przfumkjastcgmejfvrt.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InByemZ1bWtqYXN0Y2dtZWpmdnJ0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDcwNjU5MzgsImV4cCI6MjA2MjY0MTkzOH0.OsYJ-_TWHZ7lUSWGD7lFkzGf18tqqapSkbrTqq8d7rk"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def create_app():
    app = Flask(__name__)
    app.secret_key = "your_secret_key"

    RESET_FORM = """
    <!doctype html>
    <title>Set New Password</title>
    <h2>Set a New Password</h2>
    {% if token %}
    <form method=post>
      <input type="hidden" name="access_token" value="{{ token }}">
      <label>New Password:</label><br>
      <input type="password" name="password" required><br><br>
      <input type="submit" value="Set Password">
    </form>
    {% else %}
    <p style="color:red;">Invalid or missing token.</p>
    {% endif %}
    {% with messages = get_flashed_messages() %}
      {% if messages %}
        <ul>
        {% for message in messages %}
          <li style="color:green;">{{ message }}</li>
        {% endfor %}
        </ul>
      {% endif %}
    {% endwith %}
    """

    @app.route("/reset", methods=["GET", "POST"])
    def reset():
        token = request.args.get("access_token") or request.form.get("access_token")
        if not token:
            return render_template_string(RESET_FORM, token=None)
        if request.method == "POST":
            password = request.form["password"]
            try:
                supabase.auth.update_user({"password": password}, access_token=token)
                flash("Password updated successfully! You can now log in.")
                return redirect(url_for("reset", access_token=token))
            except Exception as e:
                flash("Failed to update password. The link may be invalid or expired.")
        return render_template_string(RESET_FORM, token=token)

    return app

# Optional: allow running directly
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)