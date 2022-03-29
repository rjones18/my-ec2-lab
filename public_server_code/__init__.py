from flask import Flask, render_template
import subprocess

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey123"

@app.route("/") 
def home():
    ec2info = subprocess.check_output('aws ec2 describe-instances --filters "Name=tag:Name,Values=private_server_*" --query "Reservations[].Instances[].InstanceId"', shell=True)
    return render_template("index.html", ec2info=ec2info)
	
if __name__ == "__main__":
	    app.run()