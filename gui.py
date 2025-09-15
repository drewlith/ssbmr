import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import filedialog
from tkinter import Scrollbar
from tkinter import messagebox
from tkinter import font
import json, string, random, re, requests, webbrowser, threading, os

with open ('Data/options.json', 'r') as file:
    options_dict = json.load(file)

with open ('Data/standard.json', 'r') as file:
    standard_dict = json.load(file)

with open ('Data/special.json', 'r') as file:
    special_dict = json.load(file)

with open ('Data/gecko.json', 'r') as file:
    gecko_dict = json.load(file)

with open ('Data/custom.json', 'r') as file:
    custom_dict = json.load(file)

root = tk.Tk()
# Basic Window
root.iconbitmap('Data/logo.ico')
root.geometry("800x600")
root.resizable(False, False)
root.title("Melee Randomizer v1.0 by drewlith")

main_screen = tk.Frame(root)
main_screen.columnconfigure(0, weight=3, uniform="a")
main_screen.columnconfigure(1, weight=6, uniform="a")
success_screen = tk.Frame(root)
generating_screen = tk.Frame(root)
generating_label = tk.Label(generating_screen, text="Seed is generating... Please wait!", font="OpenSans 16")
generating_label.pack()

# ISO PATH, SEED, OUTPUT PATH
def browse_file():
    filepath = filedialog.askopenfilename(
        title="Select Melee v1.02 NTSC ISO",
        filetypes=[("Gamecube ISOs", "*.iso")])
    iso_input.delete(0, tk.END)
    iso_input.insert(0, filepath)

def browse_folder():
    folder = filedialog.askdirectory()
    out_input.delete(0, tk.END)
    out_input.insert(0, folder)


header_frame = tk.Frame(main_screen)
label = tk.Label(header_frame, text="ISO Path")
label.grid(row=0, column=0, pady=5, sticky="e")
iso_input = tk.Entry(header_frame, width=64)
iso_input.insert(0, options_dict["ISO Path"])
iso_input.grid(row=0, column=1, sticky="ew", padx=10)
iso_browse_button = tk.Button(header_frame, text="Browse", command=browse_file, width=8)
iso_browse_button.grid(row=0, column=2)

label = tk.Label(header_frame, text="Output Path")
label.grid(row=1, column=0, pady=5, sticky="e")
out_input = tk.Entry(header_frame, width=64)
out_input.insert(0, options_dict["Output Path"])
out_input.grid(row=1, column=1, sticky="ew", padx=10)
out_browse_button = tk.Button(header_frame, text="Browse", command=browse_folder, width=8)
out_browse_button.grid(row=1, column=2)

label = tk.Label(header_frame, text="Seed")
label.grid(row=2, column=0, pady=5, sticky="e")
seed_input = tk.Entry(header_frame, width=32)
seed_input.grid(row=2, column=1, sticky="ew", padx=10)
seed_input.bind("<FocusOut>", lambda e:update_flagset())

header_frame.grid(row=0, columnspan=2)

# TABS
style = ttk.Style()
# Configure padding for TNotebook.Tab
style.configure("TNotebook.Tab", padding=[20, 5], width="15", anchor="center") # [left/right, top/bottom]

def tab_controller_on_leave(event):
    if event.y < 50 or event.y > 150:
        update_infobox(DEFAULT_MESSAGE)
tab_controller = ttk.Notebook(main_screen)
tab_controller.bind("<Leave>", tab_controller_on_leave)
main_tab = ttk.Frame(tab_controller)
main_tab.grid_columnconfigure(1, weight=1)
main_tab.grid_rowconfigure(0, weight=1)
main_tab.columnconfigure(1, weight=1)
special_tab = ttk.Frame(tab_controller)
special_tab.grid_columnconfigure(1, weight=1)
special_tab.grid_rowconfigure(0, weight=1)
special_tab.columnconfigure(1, weight=1)
shuffle_tab = ttk.Frame(tab_controller)
shuffle_tab.grid_columnconfigure(1, weight=1)
shuffle_tab.grid_rowconfigure(0, weight=1)
shuffle_tab.columnconfigure(1, weight=1)
gecko_tab = ttk.Frame(tab_controller)
gecko_tab.grid_columnconfigure(1, weight=1)
gecko_tab.grid_rowconfigure(0, weight=1)
gecko_tab.columnconfigure(1, weight=1)
custom_tab = ttk.Frame(tab_controller)
custom_tab.grid_columnconfigure(1, weight=1)
custom_tab.grid_rowconfigure(0, weight=1)
custom_tab.grid_rowconfigure(1, weight=10)
custom_tab.columnconfigure(1, weight=1)
tab_controller.add(main_tab, text="Standard Flags")
tab_controller.add(shuffle_tab, text="Shuffle")
tab_controller.add(special_tab, text="Special Flags")
tab_controller.add(gecko_tab, text="Gecko Codes")
tab_controller.add(custom_tab, text="Custom Flags")
tab_controller.grid(row=1, columnspan=2, sticky="nsew", padx=5)
infoboxes = []
def update_infobox(text):
    for info in infoboxes:
        info.config(state="normal")
        info.delete("1.0", tk.END)
        info.insert("1.0", text)
        info.config(state="disabled")
# TAB CONTENT

# MAIN
DEFAULT_MESSAGE = "Welcome to Melee Randomizer! To get started, browse for a Super Smash Bros. Melee v1.02 ISO path and an output path and input them in the fields above (they will be remembered). If you leave the 'seed' field blank, a random seed will be assigned. You may then configure the randomizer however you wish by checking various 'Flags' on the left, however the default settings work fine too! Hover over a Flag to see what it does. Once you've selected all the options you want, click Randomize at the bottom right and a new ISO will be created at the path you specified. Any ISO generated with the same seed and settings should be compatible to play online! All seeds should also be console compatible. Have fun, and randomize often!"
flags_frame = tk.Frame(main_tab)
flags_frame.grid(row=0, column=0, sticky="nsew", pady=5, padx=5)
infobox = scrolledtext.ScrolledText(main_tab, height=18, background=None)
infobox.config(highlightthickness=0, borderwidth=0, wrap=tk.WORD)
infobox.grid(row=0, column=1, pady=5, sticky="nsew")
infobox.insert("1.0", DEFAULT_MESSAGE)
infobox.config(state="disabled")
infoboxes.append(infobox)
# Shuffle
def trace_update_flags(*args):
    update_flagset()
shuffle_frame = tk.Frame(shuffle_tab)
shuffle_frame.grid(row=0, column=0, sticky="nsew", pady=5, padx=5)
shuffle_infobox = scrolledtext.ScrolledText(shuffle_tab, height=18, background=None)
shuffle_infobox.config(highlightthickness=0, borderwidth=0, wrap=tk.WORD)
shuffle_infobox.grid(row=0, column=1, pady=5, sticky="nsew")
shuffle_infobox.insert("1.0", DEFAULT_MESSAGE)
shuffle_infobox.config(state="disabled")
infoboxes.append(shuffle_infobox)
choices = ['Balanced', 'Unbalanced']
choicevar = tk.StringVar(main_screen)
choicevar.set('Balanced')
choicevar.trace_add("write", trace_update_flags)
choicemenu = tk.OptionMenu(shuffle_frame, choicevar, *choices)
choicemenu.pack()
choicemenu.config(width=20, height=2)
choicemenu.bind("<Enter>", lambda text:update_infobox("Puts all hitboxes into a pool, shuffles them, and redistributes them. This could turn Jigglypuff's Rest into Captain Falcon's knee, for example. The percentage dictates the chance a hitbox will be added to the pool. Balanced will create tiered pools where hitboxes are grouped based on their relative power level, making it so really strong moves only shuffle with other really strong moves, or weak moves only shuffle with weak moves, etc..."))
percent_label = tk.Label(shuffle_frame, text="\n\nShuffle Percent")
percent_label.pack()
percent_input = tk.Scale(shuffle_frame, from_=0, to=100, orient=tk.HORIZONTAL, length=200)
percent_input.set(25)
percent_input.config(command=trace_update_flags)
percent_input.bind("<Enter>", lambda text:update_infobox("Puts all hitboxes into a pool, shuffles them, and redistributes them. This could turn Jigglypuff's Rest into Captain Falcon's knee, for example. The percentage dictates the chance a hitbox will be added to the pool. Balanced will create tiered pools where hitboxes are grouped based on their relative power level, making it so really strong moves only shuffle with other really strong moves, or weak moves only shuffle with weak moves, etc..."))
percent_input.pack()
# Special
special_frame = tk.Frame(special_tab)
special_frame.grid(row=0, column=0, sticky="nsew", pady=5, padx=5)
special_infobox = scrolledtext.ScrolledText(special_tab, height=18, background=None)
special_infobox.config(highlightthickness=0, borderwidth=0, wrap=tk.WORD)
special_infobox.grid(row=0, column=1, pady=5, sticky="nsew", )
special_infobox.insert("1.0", DEFAULT_MESSAGE)
special_infobox.config(state="disabled")
infoboxes.append(special_infobox)
# Gecko
def on_mousewheel(event):
    gecko_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    custom_canvas.yview_scroll(int(-1*(event.delta/120)), "units")

gecko_frame = tk.Frame(gecko_tab)
gecko_infobox = scrolledtext.ScrolledText(gecko_tab, height=18, background=None)
gecko_infobox.config(highlightthickness=0, borderwidth=0, wrap=tk.WORD)
gecko_infobox.grid(row=0, column=1, pady=5, sticky="nsew")
gecko_infobox.insert("1.0", DEFAULT_MESSAGE)
gecko_infobox.config(state="disabled")
gecko_canvas = tk.Canvas(gecko_frame, borderwidth=0, highlightthickness=0)
gecko_canvas.bind_all("<MouseWheel>", on_mousewheel)
gecko_scroll_frame = tk.Frame(gecko_canvas)
gecko_scroll_frame.bind(
    "<Configure>",
    lambda e: gecko_canvas.configure(
        scrollregion=gecko_canvas.bbox("all")
    )
)
gecko_canvas.create_window((0, 0), window=gecko_scroll_frame, anchor="nw")
gecko_canvas.grid(row=0,column=0, sticky="nsew")
gecko_scroll = Scrollbar(gecko_frame, orient="vertical", command=gecko_canvas.yview)
gecko_frame.grid(row=0, column=0, sticky="nsew", pady=5, padx=5)
gecko_scroll.grid(row=0, column=1, sticky='ns')
gecko_canvas.configure(yscrollcommand=gecko_scroll.set)

infoboxes.append(gecko_infobox)

# Custom

# Import Flags
def import_custom_json():
    global custom_dict
    filepath = filedialog.askopenfilename(
        title="Select custom.json",
        filetypes=[("JSON", "*.json")])
    if len(filepath) < 1:
        return
    response = messagebox.askquestion(title="Overwriting", message="Warning! Importing flags will overwrite all existing custom flags. If you only want to add a few flags, try using 'Add New Flag' instead. Continue?")
    if response == "yes":
        with open(filepath, 'r') as file:
            data_dict = json.load(file)
        custom_dict = data_dict
        with open("Data/custom.json", 'w') as f:
            json.dump(custom_dict, f, indent=4)
        load_custom_flags()
    return

# Export Flags
def export_custom_json():
    folder = filedialog.askdirectory()
    with open(folder + "/export.json", 'w') as f:
        json.dump(custom_dict, f, indent=4)
    messagebox.showinfo(title="Export Flags", message="Exported successfully to: " + folder + "/export.json")

# Add Flags
def open_add_flag_window():
    def add_flag_to_custom_dict():
        if len(add_name_entry.get()) < 1:
            messagebox.showerror(title="Invalid", message="Flag name field cannot be empty.")
            return
        if len(add_command_infobox.get("1.0", tk.END).replace("\n", "")) < 1:
            messagebox.showerror(title="Invalid", message="Flag commands field cannot be empty.")
            return
        flag_dict = {}
        flag_dict["Commands"] = add_command_infobox.get("1.0", tk.END).replace("\n", "")
        flag_dict["Description"] = add_description_infobox.get("1.0", tk.END).replace("\n", "")
        flag_dict["Credit"] = add_creator_entry.get()
        custom_dict[add_name_entry.get()] = flag_dict
        with open("Data/custom.json", 'w') as f:
            json.dump(custom_dict, f, indent=4)
        load_custom_flags()
        add_window.destroy()

    add_window = tk.Toplevel(main_screen)
    add_window.title("Add new Flag")
    add_window.geometry("600x450")
    add_window.attributes("-topmost", True)
    add_window.grab_set()
    add_window.focus_set()
    add_window.transient(main_screen)
    add_name_label = tk.Label(add_window, text="Enter Flag Name")
    add_name_label.pack(pady=4)
    add_name_entry = tk.Entry(add_window)
    add_name_entry.pack()
    add_creator_label = tk.Label(add_window, text="Enter Your Name or Gamer Tag (Optional)")
    add_creator_label.pack(pady=4)
    add_creator_entry = tk.Entry(add_window)
    add_creator_entry.pack()
    add_description_label = tk.Label(add_window, text="Enter Flag Description")
    add_description_label.pack(pady=4)
    add_description_infobox = scrolledtext.ScrolledText(add_window, height=7)
    add_description_infobox.pack(padx=10)
    add_command_label = tk.Label(add_window, text="Enter Flag Commands (CTRL + V works to paste)")
    add_command_label.pack(pady=4)
    add_command_infobox = scrolledtext.ScrolledText(add_window, height=8)
    add_command_infobox.pack(padx=10)
    add_button_frame = tk.Frame(add_window, pady=5)
    add_flag_button = tk.Button(add_button_frame, text="Add Flag", width=10, command=add_flag_to_custom_dict)
    add_flag_button.grid(row=0,column=0)
    close_button = tk.Button(add_button_frame, text="Close", command=add_window.destroy, width=8)
    close_button.grid(row=0,column=1, padx=20)
    add_button_frame.pack()

# Remove Flags
class CustomFlag:
    def __init__(self, main_screen, key, row, color):
        self.key = key
        self.main_screen = main_screen
        self.frame = tk.Frame(main_screen, height=2)
        self.label = tk.Label(self.frame, text=key, width=40, background=color).grid(row=0, column=0, sticky="ns")
        self.button = tk.Button(self.frame, text="Remove", width=10, command=self.remove_flag).grid(row=0, column=1)
        self.frame.pack()
    
    def remove_flag(self):
        del custom_dict[self.key]
        with open("Data/custom.json", 'w') as f:
            json.dump(custom_dict, f, indent=4)
        self.main_screen.destroy()
        open_remove_flags_window()
        load_custom_flags()

def open_remove_flags_window():
    remove_window = tk.Toplevel(main_screen)
    remove_window.title("Remove Flags")
    remove_window.geometry("600x450")
    remove_window.attributes("-topmost", True)
    remove_window.grab_set()
    remove_window.focus_set()
    remove_window.transient(main_screen)
    add_name_label = tk.Label(remove_window, text="Remove Flags")
    add_name_label.pack(pady=4)
    custom_flags = []
    colors = ["lightgray", "gray95"]
    row = 0
    for key in custom_dict:
        custom_flags.append(CustomFlag(remove_window, key, row, colors[row%2]))
        row += 1
    if len(custom_flags) < 1:
         tk.Label(remove_window, text="But there were not any custom flags...", pady=10).pack()
    close_button = tk.Button(remove_window, text="Close", command=remove_window.destroy, width=8)
    close_button.pack()

def on_mousewheel(event):
    custom_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
custom_frame = tk.Frame(custom_tab)
custom_ui_frame = tk.Frame(custom_tab)
custom_buttons_frame = tk.Frame(custom_ui_frame)
custom_buttons_frame.columnconfigure(0,weight=1)
custom_buttons_frame.columnconfigure(1,weight=1)
custom_buttons_frame.columnconfigure(2,weight=1)
custom_import = tk.Button(custom_buttons_frame, text="Import Flags", width=12, command=import_custom_json)
custom_import.grid(row=0,column=0, sticky="ew")
custom_export = tk.Button(custom_buttons_frame, text="Export Flags", width=12, command=export_custom_json)
custom_export.grid(row=0,column=1, sticky="ew")
custom_add = tk.Button(custom_buttons_frame, text="Add New Flag", width=12, command=open_add_flag_window)
custom_add.grid(row=0,column=2, sticky="ew")
custom_remove = tk.Button(custom_buttons_frame, text="Remove Flag", width=12, command=open_remove_flags_window)
custom_remove.grid(row=0,column=3, sticky="ew")
custom_infobox = scrolledtext.ScrolledText(custom_ui_frame, height=16, background=None)
custom_infobox.config(highlightthickness=0, borderwidth=0, wrap=tk.WORD)
custom_buttons_frame.pack(pady=5, anchor="w")
custom_infobox.pack()
custom_infobox.insert("1.0", DEFAULT_MESSAGE)
custom_infobox.config(state="disabled")
custom_ui_frame.grid(row=0, column=1)
custom_canvas = tk.Canvas(custom_frame, borderwidth=0, highlightthickness=0)
custom_scroll_frame = tk.Frame(custom_canvas)
custom_scroll_frame.bind(
    "<Configure>",
    lambda e: custom_canvas.configure(
        scrollregion=custom_canvas.bbox("all")
    )
)
custom_canvas.create_window((0, 0), window=custom_scroll_frame, anchor="nw")
custom_canvas.grid(row=0,column=0, sticky="nsew")
custom_scroll = Scrollbar(custom_frame, orient="vertical", command=custom_canvas.yview)
custom_frame.grid(row=0, column=0, sticky="nsew", pady=5, padx=5)
custom_scroll.grid(row=0, column=1, sticky='ns')
custom_canvas.configure(yscrollcommand=custom_scroll.set)
infoboxes.append(custom_infobox)

# FLAGSET
def get_all_substrings(string, start_delim, end_delim):
    pattern = re.escape(start_delim) + "(.*?)" + re.escape(end_delim)
    results = re.findall(pattern, string)
    return results

def update_gui(event=None):
    flags = get_all_substrings(flagset.get("1.0", tk.END), "/", "/")
    for flag in GUIFlag.all_flags:
        flag.checkvar.set(0)
        flag_name = flag.name.replace(" ", "_")
        flag_name = flag_name.lower()
        if flag_name in flags:
            flag.checkvar.set(1)
    percent_input.set(0)
    for flag in flags:
        if "shuffle_balanced" in flag:
            choicevar.set("Balanced")
            parameter = flag.replace("shuffle_balanced ", "")
            percent_input.set(int(parameter))
        elif "shuffle_unbalanced" in flag:
            choicevar.set("Unbalanced")
            parameter = flag.replace("shuffle_unbalanced ", "")
            percent_input.set(int(parameter))
        if "seed" in flag:
            seed_input.delete(0, tk.END)
            seed_input.insert(0, flag.replace("seed ", ""))
    update_flagset()

flagset = scrolledtext.ScrolledText(main_screen, height=7)
flagset.bind("<FocusOut>", lambda e:update_gui())
flagset.grid(row=4, columnspan=2, pady=5, sticky="nsew", padx=10)

def update_flagset():
    string = ""
    if len(seed_input.get()) > 0:
        string += "/seed " + seed_input.get() + "/ "
    for flag in GUIFlag.all_flags:
        if flag.checkvar.get() == 1:
            flag_name = flag.name.lower().replace(" ", "_")
            string += "/" + flag_name + "/ "
    if percent_input.get() > 0:
        shuffle_flag = "/shuffle_"
        if choicevar.get() == "Balanced":
            shuffle_flag += "balanced"
        else:
            shuffle_flag += "unbalanced"
        shuffle_flag += " " + str(percent_input.get()) + "/"
        string += shuffle_flag
    flagset.delete("1.0", tk.END)
    flagset.insert("1.0", string)

# BUTTONS

def generate_random_alphanumeric(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    vowels = 'aeiouAEIOU'
    consonents = 'qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM'
    for vowel in vowels:
        random_string = random_string.replace(vowel, consonents[random.randint(0,len(consonents)-1)])
    return random_string
#########################################################################################
# RANDOMIZE
#########################################################################################
def generate_online(_flagset, seed):
    url = "https://ssbmr.com/generate"
    payload = {
        "seed": seed,
        "flags": _flagset
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            share_link_var.set(response.text)
    except:
        messagebox.showerror("Network Error: Seed could not be generated online. The server may be down or there may be no internet connection.")

def check_thread_status(root, thread):
    if thread.is_alive():
        root.after(100, check_thread_status, root, thread)
    else:
        generating_screen.place_forget()
        success_screen.pack()

def start_randomizer():
    _flagset = ""
    for flag in GUIFlag.all_flags:
        if flag.checkvar.get() == 1:
            _flagset += flag.commands + " "
    # Shuffle Flag        
    if percent_input.get() > 0:
        shuffle_flag = "|shuffle_hitboxes"
        if choicevar.get() == "Balanced":
            shuffle_flag += "_balanced"
        shuffle_flag += " " + str(percent_input.get()) + "|"
        _flagset += shuffle_flag
    ###
    #with open('flags_test.txt', 'w') as f: f.write(_flagset)
    iso_path = iso_input.get()
    options_dict["ISO Path"] = iso_path
    output_path = out_input.get()
    options_dict["Output Path"] = output_path
    options_dict["Online Seed"] = online_var.get()
    options_dict["Show Commands"] = show_command_var.get()
    options_dict["Log"] = log_var.get()
    seed = seed_input.get()
    if len(seed) < 1:
        seed = generate_random_alphanumeric(10)
    iso_name = "/" + seed + " - Melee Randomizer v1.0.iso"

    with open("Data/options.json", "w") as f:
        json.dump(options_dict, f, indent=4)

    gen_log = False
    if log_var.get() == 1:
        gen_log = True
    import ssbmr
    local_thread = threading.Thread(target=ssbmr.generate_seed, args=(_flagset, iso_path, output_path + iso_name, seed, gen_log))
    local_thread.start()
    #ssbmr.generate_seed(_flagset, iso_path, output_path + iso_name, seed)
    generating_screen.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
    main_screen.pack_forget()
    success_flagset.insert("1.0", flagset.get("1.0", tk.END))
    success_flagset.config(state="disabled")
    if online_var.get() == 0:
        check_thread_status(root, local_thread)
        share_label.pack_forget()
        link_frame.pack_forget()
    if online_var.get() == 1:
        online_thread = threading.Thread(target=generate_online, args=(_flagset, seed))
        online_thread.start()
        check_thread_status(root, online_thread)
        #generate_online(_flagset)
    

randomize_button = tk.Button(main_screen, text="Randomize!", command=start_randomizer, width=10)
randomize_button.grid(row=5, column=1, sticky="se", padx=10)

def copy_to_clipboard(text):
    main_screen.clipboard_clear()
    main_screen.clipboard_append(text)

def paste_from_clipboard():
    clipboard_content = main_screen.clipboard_get()
    flagset.delete("1.0", tk.END)
    flagset.insert(tk.INSERT, clipboard_content)
    update_gui()

copy_paste_frame = tk.Frame(main_screen)
copy_paste_frame.grid(row=5, column=0, sticky="sw", padx=10)
copy = tk.Button(copy_paste_frame, text = "Copy Flagset", width=12, command=lambda:copy_to_clipboard(flagset.get("1.0", tk.END).replace("\n", "")))
copy.grid(row=0, column=0)
paste = tk.Button(copy_paste_frame, text = "Paste Flagset", width=12, command=paste_from_clipboard)
paste.grid(row=0, column=1, padx=4)

# ETC...
show_command_var = tk.IntVar()
show_command_check = tk.Checkbutton(main_screen, text="Show Commands", variable=show_command_var)
show_command_check.place(x=250, y=560)
show_command_var.set(options_dict["Show Commands"])

online_var = tk.IntVar()
online_check = tk.Checkbutton(main_screen, text="Generate on ssbmr.com", variable=online_var)
online_check.place(x=380, y=560)
online_var.set(options_dict["Online Seed"])

log_var = tk.IntVar()
log_check = tk.Checkbutton(main_screen, text="Generate JSON log", variable=log_var)
log_check.place(x=540, y=560)
log_var.set(options_dict["Log"])

class GUIFlag():
    max_width = 0
    global_rows = 0
    all_flags = []
    def __init__(self, main_screen, name, commands, description, credit, default_on=0):
        self.name = name
        self.description = description
        self.credit = credit
        self.commands = commands
        self.frame = tk.Frame(main_screen, borderwidth=1)
        self.frame.grid(row=GUIFlag.global_rows, column=0, sticky="nsew")
        self.frame.bind("<Enter>", self.on_mouse_enter)
        self.frame.bind("<Leave>", self.on_mouse_leave)
        self.frame.bind("<Button-1>", self.on_click)
        self.checkvar = tk.IntVar()
        self.checkvar.set(default_on)
        self.checkbox = tk.Checkbutton(self.frame, variable=self.checkvar)
        self.checkbox.bind("<Enter>", self.on_mouse_enter_child)
        self.checkbox.bind("<Leave>", self.on_mouse_leave_child)
        self.label = tk.Label(self.frame, text=name, justify="left")
        self.label.grid(row=0, column=1, sticky="nsew")
        self.label.bind("<Enter>", self.on_mouse_enter_child)
        self.label.bind("<Leave>", self.on_mouse_leave_child)
        self.label.bind("<Button-1>", self.on_click)
        self.checkbox.grid(row=0, column=0, sticky='w', padx=3)
        self.frame.update_idletasks()
        if self.frame.winfo_width() > GUIFlag.max_width:
            GUIFlag.max_width = self.frame.winfo_width()
        GUIFlag.global_rows += 1
        GUIFlag.all_flags.append(self)
    
    def on_mouse_enter(self, event):
        event.widget.config(bg='gold')
        for child in event.widget.winfo_children():
            child.config(bg="gold")
        string = self.description + "\n\nCredit: " + self.credit
        if show_command_var.get() == 1:
            string += "\n\nCommands: " + self.commands
        update_infobox(string)
    
    def on_mouse_leave(self, event):
        event.widget.config(bg='gray95')
        for child in event.widget.winfo_children():
            child.config(bg="gray95")

    def on_mouse_enter_child(self, event):
        event.widget.master.config(bg='gold')
        for child in event.widget.master.winfo_children():
            child.config(bg="gold")
        string = self.description + "\n\nCredit: " + self.credit
        if show_command_var.get() == 1:
            string += "\n\nCommands: " + self.commands
        update_infobox(string)

    def on_mouse_leave_child(self, event):
        event.widget.master.config(bg='gray95')
        for child in event.widget.master.winfo_children():
            child.config(bg="gray95")
    
    def on_click(self, event):
        if self.checkvar.get() < 1:
            self.checkvar.set(1)
            update_flagset()
            return
        self.checkvar.set(0)
        update_flagset()

    def destroy(self):
        self.frame.destroy()

for key in standard_dict:
    GUIFlag(flags_frame, key, standard_dict[key]["Commands"], 
            standard_dict[key]["Description"], 
            standard_dict[key]["Credit"],
            1)
GUIFlag.global_rows = 0
for key in special_dict:
    GUIFlag(special_frame, key, special_dict[key]["Commands"], 
            special_dict[key]["Description"], 
            special_dict[key]["Credit"])
GUIFlag.global_rows = 0   
for key in gecko_dict:
    GUIFlag(gecko_scroll_frame, key, gecko_dict[key]["Commands"], 
            gecko_dict[key]["Description"], 
            gecko_dict[key]["Credit"])
gecko_canvas.configure(width=GUIFlag.max_width)
custom_flags = []
def load_custom_flags():
    for flag in custom_flags:
        flag.destroy()
    custom_flags.clear()
    GUIFlag.global_rows = 0
    GUIFlag.max_width = 0
    for key in custom_dict:
        custom_flags.append(GUIFlag(custom_scroll_frame, key, custom_dict[key]["Commands"], 
                custom_dict[key]["Description"], 
                custom_dict[key]["Credit"]))
    if len(custom_flags) < 1:
        GUIFlag.max_width = 200
    custom_canvas.configure(width=GUIFlag.max_width)
load_custom_flags()
update_flagset()
main_screen.pack()

### SUCCESS SCREEN ###
def open_link(url):
    webbrowser.open_new_tab(url)

def open_specific_folder():
    folder_path = out_input.get()  # Example for Windows
    if os.name == 'nt':  # Windows
        os.startfile(folder_path)
    elif os.name == 'posix':  # Linux or macOS
        os.system(f'xdg-open "{folder_path}"' if 'Linux' in os.uname().sysname else f'open "{folder_path}"')

def generate_again():
    success_screen.pack_forget()
    main_screen.pack()
    
share_link_var = tk.StringVar()
random_affirmations = ["amazing", "wonderful", "excellent", "outstanding", "expertly-crafted", "awesome", "genius", "crazy"]
affirmation = random_affirmations[random.randint(0, len(random_affirmations)-1)]
success_label = tk.Label(success_screen, text="Your " + affirmation + " seed generated successfully! It can be found at the path below.", pady=5, font="OpenSans 14")
path_frame = tk.Frame(success_screen)
path_label = tk.Label(path_frame, text="Path: " + out_input.get(), pady=5, font="OpenSans 12")
path_button = tk.Button(path_frame, text="Open Folder", command=open_specific_folder)
share_label = tk.Label(success_screen, text="Your seed is accessible online at the following link: ", pady=5, font="OpenSans 14")
link_frame = tk.Frame(success_screen)
link_label = tk.Label(link_frame, textvariable=share_link_var, fg="blue", cursor="hand2", font="OpenSans 12")
link_label.bind("<Button-1>", lambda e: open_link(share_link_var.get()))
link_copy = tk.Button(link_frame, text="Copy Link", command=lambda:copy_to_clipboard(share_link_var.get()))
flagset_frame = tk.Frame(success_screen)
flagset_label = tk.Label(flagset_frame, text="Flagset", justify="left", font="OpenSans 14")
flagset_copy_button = tk.Button(flagset_frame, text="Copy Flags", command=lambda:copy_to_clipboard(flagset.get("1.0", tk.END).replace("\n", "")))
success_flagset = scrolledtext.ScrolledText(flagset_frame, height=7)

social_frame = tk.Frame(success_screen)
yt = tk.PhotoImage(file="Data/youtube.png")
twitch = tk.PhotoImage(file="Data/twitch.png")
twitter = tk.PhotoImage(file="Data/twitter.png")
bluesky = tk.PhotoImage(file="Data/bluesky.png")
social_label = tk.Label(social_frame, text="Follow me!", font="OpenSans 12")
yt_label = tk.Label(social_frame, image=yt, cursor="hand2")
yt_label.bind("<Button-1>", lambda e: open_link("https://www.youtube.com/@drewlith"))
twitch_label = tk.Label(social_frame, image=twitch, cursor="hand2")
twitch_label.bind("<Button-1>", lambda e: open_link("https://www.twitch.tv/drewlith"))
twitter_label = tk.Label(social_frame, image=twitter, cursor="hand2")
twitter_label.bind("<Button-1>", lambda e: open_link("https://x.com/drewlith"))
bluesky_label = tk.Label(social_frame, image=bluesky, cursor="hand2")
bluesky_label.bind("<Button-1>", lambda e: open_link("https://bsky.app/profile/drewlith.bsky.social"))
generate_again_button = tk.Button(success_screen, text="Generate Another Seed", width=20, height=2, font="TkDefaultFont 14", command=generate_again)

random_yummies = ["Coffee", "Ice Cream Cone", "Burger", "Plate of Spaghetti", "Bowl of Goulash", "Taco", "Soda", "Lollipop", "Root Beer Float", "Sundae", "Quesadilla", "Cheesecake", "Sweet Tea", "Bubble Tea", "Plate of Alfredo", "Salad", "Bowl of Soup", "Gyro", "Pizza", "Calzone", "Candy Bar"]
donation_label = tk.Label(success_screen, text="Buy me a " + random_yummies[random.randint(0,len(random_yummies)-1)] + "! (Ko-fi)", fg="blue", cursor="hand2", font="OpenSans 12")
donation_label.bind("<Button-1>", lambda e: open_link("https://ko-fi.com/drewlitherland"))

success_label.pack()
path_label.grid(row=0,column=0)
path_button.grid(row=0,column=1, padx=5)
path_frame.pack()
share_label.pack()
link_label.grid(row=0,column=0)
link_copy.grid(row=0, column=1, padx=5)
link_frame.pack()
flagset_label.grid(row=0, column=0, sticky="w")
flagset_copy_button.grid(row=0, column=1, sticky="e", padx=3)
success_flagset.grid(row=1, columnspan=2)
flagset_frame.pack()

generate_again_button.pack(pady=10)
social_label.grid(row=0, column=0, pady=5)
twitch_label.grid(row=0, column=1)
twitter_label.grid(row=0, column=2)
yt_label.grid(row=0, column=3)
bluesky_label.grid(row=0, column=4)
social_frame.pack()
donation_label.pack()
root.mainloop()




