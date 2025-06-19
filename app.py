from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load memory
with open("memory.json", "r") as f:
    memory = json.load(f)

@app.route("/")
def home():
    return render_template("home.html", memory=memory)

@app.route("/apps")
def apps():
    return render_template("apps.html", apps=memory.get("active_apps", []))

@app.route("/missions")
def missions():
    missions = [
        {"id": 1, "task": "Invite 5 people", "reward": 100},
        {"id": 2, "task": "Complete setup", "reward": 50}
    ]
    return render_template("missions.html", missions=missions)

@app.route("/console")
def console():
    return render_template("console.html")

@app.route("/settings")
def settings():
    return render_template("settings.html", memory=memory)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
