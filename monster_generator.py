import random
import math
import tkinter as tk

# This program uses ttkbootstrap from: https://ttkbootstrap.readthedocs.io/en/latest/
# run the program below in terminal to install
# python -m pip install ttkbootstrap
import ttkbootstrap as ttk

stat_list = ["CR","Prof. Bonus","Armor Class","Hit Points","Attack Bonus","Damage/Round","Save DC"]

def main():
    print_banner()
    root, frm_main = init_tk()
    cr_dict = read_cr_table(filename="cr_table.csv")
    window_objects = populate_main_window(frm_main, cr_dict)

    root.mainloop()

def print_banner():
    print("""
  _____         _____  
 |  __ \\  ___  |  __ \\   
 | |  | |( _ ) | |  | | \033[1m Monster Stat Block Generator\033[0m
 | |  | |/ _ \\/\\ |  | |
 | |__| | (_>  < |__| |
 |_____/ \\___/\\/_____/                 -By Matt Talbert\n""")

def init_tk():
    root = tk.Tk()
    frm_main = ttk.Frame(root)
    root.iconbitmap('d20.ico')
    style = ttk.Style("cyborg")
    frm_main.master.title("Monster Stat Block Generator")
    frm_main.pack(padx=3, pady=3, fill=tk.BOTH, expand=1)
    # window_objects = populate_main_window(frm_main, root)
    return root, frm_main

def populate_main_window(frm_main, cr_dict):
    upper_frame = ttk.Frame(frm_main)
    lower_frame = ttk.Frame(frm_main)
    upper_frame.pack(side=tk.TOP)
    lower_frame.pack(side=tk.TOP)

    flavor_lblfr = ttk.LabelFrame(upper_frame, text="Identity")
    name_lbl = ttk.Label(flavor_lblfr, text="Name")
    name_ent = ttk.Entry(flavor_lblfr)
    type_lbl = ttk.Label(flavor_lblfr, text="Type")
    type_ent = ttk.Entry(flavor_lblfr)
    senses_lbl = ttk.Label(flavor_lblfr, text="Senses")
    senses_ent = ttk.Entry(flavor_lblfr)
    languages_lbl = ttk.Label(flavor_lblfr, text="Languages")
    languages_ent = ttk.Entry(flavor_lblfr)

    visible_lblfr = ttk.ttk.LabelFrame(upper_frame, text="Stats")
    cr_lbl = ttk.Label(visible_lblfr, text="CR: ENTER")
    cr_ent = ttk.Entry(visible_lblfr)
    ac_lbl = ttk.Label(visible_lblfr, text="AC")
    ac_ent = ttk.Entry(visible_lblfr)
    hp_lbl = ttk.Label(visible_lblfr, text="HP")
    hp_ent = ttk.Entry(visible_lblfr)
    speed_lbl = ttk.Label(visible_lblfr, text="Speed")
    speed_ent = ttk.Entry(visible_lblfr)

    combat_lblfr = ttk.LabelFrame(upper_frame, text="Combat")
    attack_bonus_lbl = ttk.Label(combat_lblfr, text="Attack Bonus")
    attack_bonus_ent = ttk.Entry(combat_lblfr)
    dmg_per_round_lbl = ttk.Label(combat_lblfr, text="Damage per Round")
    dmg_per_round_ent = ttk.Entry(combat_lblfr)
    save_dc_lbl = ttk.Label(combat_lblfr, text="Save DC")
    save_dc_ent = ttk.Entry(combat_lblfr)
    prof_bonus_lbl = ttk.Label(combat_lblfr, text="Proficiency Bonus")
    prof_bonus_ent = ttk.Entry(combat_lblfr)
    

    calc_cr_btn = ttk.Button(lower_frame, text="Calculate CR", style="dark", padding=12)
    export_txt = ttk.Button(lower_frame, text="Export txt", style="dark", padding=12)

    ability_lblfr = ttk.LabelFrame(lower_frame, text="Ability Scores")
    str_lbl = ttk.Label(ability_lblfr, text="STR")
    str_ent = ttk.Entry(ability_lblfr, width=4)
    dex_lbl = ttk.Label(ability_lblfr, text="DEX")
    dex_ent = ttk.Entry(ability_lblfr, width=4)
    con_lbl = ttk.Label(ability_lblfr, text="CON")
    con_ent = ttk.Entry(ability_lblfr, width=4)
    int_lbl = ttk.Label(ability_lblfr, text="INT")
    int_ent = ttk.Entry(ability_lblfr, width=4)
    wis_lbl = ttk.Label(ability_lblfr, text="WIS")
    wis_ent = ttk.Entry(ability_lblfr, width=4)
    cha_lbl = ttk.Label(ability_lblfr, text="CHA")
    cha_ent = ttk.Entry(ability_lblfr, width=4)

    err_msg = ttk.Label(frm_main)

    # ---- GRID PLACEMENT ----
    #Upper frame with flavor, visible and combat stats
    flavor_lblfr.grid(row=0, column=0, padx=6, pady=6)
    name_lbl.grid(row=0, column=0, padx=3, pady=3)
    name_ent.grid(row=0, column=1, padx=3, pady=3)
    type_lbl.grid(row=1, column=0, padx=3, pady=3)
    type_ent.grid(row=1, column=1, padx=3, pady=3)
    senses_lbl.grid(row=2, column=0, padx=3, pady=3)
    senses_ent.grid(row=2, column=1, padx=3, pady=3)
    languages_lbl.grid(row=3, column=0, padx=3, pady=3)
    languages_ent.grid(row=3, column=1, padx=3, pady=3)

    visible_lblfr.grid(row=0, column=1, padx=6, pady=6)
    cr_lbl.grid(row=0, column=0, padx=3, pady=3)
    cr_ent.grid(row=0, column=1, padx=3, pady=3)
    ac_lbl.grid(row=1, column=0, padx=3, pady=3)
    ac_ent.grid(row=1, column=1, padx=3, pady=3)
    hp_lbl.grid(row=2, column=0, padx=3, pady=3)
    hp_ent.grid(row=2, column=1, padx=3, pady=3)
    speed_lbl.grid(row=3, column=0, padx=3, pady=3)
    speed_ent.grid(row=3, column=1, padx=3, pady=3)

    combat_lblfr.grid(row=0, column=2, padx=6, pady=6)
    attack_bonus_lbl.grid(row=0, column=0, padx=3, pady=3)
    attack_bonus_ent.grid(row=0, column=1, padx=3, pady=3)
    dmg_per_round_lbl.grid(row=1, column=0, padx=3, pady=3)
    dmg_per_round_ent.grid(row=1, column=1, padx=3, pady=3)
    save_dc_lbl.grid(row=2, column=0, padx=3, pady=3)
    save_dc_ent.grid(row=2, column=1, padx=3, pady=3)
    prof_bonus_lbl.grid(row=3, column=0, padx=3, pady=3)
    prof_bonus_ent.grid(row=3, column=1, padx=3, pady=3)

    #Lower Frame with abilties and export buttons

    attribute_gap = 9
    ability_lblfr.pack(side=tk.LEFT, padx=(6,6), pady=6)
    str_lbl.grid(row=0, column=0, padx=3, pady=3)
    str_ent.grid(row=0, column=1, padx=(3, attribute_gap), pady=3)
    dex_lbl.grid(row=0, column=2, padx=3, pady=3)
    dex_ent.grid(row=0, column=3, padx=(3, attribute_gap), pady=3)
    con_lbl.grid(row=0, column=4, padx=3, pady=3)
    con_ent.grid(row=0, column=5, padx=(3, attribute_gap), pady=3)
    int_lbl.grid(row=0, column=6, padx=3, pady=3)
    int_ent.grid(row=0, column=7, padx=(3, attribute_gap), pady=3)
    wis_lbl.grid(row=0, column=8, padx=3, pady=3)
    wis_ent.grid(row=0, column=9, padx=(3, attribute_gap), pady=3)
    cha_lbl.grid(row=0, column=10, padx=3, pady=3)
    cha_ent.grid(row=0, column=11, padx=3, pady=3)

    export_txt.pack(side=ttk.RIGHT, padx=4, pady=(9, 0))
    calc_cr_btn.pack(side=ttk.RIGHT, padx=4, pady=(9, 0))


    window_objects = {"name" : name_ent, "type" : type_ent, "senses" : senses_ent, "languages" : languages_ent, "cr" : cr_ent,
                        "ac" : ac_ent, "hp" : hp_ent, "speed" : speed_ent, "attack_bonus" : attack_bonus_ent, 
                        "damage_per_round" : dmg_per_round_ent, "save_dc" : save_dc_ent,"prof_bonus" : prof_bonus_ent,"str" :
                        str_ent, "dex" : dex_ent, "con" : con_ent, "int" : int_ent, "wis" : wis_ent, "cha" : cha_ent, "calc_cr_btn" :
                        calc_cr_btn, "export_txt" : export_txt, "cr_label" : cr_lbl, "error_message" : err_msg}
    
    cr_ent.bind('<Return>', lambda event, entry1=window_objects, entry2=cr_dict: write_cr(entry1, entry2))
    calc_cr_btn.config(command= lambda entry1=window_objects, entry2=cr_dict: calculate_cr(entry1, entry2))
    export_txt.config(command= lambda entry1=window_objects: print_to_txt(entry1))

    return window_objects


def read_cr_table(filename):
    try:
        cr_dict = {}
        with open(filename) as cr_table:
            next(cr_table)
            for line in cr_table:
                line = line.strip().split(",")
                for i in range(len(line)):
                    if "+" in line[i]:
                        line[i] = line[i].strip("+")
                    if "-" in line[i]:
                        line[i] = line[i].split("-")
                    if "/" in line[i]:
                        line[i] = line[i].replace("/", "_")
                cr_dict[line[0]] = list(line[1:7])

    except FileNotFoundError as not_found_err:
        print(f"{type(not_found_err).__name__}: {not_found_err}")
        print("Error: missing file")
        print(not_found_err)
        raise FileNotFoundError

    except KeyError as value_err:
        print(f"{type(value_err).__name__}: {value_err}")
        print("Incorrect dictionary key value")

    except IndexError as index_err:
        print(f"{type(index_err).__name__}: {index_err}")
        print("Incorrect list index value")


    
    return cr_dict

def write_cr(window_objects, cr_dict):
    cr_input = window_objects["cr"].get()
    cr_input = cr_input.replace("/", "_")
    try:
        global stat_list
        stat_list = cr_dict[cr_input]
        write_stats_to_entries(window_objects, cr_input)
        window_objects["error_message"].pack_forget()
    except KeyError as value_err:
        print(f"{type(value_err).__name__}: {value_err}")
        print("Incorrect dictionary key value")
        window_objects["error_message"].configure(text=f"Sorry but {value_err} is not a valid CR. Please try again!")
        window_objects["error_message"].pack(side=tk.TOP)

def write_stats_to_entries(window_objects, cr_input):
    try:
        selected_cr_stats = stat_list
        window_objects["cr_label"].config(text=f"CR: {cr_input}")
        # window_objects["cr"].config(text=f"{cr_input}")
        window_objects["cr"].delete(0, tk.END)
        window_objects["cr"].insert(tk.END, cr_input)
        window_objects["prof_bonus"].delete(0, tk.END)
        window_objects["prof_bonus"].insert(tk.END, f"+{selected_cr_stats[0]}")
        window_objects["ac"].delete(0, tk.END)
        window_objects["ac"].insert(tk.END, selected_cr_stats[1])
        window_objects["hp"].delete(0, tk.END)

        if type(selected_cr_stats[2]) is list:
            random_hp = random.randint(int(selected_cr_stats[2][0]), int(selected_cr_stats[2][1]))
            window_objects["hp"].insert(tk.END, random_hp)
        else:
            window_objects["hp"].insert(tk.END, selected_cr_stats[2])


        window_objects["attack_bonus"].delete(0, tk.END)
        window_objects["attack_bonus"].insert(tk.END, selected_cr_stats[3])
        window_objects["damage_per_round"].delete(0, tk.END)

        if type(selected_cr_stats[4]) is list:
            random_dmg = random.randint(int(selected_cr_stats[4][0]), int(selected_cr_stats[4][1]))
            window_objects["damage_per_round"].insert(tk.END, random_dmg)
        else:
            window_objects["damage_per_round"].insert(tk.END, selected_cr_stats[4])

        window_objects["save_dc"].delete(0, tk.END)
        window_objects["save_dc"].insert(tk.END, selected_cr_stats[5])
        window_objects["error_message"].pack_forget()
    except KeyError as value_err:
        print(f"{type(value_err).__name__}: {value_err}")
        print("Incorrect dictionary key value")
        window_objects["error_message"].configure(text=f"Sorry but {value_err} is not a valid CR. Please try again!")
        window_objects["error_message"].pack(side=tk.TOP)

def write_stats_to_memory(window_objects):
    global stat_list
    cr = window_objects["cr"].get()
    prof_bonus = window_objects["prof_bonus"].get().strip("+")
    ac = window_objects["ac"].get()
    hp = window_objects["hp"].get()
    attack_bonus = window_objects["attack_bonus"].get().strip("+")
    damage_per_round = window_objects["damage_per_round"].get()
    save_dc = window_objects["save_dc"].get()

    name = window_objects["name"].get() 
    type = window_objects["type"].get() 
    senses = window_objects["senses"].get() 
    languages = window_objects["languages"].get() 
    speed = window_objects["speed"].get() 
    str = window_objects["str"].get() 
    dex = window_objects["dex"].get() 
    con = window_objects["con"].get()
    int = window_objects["int"].get() 
    wis = window_objects["wis"].get() 
    cha = window_objects["cha"].get() 

    stat_list = [prof_bonus, ac, hp, attack_bonus, damage_per_round, save_dc, speed, name, type, senses, languages, [str, dex, con, int, wis, cha], cr]

def find_cr_level(cr_dict, index, statistic):
    try:
        correct_key_max = "null"
        correct_key_min = "null"
        for cr_key in cr_dict:
            cr_level = cr_dict[cr_key]
            if type(cr_level[index]) is list:
                if statistic in range(int(cr_level[index][0]), int(cr_level[index][1]) + 1):
                    correct_key_max = cr_key
                    if correct_key_min == "null":
                        correct_key_min = cr_key
            else:
                if statistic == int(cr_level[index]):
                    correct_key_max = cr_key
                    if correct_key_min == "null":
                        correct_key_min = cr_key
        return correct_key_max, correct_key_min
    except IndexError as value_err:
        print(f"{type(value_err).__name__}: {value_err}")
        print("Incorrect dictionary key value")
        raise IndexError

def calculate_cr(window_objects, cr_dict):
    #CR includes 0, 1/2 1/8 and more odd numbers. This will put them in a list to assign ordered integer values instead
    try:
        global stat_list
        cr_progression = []
        for cr_key in cr_dict:
            cr_progression.append(cr_key)
        write_stats_to_memory(window_objects)
        ac = int(stat_list[1])
        hp = int(stat_list[2])
        attack_bonus = int(stat_list[3])
        damage_per_round = int(stat_list[4])

        #start with CR from hit points
        cr_from_hp = cr_progression.index(find_cr_level(cr_dict, 2, hp)[0])

        #adjust CR up or down 1 for each difference of 2 to AC
        def_cr_dif = ac - int(cr_dict[cr_progression[cr_from_hp]][1])
        if def_cr_dif <= 0:
            defensive_cr = cr_from_hp + math.ceil(def_cr_dif / 2)
        else:
            defensive_cr = cr_from_hp + math.floor(def_cr_dif / 2)

        #Find the CR from damage output per round
        cr_from_dmg = cr_progression.index(find_cr_level(cr_dict, 4, damage_per_round)[0])

        #adjust CR up or down 1 for each difference of 2 in attack bonus
        off_cr_dif = attack_bonus - int(cr_dict[cr_progression[cr_from_dmg]][3])
        if off_cr_dif <= 0:
            offensive_cr = cr_from_dmg + math.ceil(off_cr_dif / 2)
        else:
            offensive_cr = cr_from_dmg + math.floor(off_cr_dif / 2)

        calculated_cr = round((defensive_cr + offensive_cr) / 2)

        calculated_cr = cr_progression[calculated_cr]
        cr = calculated_cr
        prof_bonus = cr_dict[calculated_cr][0]
        save_dc = cr_dict[calculated_cr][5]

        window_objects["error_message"].pack_forget()
        stat_list[:5] = [prof_bonus, ac, hp, attack_bonus, damage_per_round, save_dc]
        # stat_list[0:6] = [cr, prof_bonus, ac, hp, attack_bonus, damage_per_round, save_dc]
        write_stats_to_entries(window_objects, cr_input=cr)

        window_objects["error_message"].pack_forget()
    except KeyError as value_err:
        print(f"{type(value_err).__name__}: {value_err}")
        print("Incorrect dictionary key value")
        window_objects["error_message"].configure(text=f"Sorry but {value_err} isn't a valid input. Please try again!")
        window_objects["error_message"].pack(side=tk.TOP)
    except ValueError as value_err:
        print(f"{type(value_err).__name__}: {value_err}")
        print("Incorrect dictionary key value")
        window_objects["error_message"].configure(text=f"Sorry but there is an invalid input. Please try again!\n*{value_err}*")
        window_objects["error_message"].pack(side=tk.TOP)

def print_to_txt(window_objects):
    global stat_list
    cr = window_objects["cr"].get()
    write_stats_to_memory(window_objects)
    cr = stat_list[12]
    prof_bonus = stat_list[0]
    armor_class = stat_list[1]
    hit_points = stat_list[2]
    attack_bonus = stat_list[3]
    damage_per_round = stat_list[4]
    save_dc = stat_list[5]

    speed = stat_list[6].title()
    name = stat_list[7].title()
    type = stat_list[8].title()
    senses = stat_list[9].title()
    languages = stat_list[10].title()

    str = stat_list[11][0] 
    dex = stat_list[11][1] 
    con = stat_list[11][2]
    int = stat_list[11][3] 
    wis = stat_list[11][4] 
    cha = stat_list[11][5] 

    with open(f"{name.lower().replace(" ", "_")}_stat_block.txt", "w") as write_file:
        print(f"{name}",file=write_file)
        print(f"{type}",file=write_file)
        print("---------------",file=write_file)
        print(f"Armor Class: {armor_class}",file=write_file)
        print(f"Hit Points: {hit_points}",file=write_file)
        print(f"Speed: {speed}",file=write_file)
        print("---------------",file=write_file)
        print(f"STR:{str} | DEX:{dex} | CON:{con} | INT:{int} | WIS:{wis} | CHA:{cha}",file=write_file)
        print("---------------",file=write_file)
        print(f"## Add {prof_bonus} to any relevant proficiencies",file=write_file)
        print(f"Senses: {senses}",file=write_file)
        print(f"Languages: {languages}",file=write_file)
        print(f"Challenge: {cr}",file=write_file)
        print("Actions:---------------",file=write_file)
        print(f"## {name} will deal {damage_per_round} damage per round.",file=write_file)
        print(f"## Attack Bonus: +{attack_bonus}",file=write_file)
        print(f"## Save DC: {save_dc}",file=write_file)

if __name__ == "__main__":
    main()