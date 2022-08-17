import randomizer, json, threading, time, util
import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import tkinter.font as font
from tkinter.filedialog import askopenfile, askdirectory
from tkinter import ttk
from os.path import exists

bg_color = "#0A003C"

# Path/ISO Settings
class ApplicationMain():
    def __init__(self, master):
        self.master = master
        self.randomizing = False
        self.frame = tk.Frame(master)
        self.iso_path = tk.StringVar()
        self.output_path = tk.StringVar()
        self.information = tk.StringVar()
        self.description = tk.StringVar()
        file = open(r"data/presets.json")
        self.presets = json.load(file)
        self.preset_keys = []
        for key in self.presets:
            if key != "Flags" and key != "Description":
                self.preset_keys.append(key)
        self.description.set(self.presets[self.preset_keys[0]]["Description"])
        self.background = tk.PhotoImage(file=r"data/background.png")
        self.menu_button = tk.PhotoImage(file=r"data/menu_button.png")
        ui_font_large = font.Font(family="data/Folk.otf",size=22)
        ui_font_medium = font.Font(family="data/Folk.otf",size=16)
        ui_font_small = font.Font(family="data/Folk.otf",size=12)
        self.information.set("SSBM Randomizer created by @drewlith.")

        # Background + Text
        canvas = tk.Canvas(master,width=600,height=450)
        canvas.place(x=-2,y=0)
        canvas.create_image(0,0,image=self.background,anchor="nw")
        canvas.create_text(25,50,text="ISO Path",anchor=tk.SW,font=ui_font_medium,fill="white")
        canvas.create_text(12,90,text="Output Path",anchor=tk.SW,font=ui_font_medium,fill="white")
        canvas.create_text(42,130,text="Seed",anchor=tk.SW,font=ui_font_medium,fill="white")
        canvas.create_text(35,170,text="Preset",anchor=tk.SW,font=ui_font_medium,fill="white")
        canvas.create_text(40,264,text="Flags",anchor=tk.SW,font=ui_font_medium,fill="white")

        # Information
        tk.Label(master,bg=bg_color,fg='white',textvariable=self.information,font=ui_font_small).place(x=8,y=425)
        # ISO Browser
        #tk.Label(master,fg='white',bg=bg_color,text="ISO Path",font=ui_font_medium).place(x=22,y=21)
        tk.Entry(master,textvariable=self.iso_path,width=58).place(x=130,y=27)
        tk.Button(master, text="Browse",font=ui_font_small, width=8,command=lambda:self.select_iso()).place(x=495,y=20)
        # Output Dir Browser
        #tk.Label(master,fg='white',bg=bg_color,text="Output Path",font=ui_font_medium).place(x=8,y=61)
        tk.Entry(master,textvariable=self.output_path,width=58).place(x=130,y=67)
        tk.Button(master, text="Browse",font=ui_font_small, width=8,command=lambda:self.select_out_path()).place(x=495,y=60)
        # Seed Creator
        #tk.Label(master,fg='white',bg=bg_color,text="Seed",font=ui_font_medium).place(x=41,y=101)
        self.seed_var = tk.StringVar()
        self.seed_var.trace("w", self.update_flags_box)
        self.seed_creator = tk.Entry(master,width=58,textvariable=self.seed_var)
        self.seed_creator.place(x=130,y=107)
        # Preset Chooser
        #tk.Label(master,fg='white',bg=bg_color,text="Preset",font=ui_font_medium).place(x=35,y=141)
        self.presets_menu = ttk.Combobox(master,value=self.preset_keys,width=55)
        self.presets_menu.place(x=130,y=147)
        self.presets_menu.current(0)
        self.presets_menu['state'] = 'readonly'
        self.presets_menu.bind("<<ComboboxSelected>>", self.update_preset_text)
        tk.Button(master, text="Customize",font=ui_font_small, width=8,command=lambda:self.open_custom_window()).place(x=495,y=140)
        # Preset Description
        preset_info =tk.Label(master,fg='white',bg=bg_color,textvariable=self.description,font=ui_font_small,wraplength=360)
        preset_info.place(x=130,y=170)
        preset_info.justify = tk.LEFT
        # Flag Inputer
        #tk.Label(master,fg='white',bg=bg_color,text="Flags",font=ui_font_medium).place(x=41,y=235)
        self.flag_text_box = scrolledtext.ScrolledText(master,width=53,height=6)
        self.flag_text_box.place(x=130,y=242)
        self.flag_text_box.frame.bind("<<Modified>>", self.update_seed)
        # Copy Button
        tk.Button(master, text="Copy",font=ui_font_small, width=8,command=lambda:self.copy_flags()).place(x=23,y=270)
        # Paste Button
        tk.Button(master, text="Paste",font=ui_font_small, width=8,command=lambda:self.paste_flags()).place(x=23,y=310)
        # Randomize Button
        self.r_btn_text = tk.StringVar()
        self.r_btn_text.set("Randomize")
        self.randomize_btn = tk.Button(master,activebackground=bg_color,bg=bg_color,textvariable=self.r_btn_text,fg="orange",compound=tk.CENTER,font=ui_font_large, image=self.menu_button, borderwidth=0, command=lambda:self.generate_iso())
        self.randomize_btn.place(x=170,y=350)
        self.randomize_btn.bind('<ButtonPress-1>',self.button_pressed)
        self.randomize_btn.bind('<ButtonRelease-1>',self.button_released)

        self.update_preset_text(None)

        # Get Saved Data from JSON if it exists
        if exists("data/config.json"):
            file = open("data/config.json")
            data = json.load(file)
            self.iso_path.set(data["ISO Path"])
            self.output_path.set(data["Output Path"])

    def paste_flags(self):
        self.flag_text_box.delete("1.0", tk.END)
        flags = self.master.clipboard_get()
        self.flag_text_box.insert(tk.INSERT, flags)
        self.update_seed()
        self.update_information("Pasted flags from clipboard.")

    def copy_flags(self):
        self.master.clipboard_clear()
        self.master.clipboard_append(self.flag_text_box.get("1.0", tk.END).strip())
        self.update_information("Copied flags to clipboard.")

    def update_seed(self):
        flags = self.flag_text_box.get("1.0", tk.END)
        if "-seed" in flags:
            self.seed_var.set(util.get_string_between(flags, "-seed ", " -"))

    def update_flags_box(self, *args):
        flags = self.flag_text_box.get("1.0", tk.END)
        if "-seed" in flags:
            string = util.get_string_between(flags, "-seed", "-")
            flags = flags.replace(string, "")
            flags = flags.replace("-seed", "")
            if len(self.seed_var.get()) > 0:
                flags = "-seed " + self.seed_var.get() + " " + flags
        elif len(self.seed_var.get()) > 0:
            flags = "-seed " + self.seed_var.get() + " " + flags
        self.flag_text_box.delete("1.0", tk.END)
        self.flag_text_box.insert(tk.INSERT, flags)

    def update_preset_text(self, event):
        self.description.set(self.presets[self.presets_menu.get()]["Description"])
        self.flag_text_box.delete("1.0", tk.END)
        self.flag_text_box.insert(tk.INSERT, self.presets[self.presets_menu.get()]["Flags"])

    def button_pressed(self, event):
        if self.randomizing: return
        self.menu_button['file'] = r"data/menu_selected.png"

    def button_released(self, event):
        if self.randomizing: return
        self.menu_button['file'] = r"data/menu_button.png"
   
    def select_iso(self):
        if self.randomizing: return
        file = askopenfile(parent=self.master,mode="rb",title="Select v1.02 ISO.",filetype=[("ISO File","*.iso")])
        if file:
            self.iso_path.set(file.name)
        self.update_information("ISO Path set: " + self.iso_path.get())

    def select_out_path(self):
        if self.randomizing: return
        path = askdirectory(parent=self.master,title="Select output directory.")
        if path:
            self.output_path.set(path)
        self.update_information("Output Path set: " + self.output_path.get())

    def randomize(self, iso_path, output_path, flags):
        self.update_information("Randomizing... Please wait")
        self.randomizing = True
        self.randomize_btn['state'] = 'disabled'
        randomizer.start(iso_path, output_path, flags)
        self.randomizing = False
        self.update_information("ISO generated! Path: " + self.output_path.get())
        self.randomize_btn['state'] = 'normal'

    def generate_iso(self):
        if self.randomizing: return
        if len(self.seed_creator.get()) > 1:
            flags = "-seed " + self.seed_creator.get() + " " + self.flag_text_box.get("1.0",tk.END)
        else:
            flags = self.flag_text_box.get("1.0",tk.END)
        args = [self.iso_path.get(),self.output_path.get(),flags]
        # Check for Errors
        for arg in args:
            if len(arg) <= 0:
                print("Error: Invalid argument: " + arg)
                return
        if ".iso" not in args[0]:
            self.update_information("Error: Chosen path is not an .iso")
            return
        # Start a Thread so App doesn't hang
        r = threading.Thread(target=self.randomize,args=(args))
        r.start()
        # Write Save Data to config.json
        data = {"ISO Path":args[0],"Output Path":args[1],"Flags":args[2]}
        with open('data/config.json','w') as file:
            json.dump(data,file,indent=2)

    def open_custom_window(self):
        if self.randomizing: return
        flags = self.flag_text_box.get("1.0",tk.END)
        for widget in self.master.winfo_children():
            widget.destroy()
        ApplicationCustom(self.master, flags)

    def update_information(self, string):
        if self.randomizing: return
        self.information.set(string)

class Tab():
    def __init__(self, master, c_menu, menu, x_pos, y_pos, text = "", default=False):
        self.master = master
        self.menu = menu
        self.c_menu = c_menu
        self.c_menu.tabs.append(self)
        ui_font_large = font.Font(family="data/Folk.otf",size=22)
        ui_font_medium = font.Font(family="data/Folk.otf",size=16)
        ui_font_small = font.Font(family="data/Folk.otf",size=12)
        self.tab = tk.Label(master,bg='#BB6622',fg='black',text=text,font=ui_font_medium,width=8)
        self.tab.place(x=x_pos,y=y_pos)
        self.tab.bind('<Button-1>', self.on_click)
        self.tab.bind('<Enter>', self.on_hover)
        self.tab.bind('<Leave>', self.on_leave)
        if default:
            self.tab.configure(fg="white", bg="orange")
            
    def on_hover(self, event):
        if type(self.c_menu.active_menu) == self.menu:
            return
        self.tab.configure(fg="white")

    def on_leave(self, event):
        if type(self.c_menu.active_menu) == self.menu:
            return
        self.tab.configure(fg="black")

    def on_click(self, event):
        if type(self.c_menu.active_menu) == self.menu:
            return
        for tab in self.c_menu.tabs:
            tab.reset()
        self.tab.configure(bg="orange",fg="white")
        self.c_menu.active_menu.clear()
        self.c_menu.active_menu = self.menu(self.master, self.c_menu)

    def reset(self):
        self.tab.configure(bg="#BB6622", fg ='black')

class ApplicationCustom():
    def __init__(self, master, flags):
        self.master = master
        ui_font_large = font.Font(family="data/Folk.otf",size=22)
        ui_font_medium = font.Font(family="data/Folk.otf",size=16)
        ui_font_small = font.Font(family="data/Folk.otf",size=12)
        self.background = tk.PhotoImage(file=r"data/background.png")
        self.flags = flags
        self.hitbox_flags = ""
        self.attribute_flags = ""
        self.misc_flags = ""
        self.seed = util.get_string_between(self.flags, "-seed ", " -")
        self.active_menu = None
        self.information = tk.StringVar()
        self.information.set("Activate and adjust flags to change what gets randomized!")
        # Background + Text
        canvas = tk.Canvas(master,width=600,height=450)
        canvas.place(x=-2,y=0)
        canvas.create_image(0,0,image=self.background,anchor="nw")
        canvas.create_text(20,50,text="Flags",anchor=tk.SW,font=ui_font_large,fill="white")
        tk.Label(master,bg=bg_color,fg='white',textvariable=self.information,font=ui_font_small).place(x=8,y=425)
        # Return button
        tk.Button(master, text="Done",font=ui_font_small, width=8,command=lambda:self.open_main_window()).place(x=505,y=410)
        # Hitbox Menu (default)
        self.active_menu = HitboxMenu(self.master, self)
        self.tabs = []

        # Tabs
        Tab(self.master,self,HitboxMenu,50,60,"Hitboxes",True)
        Tab(self.master,self,AttributeMenu,180,60,"Attributes")
        Tab(self.master,self,MiscMenu,310,60,"Misc.")
        Tab(self.master,self,PresetMenu,440,60,"Preset")

        # Initialize
        a = AttributeMenu(self.master, self)
        a.determine_settings()
        m = MiscMenu(self.master, self)
        m.determine_settings()
        a.clear()
        m.clear()

    def open_main_window(self):
        self.update_flags()
        for widget in self.master.winfo_children():
            widget.destroy()
        main_window = ApplicationMain(self.master)
        main_window.flag_text_box.delete('1.0', tk.END)
        main_window.flag_text_box.insert(tk.INSERT, self.flags)
        main_window.update_seed()

    def update_flags(self):
        self.flags = self.hitbox_flags + self.attribute_flags + self.misc_flags
        if len(self.seed) > 0:
            self.flags = "-seed " + self.seed + " " + self.flags

    def update_information(self, string):
        self.information.set(string)

class OneOptionFlag():
    def __init__(self, master, menu, name, flag_name, x_pos, y_pos):
        self.master = master
        self.menu = menu
        self.flag_name = flag_name
        ui_font_large = font.Font(family="data/Folk.otf",size=22)
        ui_font_medium = font.Font(family="data/Folk.otf",size=16)
        ui_font_small = font.Font(family="data/Folk.otf",size=12)
        self.flag_var = tk.IntVar()
        self.check = tk.Checkbutton(self.master, fg='white',bg=bg_color, font=ui_font_small, selectcolor=bg_color,
                            text=name, onvalue=1, offvalue=0, variable=self.flag_var, command=menu.determine_flags)
        self.check.place(x=x_pos,y=y_pos)
        menu.my_widgets.append(self.check)
        
class TwoOptionFlag():
    def __init__(self, master, menu, name, flag_name, x_pos, y_pos, label = "Shuffle %"):
        self.master = master
        self.menu = menu
        self.flag_name = flag_name
        ui_font_large = font.Font(family="data/Folk.otf",size=22)
        ui_font_medium = font.Font(family="data/Folk.otf",size=16)
        ui_font_small = font.Font(family="data/Folk.otf",size=12)
        self.flag_var = tk.IntVar()
        self.magnitude = tk.IntVar()
        self.check = tk.Checkbutton(self.master, fg='white',bg=bg_color, font=ui_font_small, selectcolor=bg_color,
                            text=name, onvalue=1, offvalue=0, variable=self.flag_var, command=menu.determine_flags)
        self.check.place(x=x_pos,y=y_pos)
        self.scale = tk.Scale(self.master, label=label,length=100, from_=0, to=100, orient=tk.HORIZONTAL, fg='white', bg=bg_color,
                     variable=self.magnitude,command=menu.determine_flags)
        self.scale.place(x=x_pos+115,y=y_pos-15)
        menu.my_widgets.append(self.check)
        menu.my_widgets.append(self.scale)

class TwoOptionFlagDropdown():
    def __init__(self, master, menu, name, flag_name, options, x_pos, y_pos, label = "Shuffle %"):
        self.master = master
        self.menu = menu
        self.flag_name = flag_name
        self.options = options
        ui_font_large = font.Font(family="data/Folk.otf",size=22)
        ui_font_medium = font.Font(family="data/Folk.otf",size=16)
        ui_font_small = font.Font(family="data/Folk.otf",size=12)
        self.flag_var = tk.IntVar()
        self.mode_var = 0
        self.check = tk.Checkbutton(self.master, fg='white',bg=bg_color, font=ui_font_small, selectcolor=bg_color,
                            text=name, onvalue=1, offvalue=0, variable=self.flag_var, command=menu.determine_flags)
        self.check.place(x=x_pos,y=y_pos)
        self.mode_menu = ttk.Combobox(master,width=14)
        self.mode_menu['values'] = options
        self.mode_menu.place(x=x_pos+115,y=y_pos+5)
        self.mode_menu.current(0)
        self.mode_menu['state'] = 'readonly'
        self.mode_menu.bind("<<ComboboxSelected>>", self.value_changed)
        self.menu.my_widgets.append(self.check)
        self.menu.my_widgets.append(self.mode_menu)
        self.menu.determine_flags(0)

    def value_changed(self, event):
        if self.mode_menu.get() == self.options[0]:
            self.mode_var = 0
        if self.mode_menu.get() == self.options[1]:
            self.mode_var = 1
        if self.mode_menu.get() == self.options[2]:
            self.mode_var = 2
        if self.mode_menu.get() == self.options[3]:
            self.mode_var = 3
        self.menu.determine_flags(0)

class ThreeOptionFlag():
    def __init__(self, master, menu, name, flag_name, options, x_pos, y_pos, label = "Shuffle %"):
        self.master = master
        self.menu = menu
        self.flag_name = flag_name
        self.options = options
        ui_font_large = font.Font(family="data/Folk.otf",size=22)
        ui_font_medium = font.Font(family="data/Folk.otf",size=16)
        ui_font_small = font.Font(family="data/Folk.otf",size=12)
        self.flag_var = tk.IntVar()
        self.mode_var = 0
        self.magnitude = tk.IntVar()
        self.check = tk.Checkbutton(self.master, fg='white',bg=bg_color, font=ui_font_small, selectcolor=bg_color,
                            text=name, onvalue=1, offvalue=0, variable=self.flag_var, command=menu.determine_flags)
        self.check.place(x=x_pos,y=y_pos)
        self.scale = tk.Scale(self.master, label=label,length=100, from_=0, to=100, orient=tk.HORIZONTAL, fg='white', bg=bg_color,
                     variable=self.magnitude,command=menu.determine_flags)
        self.scale.place(x=x_pos+115,y=y_pos-15)
        self.mode_menu = ttk.Combobox(master,width=14)
        self.mode_menu['values'] = options
        self.mode_menu.place(x=x_pos+115,y=y_pos+45)
        self.mode_menu.current(0)
        self.mode_menu['state'] = 'readonly'
        self.mode_menu.bind("<<ComboboxSelected>>", self.value_changed)
        self.menu.my_widgets.append(self.check)
        self.menu.my_widgets.append(self.scale)
        self.menu.my_widgets.append(self.mode_menu)

    def value_changed(self, event):
        if self.mode_menu.get() == self.options[0]:
            self.mode_var = 0
        if self.mode_menu.get() == self.options[1]:
            self.mode_var = 1
        if self.mode_menu.get() == self.options[2]:
            self.mode_var = 2
        self.menu.determine_flags(0)

class PresetMenu():
    def __init__(self, master, custom_menu):
        self.master = master
        self.custom_menu = custom_menu
        self.my_widgets = []
        ui_font_large = font.Font(family="data/Folk.otf",size=22)
        ui_font_medium = font.Font(family="data/Folk.otf",size=16)
        ui_font_small = font.Font(family="data/Folk.otf",size=12)
        self.name_label = tk.Label(master,fg='white',bg=bg_color,text="Name",font=ui_font_medium)
        self.name_label.place(x=75,y=145)
        self.preset_name = tk.Entry(master,width=58)
        self.preset_name.place(x=140,y=150)
        self.descript_label = tk.Label(master,fg='white',bg=bg_color,text="Description",font=ui_font_medium)
        self.descript_label.place(x=25,y=180)
        self.preset_description = scrolledtext.ScrolledText(master,width=53,height=6)
        self.preset_description.place(x=140,y=180)
        self.save_button = tk.Button(master, text="Save",font=ui_font_small, width=8, command=self.save)
        self.save_button.place(x=504,y=290)
        self.my_widgets.append(self.preset_name)
        self.my_widgets.append(self.preset_description)
        self.my_widgets.append(self.preset_description.vbar)
        self.my_widgets.append(self.preset_description.frame)
        self.my_widgets.append(self.save_button)
        self.my_widgets.append(self.name_label)
        self.my_widgets.append(self.descript_label)
        
    def clear(self):
        self.custom_menu.update_flags()
        for w in self.my_widgets:
            w.destroy()

    def save(self):
        if len(self.preset_name.get()) < 1:
            return
        if len(self.preset_description.get("1.0", tk.END)) > 240: # Character Limit
            self.preset_description.delete(240, tk.END)
            
        file = open(r"data/presets.json")
        presets = json.load(file)
        file.close()
        self.custom_menu.update_flags()
        presets[self.preset_name.get()] = {"Flags":self.custom_menu.flags, "Description":self.preset_description.get("1.0",tk.END)}
        file = open(r"data/presets.json", "w")
        json.dump(presets, file, indent=3)
        self.custom_menu.update_information("Preset '" + self.preset_name.get() + "' saved successfully!")

class MiscMenu():
    def __init__(self, master, custom_menu):
        self.master = master
        self.custom_menu = custom_menu
        self.my_widgets = []
        ui_font_large = font.Font(family="data/Folk.otf",size=22)
        ui_font_medium = font.Font(family="data/Folk.otf",size=16)
        ui_font_small = font.Font(family="data/Folk.otf",size=12)
        self.flag_widgets = []
        self.flag_widgets.append(TwoOptionFlag(self.master, self, "Vanilla", "-vanilla ", 50, 130, "Chance %"))
        self.flag_widgets.append(TwoOptionFlag(self.master, self, "Balance", "-balance ", 50, 200, "Chance %"))
        self.flag_widgets.append(TwoOptionFlag(self.master, self, "Throws", "-throws ", 50, 270, "Shuffle %"))
        self.flag_widgets.append(TwoOptionFlag(self.master, self, "Chaos", "-chaos ", 50, 340, "Chaos Scale"))
        self.flag_widgets.append(OneOptionFlag(self.master, self, "Soul Bond", "-soul_bond ", 300, 130))
        self.flag_widgets.append(OneOptionFlag(self.master, self, "Vanilla Bosses", "-no_bosses ", 450, 130))
        self.flag_widgets.append(OneOptionFlag(self.master, self, "Better Low Tiers", "-better_low_tiers ", 300, 170))
        self.flag_widgets.append(OneOptionFlag(self.master, self, "SFX", "-sfx ", 450, 170))
        self.flag_widgets.append(TwoOptionFlagDropdown(self.master, self, "Turnips", "-turnips ",("Balanced", "Items Only", "Chaos", "Chaos Items"), 300, 210))
        self.flag_widgets.append(TwoOptionFlagDropdown(self.master, self, "Music", "-music ",("Shuffle"), 300, 250))
        self.flag_widgets.append(OneOptionFlag(self.master, self, "Log", "-log ", 300, 290))
        self.flag_widgets.append(TwoOptionFlag(self.master, self, "Harder 1p", "-harder_bosses ", 300, 340, "Difficulty"))
        self.determine_settings()
        
    def determine_flags(self, val = 0):
        flags = ""
        for widget in self.flag_widgets:
            if widget.flag_var.get() == 1:
                if type(widget) == TwoOptionFlag:
                    flags += widget.flag_name + str(widget.magnitude.get()) + " "
                if type(widget) == ThreeOptionFlag:
                    flags += widget.flag_name + str(widget.magnitude.get()) + "." + str(widget.mode_var) + " "
                if type(widget) == OneOptionFlag:
                    flags += widget.flag_name
                if type(widget) == TwoOptionFlagDropdown:
                    flags += widget.flag_name + str(widget.mode_var) + " "
        self.custom_menu.misc_flags = flags

    def determine_settings(self):
        flags = self.custom_menu.flags.strip() + " -"
        flag_names = ["-vanilla ", "-balance ", "-throws ", "-chaos ", "-soul_bond ",
                      "-no_bosses ", "-better_low_tiers ", "-sfx ", "-turnips ", "-music ", "-log ", "-harder_bosses "]
        for i in range(len(self.flag_widgets)):
            if flag_names[i] in flags:
                if type(self.flag_widgets[i]) == OneOptionFlag:
                    self.flag_widgets[i].flag_var.set(1)
                if type(self.flag_widgets[i]) == TwoOptionFlag:
                    self.flag_widgets[i].flag_var.set(1)
                    self.flag_widgets[i].magnitude.set(int(util.get_string_between(flags,flag_names[i], "-")))
                if type(self.flag_widgets[i]) == ThreeOptionFlag:
                    values = util.get_string_between(flags,flag_names[i], " -")
                    values = values.split(".")
                    self.flag_widgets[i].flag_var.set(1)
                    self.flag_widgets[i].mode_var = int(values[1])
                    self.flag_widgets[i].mode_menu.current(int(values[1]))
                    self.flag_widgets[i].magnitude.set(int(values[0]))
                if type(self.flag_widgets[i]) == TwoOptionFlagDropdown:
                    self.flag_widgets[i].flag_var.set(1)
                    value = util.get_string_between(flags,flag_names[i], "-")
                    self.flag_widgets[i].mode_var = int(value)
                    self.flag_widgets[i].mode_menu.current(int(value))
        self.determine_flags(0)
    def clear(self):
        self.custom_menu.update_flags()
        for w in self.my_widgets:
            w.destroy()

class AttributeMenu():
    def __init__(self, master, custom_menu):
        self.master = master
        self.custom_menu = custom_menu
        self.my_widgets = []
        ui_font_large = font.Font(family="data/Folk.otf",size=22)
        ui_font_medium = font.Font(family="data/Folk.otf",size=16)
        ui_font_small = font.Font(family="data/Folk.otf",size=12)
        self.flag_widgets = []
        self.flag_widgets.append(TwoOptionFlag(self.master, self, "Weight", "-weight ", 50, 130))
        self.flag_widgets.append(ThreeOptionFlag(self.master, self, "Scale", "-scale ", ("Normal", "Bigger", "Smaller"), 50, 220, "Magnitude"))
        self.flag_widgets.append(ThreeOptionFlag(self.master, self, "Shld. Size", "-shield_size ", ("Normal", "Bigger", "Smaller"), 50, 310, "Magnitude"))
        self.flag_widgets.append(ThreeOptionFlag(self.master, self, "Movement", "-movement ", ("Normal", "Faster", "Slower"), 320, 130, "Magnitude"))
        self.flag_widgets.append(ThreeOptionFlag(self.master, self, "Jumps", "-jump ", ("Normal", "Faster", "Slower"), 320, 220, "Magnitude"))
        self.flag_widgets.append(ThreeOptionFlag(self.master, self, "Landing", "-landing ", ("Normal", "Faster", "Slower"), 320, 310, "Magnitude"))
        self.determine_settings()
        
    def determine_flags(self, val = 0):
        flags = ""
        for widget in self.flag_widgets:
            if widget.flag_var.get() == 1:
                if type(widget) == TwoOptionFlag:
                    flags += widget.flag_name + str(widget.magnitude.get()) + " "
                if type(widget) == ThreeOptionFlag:
                    flags += widget.flag_name + str(widget.magnitude.get()) + "." + str(widget.mode_var) + " "
        self.custom_menu.attribute_flags = flags

    def determine_settings(self):
        flags = self.custom_menu.flags.strip() + " -"
        flag_names = ["-weight ", "-scale ", "-shield_size ", "-movement ", "-jump ", "-landing "]
        for i in range(len(self.flag_widgets)):
            if flag_names[i] in flags:
                if type(self.flag_widgets[i]) == TwoOptionFlag:
                    self.flag_widgets[i].flag_var.set(1)
                    self.flag_widgets[i].magnitude.set(int(util.get_string_between(flags,flag_names[i], "-")))
                if type(self.flag_widgets[i]) == ThreeOptionFlag:
                    values = util.get_string_between(flags,flag_names[i], " -")
                    values = values.split(".")
                    self.flag_widgets[i].flag_var.set(1)
                    self.flag_widgets[i].mode_var = int(values[1])
                    self.flag_widgets[i].mode_menu.current(int(values[1]))
                    self.flag_widgets[i].magnitude.set(int(values[0]))
        self.determine_flags(0)

    def clear(self):
        self.custom_menu.update_flags()
        for w in self.my_widgets:
            w.destroy()

class HitboxMenu():
    def __init__(self, master, custom_menu):
        self.master = master
        self.custom_menu = custom_menu
        self.my_widgets = []
        ui_font_large = font.Font(family="data/Folk.otf",size=22)
        ui_font_medium = font.Font(family="data/Folk.otf",size=16)
        ui_font_small = font.Font(family="data/Folk.otf",size=12)
        self.flag_widgets = []
        self.flag_widgets.append(TwoOptionFlag(self.master, self, "Damage", "-damage ", 50, 130))
        self.flag_widgets.append(TwoOptionFlag(self.master, self, "Angle", "-angle ", 50, 200))
        self.flag_widgets.append(TwoOptionFlag(self.master, self, "KB Growth", "-growth ", 50, 270))
        self.flag_widgets.append(TwoOptionFlag(self.master, self, "Base KB", "-base_knockback ", 50, 340))
        self.flag_widgets.append(TwoOptionFlag(self.master, self, "Shield Dmg.", "-shield_damage ", 320, 130))
        self.flag_widgets.append(TwoOptionFlag(self.master, self, "Set KB", "-wdsk ", 320, 200, "Random %"))
        self.flag_widgets.append(TwoOptionFlag(self.master, self, "Size", "-hitbox_size ", 320, 270, "Shuffle %"))
        self.flag_widgets.append(TwoOptionFlag(self.master, self, "Element", "-element ", 320, 340, "Random %"))
        self.determine_settings()

    def determine_flags(self, val = 0):
        flags = ""
        for widget in self.flag_widgets:
            if widget.flag_var.get() == 1:
                if type(widget) == TwoOptionFlag:
                    flags += widget.flag_name + str(widget.magnitude.get()) + " "
        self.custom_menu.hitbox_flags = flags

    def determine_settings(self):
        flags = self.custom_menu.flags.strip() + " -"
        flag_names = ["-damage ", "-angle ", "-growth ", "-base_knockback ", "shield_damage ",
                      "-wdsk ", "hitbox_size ", "-element "]
        for i in range(len(self.flag_widgets)):
            if flag_names[i] in flags:
                self.flag_widgets[i].flag_var.set(1)
                self.flag_widgets[i].magnitude.set(int(util.get_string_between(flags,flag_names[i], "-")))
        self.determine_flags(0)
            
    def clear(self):
        self.custom_menu.update_flags()
        for w in self.my_widgets:
            w.destroy()
        
def start():
    root = tk.Tk()
    root.geometry("600x450")
    root.resizable(False,False)
    root.title("SSBM Randomizer")
    root.iconbitmap("data/logo.ico")
    root["bg"]=bg_color
    #root.wm_attributes("-transparentcolor",bg_color)
            
    app = ApplicationMain(root)
    root.mainloop()
    
if __name__ == "__main__":
    start()
