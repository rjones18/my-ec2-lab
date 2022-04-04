from flask import Flask, render_template
import subprocess

app = Flask(__name__)
app.config['SECRET_KEY'] = "xxxxxxxxx"

@app.route("/") 
def home():
    subprocess.call('python3 /home/ubuntu/flask_project/script.py', shell=True)
    return render_template("index.html")
	
if __name__ == "__main__":
	    app.run()