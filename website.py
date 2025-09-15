from flask import (Flask, redirect, url_for, render_template,
                   flash, request, send_from_directory, send_file)
#from werkzeug.utils import secure_filename
import base64, random, string, json, sys, subprocess
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
    num_seeds = open("seeds_generated.txt").read()
    return render_template("index.html", content=num_seeds)

@app.route("/generate", methods=['POST']) # Expects JSON with key "flags" that contains a valid flagset
def generate():
    request_data = request.json
    flags = request_data["flags"]
    _seed = request_data["seed"]
    code = create_seed_code(_seed + flags)
    subprocess.run(["python3", "ssbmr.py", "melee.iso", "output.iso", _seed, flags, code])
    #_ssbmr.generate_seed(flags, 'melee.iso', 'output.iso', _seed, False, code)
    num_seeds_file_r = open("seeds_generated.txt", "r")
    num_seeds = int(num_seeds_file_r.read()) + 1
    num_seeds_file_r.close()
    num_seeds_file_w = open("seeds_generated.txt", "w")
    num_seeds_file_w.write(str(num_seeds))
    num_seeds_file_w.close()
    with open("json/" + code, "w") as json_file:
        json.dump(request_data, json_file, indent=4)
    return "https://ssbmr.com/" + code

@app.route("/onlineseed", methods=['GET','POST'])
def simple():
    if request.method == 'POST':
        flags = request.form["flags"]
        code = create_seed_code(flags)
        return redirect(url_for('seed', seed=code))
    data = []
    with open('Data/standard.json') as json_file:
        data.append(json.load(json_file))
    with open('Data/shuffle.json') as json_file:
        data.append(json.load(json_file))
    with open('Data/special.json') as json_file:
        data.append(json.load(json_file))
    with open('Data/gecko.json') as json_file:
        data.append(json.load(json_file))
    return render_template("simple.html", json_data=data)

@app.route("/<seed>")
def seed(seed):
    # Find xdelta and include it in content
    try:
        xdelta = open("seeds/" + seed + ".xdelta", "rb").read()
    except:
        return "<h1>No seed found!</h1>"
    data = []
    data.append(base64.b64encode(xdelta).decode('ascii'))
    try:
        with open("json/" + seed, 'r') as file:
            seed_dictionary = json.load(file)
    except:
        seed_dictionary = {}
        seed_dictionary["seed"] = "Unknown"
        seed_dictionary["flags"] = "Unknown"
    data.append(seed_dictionary)
    return render_template("seed.html", content=data)

@app.route("/sotw_na")
def sotw_na():
    data = open("sotw.json")
    sotw_dict = json.load(data)
    data.close()
    return redirect("/" + sotw_dict["NA"])

@app.route("/sotw_eu")
def sotw_eu():
    data = open("sotw.json")
    sotw_dict = json.load(data)
    data.close()
    return redirect("/" + sotw_dict["EU"])

@app.route("/download")
def download():
    return send_file("Melee Randomizer v1.0.zip", as_attachment=True)

@app.route("/set_sotw", methods=['POST']) # Expects JSON with key "flags" that contains a valid flagset
def set_sotw():
    request_data = request.json
    sotw_n = request_data["NA"]
    sotw_e = request_data["EU"]
    sotw_n = sotw_n.replace("https://ssbmr.com/", "")
    sotw_e = sotw_e.replace("https://ssbmr.com/", "")
    password = request_data["Password"]
    if password == "MeleeRandomiz3r!":
        data = open("sotw.json")
        sotw_dict = json.load(data)
        data.close()
        sotw_dict["NA"] = sotw_n
        sotw_dict["EU"] = sotw_e
        with open("sotw.json", "w") as json_file:
            json.dump(sotw_dict, json_file, indent=2)
        return "Success!"
    return "Wrong password!"

if __name__ == "__main__":
    app.run()
