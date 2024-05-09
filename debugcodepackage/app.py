from flask import Flask
from dotenv import load_dotenv
import os

app1 = Flask(__name__, template_folder="templates")

load_dotenv()

@app1.route('/')
def home():
    print(os.getcwd())
    print(os.environ['FLASK_ENV'])
    return "<h1>Welcome to Home - changes updated </h1>"


