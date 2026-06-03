import tkinter as tk
from tkinter import ttk, filedialog

window = tk.Tk()
window.title("GOscdimg")

tabs = ttk.Notebook(window)
tab_general = ttk.Frame(window)
tabs.add(tab_general, text="General")
tab_fs = ttk.Frame(window)
tabs.add(tab_fs, text="Filesystem")
tab_boot = ttk.Frame(window)
tabs.add(tab_boot, text="Bootability")
tab_optimize = ttk.Frame(window)
tabs.add(tab_optimize, text="Optimization")
tab_order = ttk.Frame(window)
tabs.add(tab_order, text="File Order")
tab_dvd = ttk.Frame(window)
tabs.add(tab_dvd, text="DVD Video")
tab_mesg = ttk.Frame(window)
tabs.add(tab_mesg, text="Messages")
tab_other = ttk.Frame(window)
tabs.add(tab_other, text="Other")
tabs.grid(row=0, column=0)

oscdimg_exec_label = ttk.Label(tab_general, text="OSCDIMG executable:")
oscdimg_exec_label.grid(row=0, column=0)

oscdimg_exec = tk.StringVar()
oscdimg_exec_input = ttk.Entry(tab_general, textvariable=oscdimg_exec)
oscdimg_exec_input.grid(row=0, column=1)

def open_filedialog_oe():
    oscdimg_exec.set(filedialog.askopenfilename(filetypes=(("Executables", "*.exe"), ("All Files", "*.*")), title="Select oscdimg.exe executable:"))
oscdimg_exec_browse = ttk.Button(tab_general, text="Browse...", command=open_filedialog_oe)
oscdimg_exec_browse.grid(row=0, column=2)

input_folder_label = ttk.Label(tab_general, text="Input folder:")
input_folder_label.grid(row=1, column=0)

input_folder = tk.StringVar()
input_folder_input = ttk.Entry(tab_general, textvariable=input_folder)
input_folder_input.grid(row=1, column=1)

def open_filedialog_if():
    input_folder.set(filedialog.askdirectory(title="Select input folder:"))
input_folder_browse = ttk.Button(tab_general, text="Browse...", command=open_filedialog_if)
input_folder_browse.grid(row=1, column=2)

output_image_label = ttk.Label(tab_general, text="Output image:")
output_image_label.grid(row=2, column=0)

output_image = tk.StringVar()
output_image_input = ttk.Entry(tab_general, textvariable=output_image)
output_image_input.grid(row=2, column=1)

def open_filedialog_oi():
    output_image.set(filedialog.asksaveasfilename(filetypes=(("Disc Images", "*.iso"), ("All Files", "*.*")), title="Select output image:"))
output_image_browse = ttk.Button(tab_general, text="Browse...", command=open_filedialog_oi)
output_image_browse.grid(row=2, column=2)

window.mainloop()