import os
from tkinter import *
import tkinter as ttk
from tkinter import filedialog
from tkinter import messagebox

# Set the windows
root = ttk.Tk()
root.geometry("530x150")
root.title("Search Manager")
root.resizable(0,0)
def browseFiles1():
    filename = filedialog.askdirectory(initialdir="/", title="Sélectionner le dossier")
    folder_location.get()
    folder_location.set(filename)
def open1():
    folder = folder_location.get()
    file = file_name.get()
    file_type = ['doc', 'docm', 'docx', 'dot']
    error_count = 0
    for type in file_type:
        try:
            os.startfile(f'{folder}/{file}.{type}')
        except:
            error_count += 1
            pass
    if error_count == 4:
        messagebox.showerror("showerror", "Fichier Introuvable")


def browseFiles2():
    filename = filedialog.askdirectory(initialdir="/", title="Sélectionner le dossier")
    folder_location2.get()
    folder_location2.set(filename)

def open2():
    folder = folder_location2.get()
    file = file_name2.get()
    file_type = ['doc', 'docm', 'docx', 'dot']
    error_count = 0
    for type in file_type:
        try:
            os.startfile(f'{folder}/{file}.{type}')
        except:
            error_count += 1
            pass
    if error_count == 4:
        messagebox.showerror("showerror", "Fichier Introuvable")


folder_location = ttk.StringVar()
file_name = ttk.StringVar()

folder_location2 = ttk.StringVar()
file_name2 = ttk.StringVar()

folder1_Label = ttk.Label(root, text='Dossier 1', font=("Times New Roman", 15)).place(x=30, y=20)
folder1_Entry = ttk.Entry(root,width=30, textvariable=file_name).place(x=130, y=25)
folder1_Search = ttk.Button(root, text="...", width=5, command=browseFiles1).place(x=320, y=18)
folder1_Open = ttk.Button(root, text="Ouvrire", width=15, command=open1).place(x=370, y=18)

folder2_Label = ttk.Label(root, text='Dossier 2', font=("Times New Roman", 15)).place(x=30, y=80)
folder2_Entry = ttk.Entry(root,width=30, textvariable=file_name2).place(x=130, y=85)
folder2_Search = ttk.Button(root, text="...", width=5, command=browseFiles2).place(x=320, y=80)
folder2_Open = ttk.Button(root, text="Ouvrire", width=15, command=open2).place(x=370, y=80)

root.mainloop()