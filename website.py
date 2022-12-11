from flask import (Flask, redirect, url_for, render_template,
                   flash, request, send_from_directory, send_file)
from werkzeug.utils import secure_filename
import randomizer, os, json, base64, random, string, util
from os.path import join, dirname, realpath

app = Flask(__name__)
app.secret_key = "its a secret to everyone"

file = open(r"data/presets.json")
presets = json.load(file)
file.close()

def create_seed_code(flags):
    random.seed(flags)
    code = ""
    while True:
        code += random.choice(string.ascii_letters)
        if len(code) >= 20:
            return code

@app.route("/", methods=['GET','POST'])
def generate_new():
    if request.method == 'POST':
        flags = request.form["flags"]
        if "-seed" not in flags:
            seed = ''.join(random.choices(string.digits + string.ascii_lowercase, k=8))
            flags = "-seed " + seed + flags
        code = create_seed_code(flags)
        log = randomizer.start(["base.iso", "", flags], code)
        if log == -1: # No return value/randomizer did not run (seed already exists)
            return redirect(url_for('seed', seed=code))
        with open("json/" + code + ".json", "w") as outfile:
            json.dump(log, outfile)
        return redirect(url_for('seed', seed=code))
    return render_template("index.html")

@app.route("/<seed>")
def seed(seed):
    # Find xdelta and include it in content
    try:
        xdelta = open("seeds/" + seed + ".xdelta", "rb").read()
    except:
        return "<h1>No seed found!</h1>"
    data = base64.b64encode(xdelta).decode('ascii')
    log_json = open("json/" + seed + ".json")
    log = json.load(log_json)
    return render_template("seed.html", content=[data,log])

@app.route("/seed/<code>")
def old(code):
    return redirect(url_for('seed', seed=code))

@app.route("/json/<code>")
def send_json(code):
    return send_file(code+".json", code+".json")

if __name__ == "__main__":
    app.run(debug="True")
