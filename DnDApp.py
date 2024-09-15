import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.scrolledtext as scrolledtext
import random as rand
from random import *
import webbrowser as wb
from webbrowser import *
#create random stats and populate them
def stat_roll():
    strength = rand.randint(1,18)
    dexterity = rand.randint(1,18)
    constitution = rand.randint(1,18)
    intelligence = rand.randint(1,18)
    wisdom = rand.randint(1,18)
    charisma = rand.randint(1,18)
    
    str_score.delete(0,"end")
    dex_score.delete(0,"end")
    con_score.delete(0,"end")
    int_score.delete(0,"end")
    wis_score.delete(0,"end")
    cha_score.delete(0,"end")
    
    str_score.insert(0,strength)
    dex_score.insert(0,dexterity)
    con_score.insert(0,constitution)
    int_score.insert(0,intelligence)
    wis_score.insert(0,wisdom)
    cha_score.insert(0,charisma)
def open_name():
    wb.open("https://www.fantasynamegenerators.com/")    
 


window = tk.Tk()
window.title("DnD NPC App")
window.geometry("600x600")

# Information Tab
tabs = ttk.Notebook(window)
tabs.pack(pady=20)
# Info frame
info_frame = Frame(tabs,width = 580, height= 580)

# Stats frame
stats_frame = Frame(tabs,width = 580, height= 580)

# SRD frame
srd_frame = Frame(tabs,width = 580, height= 580)

#Add Frames to Window
tabs.add(info_frame, text="Info")
tabs.add(stats_frame, text="Stats and Attributes")
tabs.add(srd_frame,text="SRD Rules")



#Information and Links
links = LabelFrame(info_frame,text="Links")
links.pack(padx=20)
names_button = Button(info_frame,text='Name Generator',command=open_name)
names_button.place(x=25,y=25)




#Stats interactable
stat_str = LabelFrame(stats_frame,text="STR")
stat_str.pack(padx=20)
str_score = Entry(stat_str,font=('Calibri',10))
str_score.pack(pady=10,padx=10)

stat_dex = LabelFrame(stats_frame,text="DEX")
stat_dex.pack(padx=20)
dex_score = Entry(stat_dex,font=('Calibri',10))
dex_score.pack(pady=10,padx=10)

stat_con = LabelFrame(stats_frame,text="CON")
stat_con.pack(padx=20)
con_score = Entry(stat_con,font=('Calibri',10))
con_score.pack(pady=10,padx=10)

stat_int = LabelFrame(stats_frame,text="INT")
stat_int.pack(padx=20)
int_score = Entry(stat_int,font=('Calibri',10))
int_score.pack(pady=10,padx=10)

stat_wis = LabelFrame(stats_frame,text="WIS")
stat_wis.pack(padx=20)
wis_score = Entry(stat_wis,font=('Calibri',10))
wis_score.pack(pady=10,padx=10)

stat_cha = LabelFrame(stats_frame,text="CHA")
stat_cha.pack(padx=20)
cha_score = Entry(stat_cha,font=('Calibri',10))
cha_score.pack(pady=10,padx=10)



roll_button =Button(stats_frame,text="Roll Stats",command=stat_roll)
roll_button.place(x=100,y=390)

# SRD usage rules
srd_rules = LabelFrame(srd_frame, text="SRD Use Rules")
srd_rules.pack(pady=20)
srd_txt = scrolledtext.ScrolledText(srd_rules,
                       wrap=tk.WORD,
                       width=65,
                       height=50,
                       font=("Times New Roman",
                       15))
srd_txt.grid(column=0,row=0)
srd_txt.insert(END,"This work includes material taken from the System Reference Document 5.1 (“SRD 5.1”) by Wizards of the Coast LLC and available at https://dnd.wizards.com/resources/systems-reference-document. The SRD 5.1 is licensed under the Creative Commons Attribution 4.0 International License available at https://creativecommons.org/licenses/by/4.0/legalcode.)")

window.mainloop()