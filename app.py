import os
from flask import Flask
app = Flask=(__name__)

@app.route("/")
def main():
    return "Working!"

@app.route("/home")
def main():
    return "/home is Working!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)