""" This is NOT a part of the monster_generator program. Rather course requirements ask about coding experiments done in preperation. This program was made to better understand the options available in the tkinter module."""

import tkinter as tk
from tkinter import ttk, Button, Canvas, Checkbutton, Entry, Frame, Label, Listbox, Menu, Menubutton, Message, Radiobutton, Scale, Scrollbar, Text, Toplevel, Spinbox, PanedWindow, LabelFrame, messagebox, RIGHT, LEFT

def main():
    populate_main_window()


def populate_main_window():
    root = tk.Tk()
    frm_main = Frame(root)
    frm_main.master.title("Tkinter GUI Example")
    frm_main.pack(padx=3, pady=3, fill=tk.BOTH, expand=1)
    
    #Certain built-in themes can be added with themed tk objects (ttk)
    # s = ttk.Style()
    # s.theme_use('alt')
    
    msg = Message(root, text="Message Widget Down Here", width="200")
    
    def activate_message():
        msg.pack()

    def show_err_message():
        messagebox.showerror("Stop it", "Dont touch that")
        msg.pack_forget()

    mnu = Menu(root)
    mnu.add_command(label="MenuBar", command=print)
    mnu.add_cascade(label="Test this button", command=activate_message)
    root.config(menu=mnu)

    # Menubutton exists too but its too complicated for the scope of this project
    # mnubtn = Menubutton(root, text="MenuButton", menu=menu_bar)

    # Top Level is kinda odd. Good if you need a pop-up window. Disabled here
    # toplevel = Toplevel(root, bg="white", bd=5, relief="raised")
    # toplevel.title("New Window")

    btn = Button(frm_main, text="Button", command=show_err_message)
    cvs = Canvas(frm_main, width=300, height=200, bg="white")
    cvs.create_rectangle(50,50,150,150, fill="blue")
    cvs.create_text(100, 10, text="This is drawn on a canvas")
    chk = Checkbutton(frm_main, text="checkbox")
    ent = Entry(frm_main)
    lbl = Label(frm_main, text="Label")

    # Also you can do dropdowns instead with ttk
    # lbx = ttk.Combobox(frm_main, state="readonly", values=["one", "two", "three"])
    
    lbx = Listbox(frm_main, selectmode="SINGLE")
    lbx.insert(0,"option 0")
    lbx.insert(1,"option 1")
    lbx.insert(2,"option 2")
    lbx.insert(3,"option 3")
    lbx.insert(4,"option 4")
    lbx.insert(5,"option 5")
    lbx.insert(6,"option 6")
    lbx.insert(7,"option 7")
    lbx.insert(8,"option 8")

    rdo_frame = Frame(frm_main)
    rdo0 = Radiobutton(rdo_frame, text="option1", value=1)
    rdo1 = Radiobutton(rdo_frame, text="option2", value=2)
    rdo2 = Radiobutton(rdo_frame, text="option3", value=3)

    # Doesn't fully work like this but this is how you add the element
    scl = Scale(frm_main, from_=0, to=100, orient="horizontal", command=print)
    scr = Scrollbar(root, orient="vertical")
    txt = Text(frm_main, height=3, width=20, bg="white", fg="black", font=("Arial", 12))

    spn = Spinbox(frm_main, from_=0, to=100)

    pndwd = PanedWindow(frm_main, orient="horizontal")
    pndwd_left_list = tk.Listbox(root)
    pndwd_left_list.pack(side=tk.LEFT)
    pndwd.add(pndwd_left_list)
    pndwd_right_list = tk.Listbox(root)
    pndwd_right_list.pack(side=tk.LEFT)
    pndwd.add(pndwd_right_list)

    lblfr = LabelFrame(frm_main, text="Label Frame", bd=4)
    lblfrex = Label(lblfr, text="Label Frame Content")
    lblfrex.pack()

    # Layout all the labels, entry boxes, and buttons in a grid.
    scr.pack(side=RIGHT, fill="y", )

    lbl.grid(row=0, column=0, padx=3, pady=3)
    ent.grid(row=0, column=1, padx=3, pady=3)
    btn.grid(row=0, column=2, padx=3, pady=3)

    cvs.grid(row=1, column=0, padx=3, pady=3)
    chk.grid(row=1, column=1, padx=3, pady=3)
    lbx.grid(row=1, column=2, padx=3, pady=3)
    
    rdo_frame.grid(row=2, column=0, padx=3, pady=3)
    rdo0.pack()
    rdo1.pack()
    rdo2.pack()
    scl.grid(row=2, column=1, padx=3, pady=3)
    txt.grid(row=2, column=2, padx=3, pady=3)
    
    spn.grid(row=3, column=0, padx=3, pady=3)
    pndwd.grid(row=3, column=1, padx=3, pady=3)
    lblfr.grid(row=3, column=2, padx=3, pady=3)
    


    root.mainloop()


if __name__ == "__main__":
    main()
