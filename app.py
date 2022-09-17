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
        self.seed_creator.bind('<Enter>', self.show_seed_tip)
        # Preset Chooser
        #tk.Label(master,fg='white',bg=bg_color,text="Preset",font=ui_font_medium).place(x=35,y=141)
        self.presets_menu = ttk.Combobox(master,value=self.preset_keys,width=55)
        self.presets_menu.place(x=130,y=147)
        self.presets_menu.current(0)
        self.presets_menu['state'] = 'readonly'
        self.presets_menu.bind("<<ComboboxSelected>>", self.update_preset_text)
        self.presets_menu.bind("<Enter>", self.show_preset_tip)
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
        self.flag_text_box.bind("<Enter>", self.show_seed_tip)
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
        new_flags = randomizer.start(iso_path, output_path, flags)
        self.randomizing = False
        self.update_information("ISO generated! Path: " + self.output_path.get())
        self.randomize_btn['state'] = 'normal'
        self.flag_text_box.delete("1.0", tk.END)
        self.flag_text_box.insert(tk.INSERT, new_flags)
        self.update_seed()

    def generate_iso(self):
        if self.randomizing: return
        if len(self.seed_creator.get()) > 1:
            flags = "-seed " + self.seed_creator.get() + " " + self.flag_text_box.get("1.0",tk.END)
        else:
            flags = self.flag_text_box.get("1.0",tk.END)
        flags = flags.strip()
        args = [self.iso_path.get(),self.output_path.get(),flags]
        # Check for Errors
        for arg in args:
            if len(arg) <= 0:
                print("Error: Invalid argument: " + arg)
        if len(args[0]) < 1:
            self.update_information("Error: No ISO Path chosen. Please select a v1.02 Melee ISO!")
            return
        if ".iso" not in args[0]:
            self.update_information("Error: Chosen path is not an .iso")
            return
        if len(args[1]) < 1:
            self.update_information("Error: No Output Path chosen. This is where the ISO will be saved.")
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

    def show_seed_tip(self, event):
        if self.randomizing: return
        self.information.set("ISOs generated with the same seed and flags will be identical.")

    def show_preset_tip(self, event):
        if self.randomizing: return
        self.information.set("Presets are a collection of flags to start with. Click 'Customize' to make changes!")

class Tab():
    def __init__(self, master, c_menu, menu, x_pos, y_pos, text = "", default=False):
        self.master = master
        self.menu = menu
        self.c_menu = c_menu
        self.c_menu.tabs.append(self)
        self.tooltip = ""
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
        if len(self.tooltip) > 0:
            self.c_menu.update_information(self.tooltip)

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
        if "-seed " in self.flags: 
            self.seed = util.get_string_between(self.flags, "-seed ", " -")
        else:
            self.seed = ""
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
        hitbox_tab = Tab(self.master,self,HitboxMenu,50,60,"Hitboxes",True)
        hitbox_tab.tooltip = "Hitboxes control the effects of attacks when they land."
        attribute_tab = Tab(self.master,self,AttributeMenu,180,60,"Attributes")
        attribute_tab.tooltip = "Attributes will change how a character moves, and more!"
        misc_tab = Tab(self.master,self,MiscMenu,310,60,"Misc.")
        misc_tab.tooltip = "Other miscellaneous flags can be enabled here!"
        preset_tab = Tab(self.master,self,PresetMenu,440,60,"Preset")
        preset_tab.tooltip = "Like your flagset? Save it for future use!"

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
        if len(string) == 0:
            return
        self.information.set(string)

class OneOptionFlag():
    def __init__(self, master, menu, name, flag_name, x_pos, y_pos):
        self.master = master
        self.menu = menu
        self.flag_name = flag_name
        self.tooltip = ""
        ui_font_large = font.Font(family="data/Folk.otf",size=22)
        ui_font_medium = font.Font(family="data/Folk.otf",size=16)
        ui_font_small = font.Font(family="data/Folk.otf",size=12)
        self.flag_var = tk.IntVar()
        self.check = tk.Checkbutton(self.master, fg='white',bg=bg_color, font=ui_font_small, selectcolor=bg_color,
                            text=name, onvalue=1, offvalue=0, variable=self.flag_var, command=menu.determine_flags)
        self.check.place(x=x_pos,y=y_pos)
        self.check.bind('<Enter>', self.update_information)
        self.check.focus_set()
        menu.my_widgets.append(self.check)
        
    def update_information(self, event):
        self.menu.custom_menu.update_information(self.tooltip)
        
class TwoOptionFlag():
    def __init__(self, master, menu, name, flag_name, x_pos, y_pos, mag_cap = 100, label = "Magnitude"):
        self.master = master
        self.menu = menu
        self.flag_name = flag_name
        self.tooltip = ""
        ui_font_large = font.Font(family="data/Folk.otf",size=22)
        ui_font_medium = font.Font(family="data/Folk.otf",size=16)
        ui_font_small = font.Font(family="data/Folk.otf",size=12)
        self.flag_var = tk.IntVar()
        self.flag_var.trace("w", self.update_state)
        self.magnitude = tk.IntVar()
        self.check = tk.Checkbutton(self.master, fg='white',bg=bg_color, font=ui_font_small, selectcolor=bg_color,
                            text=name, onvalue=1, offvalue=0, variable=self.flag_var, command=menu.determine_flags)
        self.check.place(x=x_pos,y=y_pos)
        self.check.bind('<Enter>', self.update_information)
        self.scale = tk.Scale(self.master, label=label,length=100, from_=0, to=mag_cap, orient=tk.HORIZONTAL, fg='white', bg=bg_color,
                     variable=self.magnitude,command=menu.determine_flags)
        self.scale.place(x=x_pos+115,y=y_pos-15)
        self.scale.bind('<Enter>', self.update_information)
        menu.my_widgets.append(self.check)
        menu.my_widgets.append(self.scale)
        self.update_state()
        
    def update_information(self, event):
        self.menu.custom_menu.update_information(self.tooltip)
        
    def update_state(self, *args):
        if self.flag_var.get() == 0:
            self.scale['state'] = 'disabled'
            self.scale.configure(fg='gray', bg='black')
            return
        self.scale['state'] = 'normal'
        self.scale.configure(fg='white', bg=bg_color)
        
class TwoOptionFlagDropdown():
    def __init__(self, master, menu, name, flag_name, options, x_pos, y_pos):
        self.master = master
        self.menu = menu
        self.flag_name = flag_name
        self.options = options
        self.tooltip = ""
        ui_font_large = font.Font(family="data/Folk.otf",size=22)
        ui_font_medium = font.Font(family="data/Folk.otf",size=16)
        ui_font_small = font.Font(family="data/Folk.otf",size=12)
        self.flag_var = tk.IntVar()
        self.flag_var.trace("w", self.update_state)
        self.mode_var = 0
        self.check = tk.Checkbutton(self.master, fg='white',bg=bg_color, font=ui_font_small, selectcolor=bg_color,
                            text=name, onvalue=1, offvalue=0, variable=self.flag_var, command=menu.determine_flags)
        self.check.place(x=x_pos,y=y_pos)
        self.check.bind('<Enter>', self.update_information)
        self.mode_menu = ttk.Combobox(master,width=14)
        self.mode_menu['values'] = options
        self.mode_menu.place(x=x_pos+115,y=y_pos+5)
        self.mode_menu.current(0)
        self.mode_menu['state'] = 'readonly'
        self.mode_menu.bind("<<ComboboxSelected>>", self.value_changed)
        self.mode_menu.bind('<Enter>', self.update_information)
        self.menu.my_widgets.append(self.check)
        self.menu.my_widgets.append(self.mode_menu)
        self.menu.determine_flags(0)
        self.update_state()

    def update_information(self, event):
        self.menu.custom_menu.update_information(self.tooltip)

    def update_state(self, *args):
        if self.flag_var.get() == 0:
            self.mode_menu['state'] = 'disabled'
            return
        self.mode_menu['state'] = 'readonly'

    def value_changed(self, event):
        if self.mode_menu.get() == self.options[0]:
            self.mode_var = 0
        if self.mode_menu.get() == self.options[1]:
            self.mode_var = 1
        if self.mode_menu.get() == self.options[2]:
            self.mode_var = 2
        if len(self.options) > 3:
            if self.mode_menu.get() == self.options[3]:
                self.mode_var = 3
        self.menu.determine_flags(0)

class ThreeOptionFlag():
    def __init__(self, master, menu, name, flag_name, options, x_pos, y_pos, mag_cap = 100, label = "Magnitude"):
        self.master = master
        self.menu = menu
        self.flag_name = flag_name
        self.options = options
        self.tooltip = ""
        ui_font_large = font.Font(family="data/Folk.otf",size=22)
        ui_font_medium = font.Font(family="data/Folk.otf",size=16)
        ui_font_small = font.Font(family="data/Folk.otf",size=12)
        self.flag_var = tk.IntVar()
        self.flag_var.trace("w", self.update_state)
        self.mode_var = 0
        self.magnitude = tk.IntVar()
        self.check = tk.Checkbutton(self.master, fg='white',bg=bg_color, font=ui_font_small, selectcolor=bg_color,
                            text=name, onvalue=1, offvalue=0, variable=self.flag_var, command=menu.determine_flags)
        self.check.place(x=x_pos,y=y_pos)
        self.check.bind('<Enter>', self.update_information)
        self.scale = tk.Scale(self.master, label=label,length=100, from_=0, to=mag_cap, orient=tk.HORIZONTAL, fg='white', bg=bg_color,
                     variable=self.magnitude,command=menu.determine_flags)
        self.scale.place(x=x_pos+115,y=y_pos-15)
        self.scale.bind('<Enter>', self.update_information)
        self.mode_menu = ttk.Combobox(master,width=14)
        self.mode_menu['values'] = options
        self.mode_menu.place(x=x_pos+115,y=y_pos+45)
        self.mode_menu.current(0)
        self.mode_menu.bind("<<ComboboxSelected>>", self.value_changed)
        self.mode_menu.bind('<Enter>', self.update_information)
        self.menu.my_widgets.append(self.check)
        self.menu.my_widgets.append(self.scale)
        self.menu.my_widgets.append(self.mode_menu)
        self.update_state()

    def update_information(self, event):
        self.menu.custom_menu.update_information(self.tooltip)

    def update_state(self, *args):
        if self.flag_var.get() == 0:
            self.scale['state'] = 'disabled'
            self.scale.configure(fg='gray', bg='black')
            self.mode_menu['state'] = 'disabled'
            return
        self.scale['state'] = 'normal'
        self.scale.configure(fg='white', bg=bg_color)
        self.mode_menu['state'] = 'readonly'

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
        self.name_label = tk.Label(master,fg='white',bg=bg_color,text="Name",font=ui_font_medium,width=9)
        self.name_label.place(x=45,y=145)
        self.preset_name = tk.Entry(master,width=59)
        self.preset_name.place(x=180,y=150)
        self.descript_label = tk.Label(master,fg='white',bg=bg_color,text="Description",font=ui_font_medium,width=9)
        self.descript_label.place(x=45,y=190)
        self.preset_description = scrolledtext.ScrolledText(master,width=42,height=6)
        self.preset_description.place(x=180,y=194)
        self.save_button = tk.Button(master, text="Save",font=ui_font_small, width=8, command=self.save)
        self.save_button.place(x=457,y=312)
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
        self.flag_widgets.append(OneOptionFlag(self.master, self, "Balance", "-balance ", 300, 270))
        self.flag_widgets.append(TwoOptionFlag(self.master, self, "Throws", "-throws ", 50, 200, 20))
        self.flag_widgets.append(TwoOptionFlag(self.master, self, "Chaos", "-chaos ", 50, 270, 100, "Chaos Scale"))
        self.flag_widgets.append(TwoOptionFlag(self.master, self, "Shuffle", "-shuffle ", 50, 130, 100, "% Chance"))
        self.flag_widgets.append(OneOptionFlag(self.master, self, "Soul Bond", "-soul_bond ", 300, 190))
        self.flag_widgets.append(OneOptionFlag(self.master, self, "Better Low Tiers", "-better_low_tiers ", 300, 230))
        self.flag_widgets.append(OneOptionFlag(self.master, self, "SFX", "-sfx ", 450, 230))
        self.flag_widgets.append(TwoOptionFlagDropdown(self.master, self, "Turnips", "-turnips ",("Balanced", "Items Only", "Chaos", "Chaos Items"), 300, 310))
        self.flag_widgets.append(TwoOptionFlagDropdown(self.master, self, "Music", "-music ",("Shuffle"), 300, 350))
        self.flag_widgets.append(OneOptionFlag(self.master, self, "Log", "-log ", 520, 230))
        self.flag_widgets.append(TwoOptionFlag(self.master, self, "Harder 1p", "-harder_bosses ", 50, 340, 5, "Difficulty"))
        self.flag_widgets.append(OneOptionFlag(self.master, self, "Fox Only", "-all_fox ", 400, 270))
        self.flag_widgets.append(OneOptionFlag(self.master, self, "Elemental Mastery", "-elemental_mastery ", 420, 190))
        self.flag_widgets.append(OneOptionFlag(self.master, self, "All Characters Float", "-all_float ", 300, 120))
        self.flag_widgets[0].tooltip = "Makes attacks closer to their original power level."
        self.flag_widgets[1].tooltip = "Throws will have their properties randomized."
        self.flag_widgets[2].tooltip = "Gives each hitbox special quirks."
        self.flag_widgets[3].tooltip = "A percentage of attacks/throws will be shuffled instead of randomized."
        self.flag_widgets[4].tooltip = "Makes Nana the same as Popo."
        self.flag_widgets[5].tooltip = "Low tier characters will receive substantial buffs."
        self.flag_widgets[6].tooltip = "Hitbox sounds will be randomized."
        self.flag_widgets[7].tooltip = "Turnips will be randomized. Chaos may be buggy!"
        self.flag_widgets[8].tooltip = "Shuffles music. Will increase randomization time drastically."
        self.flag_widgets[9].tooltip = "A log will be generated that lists changes."
        self.flag_widgets[10].tooltip = "Bosses will receive substantial buffs."
        self.flag_widgets[11].tooltip = "All characters will have the movement of Fox."
        self.flag_widgets[12].tooltip = "Moves with certain elements will get special bonuses."
        self.flag_widgets[13].tooltip = "Gives all characters the ability to float like Peach! Credit: Uncle Punch"
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
        flag_names = ["-balance ", "-throws ", "-chaos ", "-shuffle ", "-soul_bond ",
                      "-better_low_tiers ", "-sfx ", "-turnips ", "-music ", "-log ", "-harder_bosses ",
                      "-all-fox ", "-elemental_mastery ", "-all_float "]
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
        self.flag_widgets.append(ThreeOptionFlag(self.master, self, "Weight", "-weight ", ("Normal", "Heavier", "Lighter"), 50, 130, 20))
        self.flag_widgets.append(ThreeOptionFlag(self.master, self, "Scale", "-scale ", ("Normal", "Bigger", "Smaller"), 50, 220, 50))
        self.flag_widgets.append(ThreeOptionFlag(self.master, self, "Shld. Size", "-shield_size ", ("Normal", "Bigger", "Smaller"), 50, 310, 10))
        self.flag_widgets.append(ThreeOptionFlag(self.master, self, "Movement", "-movement ", ("Normal", "Faster", "Slower"), 320, 130, 20))
        self.flag_widgets.append(ThreeOptionFlag(self.master, self, "Jumps", "-jump ", ("Normal", "Faster", "Slower"), 320, 220, 20))
        self.flag_widgets.append(ThreeOptionFlag(self.master, self, "Landing", "-landing ", ("Normal", "Faster", "Slower"), 320, 310, 20))
        self.flag_widgets[0].tooltip = "Higher weight will lower knockback."
        self.flag_widgets[1].tooltip = "How big a fighter is."
        self.flag_widgets[2].tooltip = "Changes the size of fighters' shields."
        self.flag_widgets[3].tooltip = "Changes speed on the ground and in the air."
        self.flag_widgets[4].tooltip = "Changes jumpsquat and jump properties."
        self.flag_widgets[5].tooltip = "Affects landing lag on aerials and base landing lag."
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
        self.flag_widgets.append(TwoOptionFlag(self.master, self, "Damage", "-damage ", 50, 200, 20))
        self.flag_widgets.append(TwoOptionFlagDropdown(self.master, self, "Angle", "-angle ",("Normal", "Deviation", "All Meteor"), 50, 130))
        self.flag_widgets.append(TwoOptionFlag(self.master, self, "KB Growth", "-growth ", 50, 270, 20))
        self.flag_widgets.append(TwoOptionFlag(self.master, self, "Base KB", "-base_knockback ", 50, 340, 20))
        self.flag_widgets.append(TwoOptionFlag(self.master, self, "Shield Dmg.", "-shield_damage ", 320, 130, 20))
        self.flag_widgets.append(TwoOptionFlag(self.master, self, "Set KB", "-wdsk ", 320, 200, 20))
        self.flag_widgets.append(TwoOptionFlag(self.master, self, "Size", "-hitbox_size ", 320, 270, 20))
        self.flag_widgets.append(TwoOptionFlag(self.master, self, "Element", "-element ", 320, 340, 100, "Random %"))
        self.flag_widgets[0].tooltip = "Changes how much damage that an attack will do."
        self.flag_widgets[1].tooltip = "Changes the angle that attacks will launch at."
        self.flag_widgets[2].tooltip = "Changes how much percent affects knockback."
        self.flag_widgets[3].tooltip = "Changes how much knockback an attack has."
        self.flag_widgets[4].tooltip = "Changes how much damage an attack does to shields."
        self.flag_widgets[5].tooltip = "Makes moves send at a fixed amount of knockback."
        self.flag_widgets[6].tooltip = "Changes hitbox sizes, making them more/less likely to land."
        self.flag_widgets[7].tooltip = "Can add Fire, Ice, Ground, Disable, etc..."
        self.determine_settings()

    def determine_flags(self, val = 0):
        flags = ""
        for widget in self.flag_widgets:
            if widget.flag_var.get() == 1:
                if type(widget) == TwoOptionFlag:
                    flags += widget.flag_name + str(widget.magnitude.get()) + " "
                elif type(widget) == TwoOptionFlagDropdown:
                    flags += widget.flag_name + str(widget.mode_var) + " "
                else:
                    flags += widget.flag_name + " "
        self.custom_menu.hitbox_flags = flags

    def determine_settings(self):
        flags = self.custom_menu.flags.strip() + " -"
        flag_names = ["-damage ", "-angle ", "-growth ", "-base_knockback ", "shield_damage ",
                      "-wdsk ", "hitbox_size ", "-element "]
        for i in range(len(self.flag_widgets)):
            if flag_names[i] in flags:
                self.flag_widgets[i].flag_var.set(1)
                if type(self.flag_widgets[i]) == TwoOptionFlag:
                    self.flag_widgets[i].magnitude.set(int(util.get_string_between(flags,flag_names[i], "-")))
                if type(self.flag_widgets[i]) == TwoOptionFlagDropdown:
                    self.flag_widgets[i].flag_var.set(1)
                    value = util.get_string_between(flags,flag_names[i], "-")
                    try:
                        self.flag_widgets[i].mode_var = int(value)
                        self.flag_widgets[i].mode_menu.current(int(value))
                    except:
                        self.flag_widgets[i].mode_var = 0
                        self.flag_widgets[i].mode_menu.current(0)
                    
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
