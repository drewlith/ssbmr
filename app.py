from tkinter import *
from tkinter import filedialog
import randomizer, os, random, string, sys, json

root = Tk()
root.geometry('300x180')
root.title("SSBM Randomizer")

icon = "data/icon.ico"
root.iconbitmap(icon)
    
root.resizable(False,False)

try:
    with open ('data/config.json') as json_file:
        config = json.load(json_file)
except:
    config = {'ISO Path': '','Output Dir': ''}
    with open ('data/config.json', 'w') as json_file:
        json.dump(config, json_file)

if len(config['ISO Path']) == 0:
    iso_path = os.getcwd()
else:
    iso_path = config['ISO Path']

if len(config['Output Dir']) == 0:
    out_path = os.getcwd()
else:
    out_path = config['Output Dir']

def iso_open():
    path = filedialog.askopenfilename(parent=root, initialdir=os.getcwd(), title="Please select v1.02 USA Super Smash Bros. Melee ISO.")
    path_entry.delete(0, END)
    path_entry.insert(END, path)

def dir_select():
    path = filedialog.askdirectory(parent=root, initialdir=os.getcwd(), title="Please choose directory to put the newly generated ISO.")
    output_entry.delete(0, END)
    output_entry.insert(END, path)

def new_seed():
    seed = ''.join(random.choices(string.digits + string.ascii_lowercase, k=8))
    sv.set(seed)

def start_randomizer():
    message.set("Randomizing... Please wait")
    iso_path = path_entry.get()
    out_path = output_entry.get()
    if ".iso" not in iso_path:
        message.set("Error: File is not a .iso!")
        return
    
    data = {"ISO Path" : iso_path, "Output Dir" : out_path }

    try:
        with open('data/config.json', 'w') as config:
            json.dump(data, config)
    except:
        print("No config file found.")

    seed = sv.get()

    randomizer.seed = seed

    if game_mode.get() in "Standard":
        randomizer.chaos = 5
        randomizer.random_percent = 20
        randomizer.balance_percent = 100
        randomizer.inclusion_percent = 80
        randomizer.attributes = True
        randomizer.a_floor = 0.9
        randomizer.a_ceiling = 1.1
        randomizer.customs_only = False

    if game_mode.get() in "Competitive":
        randomizer.chaos = 0
        randomizer.random_percent = 20
        randomizer.balance_percent = 100
        randomizer.inclusion_percent = 50
        randomizer.attributes = False
        randomizer.customs_only = False

    if game_mode.get() in "All Shuffled":
        randomizer.chaos = 0
        randomizer.random_percent = 0
        randomizer.balance_percent = 0
        randomizer.inclusion_percent = 100
        randomizer.attributes = False
        randomizer.customs_only = False

    if game_mode.get() in "All Random":
        randomizer.chaos = 0
        randomizer.random_percent = 100
        randomizer.balance_percent = 0
        randomizer.inclusion_percent = 100
        randomizer.attributes = False
        randomizer.customs_only = False

    if game_mode.get() in "Shuffle Balanced":
        randomizer.chaos = 0
        randomizer.random_percent = 0
        randomizer.balance_percent = 100
        randomizer.inclusion_percent = 100
        randomizer.attributes = False
        randomizer.customs_only = False

    if game_mode.get() in "Random Balanced":
        randomizer.chaos = 0
        randomizer.random_percent = 100
        randomizer.balance_percent = 100
        randomizer.inclusion_percent = 100
        randomizer.attributes = False
        randomizer.customs_only = False

    if game_mode.get() in "Chaotic":
        randomizer.chaos = 50
        randomizer.random_percent = 50
        randomizer.balance_percent = 80
        randomizer.inclusion_percent = 100
        randomizer.a_floor = 0.8
        randomizer.a_ceiling = 1.25
        randomizer.attributes = True
        randomizer.customs_only = False

    if game_mode.get() in "True Chaos":
        randomizer.chaos = 100
        randomizer.random_percent = 50
        randomizer.balance_percent = 50
        randomizer.inclusion_percent = 100
        randomizer.a_floor = 0.5
        randomizer.a_ceiling = 1.5
        randomizer.attributes = True
        randomizer.customs_only = False

    if game_mode.get() in "Slippi Unranked Mode":
        randomizer.customs_only = True
        
    randomizer.main(iso_path, out_path + "\SSBM_Randomizer_v1.0-" + seed + ".iso")
    
    message.set("...done!")

seed = ''.join(random.choices(string.digits + string.ascii_lowercase, k=8))
message = StringVar()
message.set("SSBM Randomizer v1.0 by drewlith")
system = Label(root,textvariable=message).place(x=2,y=155)

Button(root,text="Browse", width = 8, command= lambda:iso_open()).place(x=230,y=10)
path_entry = Entry(root,width = 25)
path_entry.place(x=70,y=14)
path_entry.insert(END, iso_path)
Label(root,text="ISO Path:").place(x=10,y=14)

Button(root,text="Browse", width = 8, command= lambda:dir_select()).place(x=230,y=40)
output_entry = Entry(root,width = 25)
output_entry.place(x=70,y=44)
output_entry.insert(END, out_path)
Label(root,text="Output Dir:").place(x=6,y=44)

seed_text = Label(root,text="Seed:").place(x=18,y=73)
sv = StringVar()
sv.set(seed)
seed_entry = Entry(root,textvariable=sv,width = 25)
seed_entry.place(x=70,y=74)
if len(seed_entry.get()) == 0:
    seed_entry.insert(END, str(seed))
Button(root,text="New Seed", width = 8, command= lambda:new_seed()).place(x=230,y=70)

game_mode = StringVar()
game_mode.set("Standard") # Default
options = ("Standard", "Competitive", "All Shuffled", "All Random", "Shuffle Balanced", "Random Balanced", "Chaotic", "True Chaos", "Slippi Unranked Mode")
option_menu = OptionMenu(root, game_mode, *options)
option_menu.place(x=67,y=100)
Label(root,text="Mode:").place(x=16,y=104)

Button(root,text="Randomize!", width = 9, command= lambda:start_randomizer()).place(x=225,y=150)
root.mainloop()

