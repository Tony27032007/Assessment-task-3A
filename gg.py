from supabase import create_client, Client

url = "https://przfumkjastcgmejfvrt.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InByemZ1bWtqYXN0Y2dtZWpmdnJ0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDcwNjU5MzgsImV4cCI6MjA2MjY0MTkzOH0.OsYJ-_TWHZ7lUSWGD7lFkzGf18tqqapSkbrTqq8d7rk"
supabase: Client = create_client(url, key)