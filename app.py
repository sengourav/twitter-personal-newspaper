from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    with open("data/topic_summary.json") as f:
        summary = json.load(f)
    return render_template("index.html", summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
