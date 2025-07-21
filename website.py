from flask import (Flask, redirect, url_for, render_template,
                   flash, request, send_from_directory, send_file)
#from werkzeug.utils import secure_filename
import ssbmr, base64, random, string, json, sys
#from os.path import join, dirname, realpath

app = Flask(__name__)
app.secret_key = "its a secret to everyone"

def create_seed_code(flags): # Seed code is a unique identifier for the URL
    random.seed(flags)
    code = ""
    while True:
        code += random.choice(string.ascii_letters)
        if len(code) >= 20:
            return code

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=['POST']) # Expects JSON with key "flags" that contains a valid flagset
def generate():
    request_data = request.json
    flags = request_data["flags"]
    code = create_seed_code(flags)
    ssbmr.generate_seed(flags, code)
    return "https://ssbmr.com/" + code

@app.route("/simple", methods=['GET','POST'])
def simple():
    if request.method == 'POST':
        flags = request.form["flags"]
        code = create_seed_code(flags)
        ssbmr.start(flags, code)
        return redirect(url_for('seed', seed=code))
    return render_template("simple.html")

@app.route("/<seed>")
def seed(seed):
    # Find xdelta and include it in content
    try:
        xdelta = open("seeds/" + seed + ".xdelta", "rb").read()
    except:
        return "<h1>No seed found!</h1>"
    data = base64.b64encode(xdelta).decode('ascii')
    return render_template("seed.html", content=data)

@app.route("/sotw_na")
def sotw_na():
    data = open("sotw.json")
    sotw_dict = json.load(data)
    print(sotw_dict, file=sys.stderr)
    data.close()
    return redirect("/" + sotw_dict["NA"])

@app.route("/sotw_eu")
def sotw_eu():
    data = open("sotw.json")
    sotw_dict = json.load(data)
    data.close()
    return redirect("/" + sotw_dict["EU"])

if __name__ == "__main__":
    app.run(debug=True)
