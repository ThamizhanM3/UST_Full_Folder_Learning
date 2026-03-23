# import os

# current_file_path = os.path.abspath(__file__)
# print("Current file path:", current_file_path)


# from pathlib import Path

# current_file_path = Path(__file__).resolve()
# print("Current file path:", current_file_path)


# import os

# current_dir = os.path.dirname(os.path.abspath(__file__))
# print("Current directory:", current_dir)


# from pathlib import Path

# current_dir = Path(__file__).resolve().parent
# print("Current directory:", current_dir)

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask via Nginx Reverse Proxy!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)