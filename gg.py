import pyrebase
firebaseConfig = {
  "apiKey": "AIzaSyDOFgG6I2VIBc3LeJfUt7AyOd2SHaPHRO4",
  "authDomain": "cinema-5819f.firebaseapp.com",
  "databaseURL": "https://cinema-5819f-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "cinema-5819f",
  "storageBucket": "cinema-5819f.firebasestorage.app",
  "messagingSenderId": "728966562197",
  "appId": "1:728966562197:web:6664d4578fbe689c20b69c",
  "measurementId": "G-F04WRTG05R"
};
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()