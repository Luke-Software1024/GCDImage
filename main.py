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

window.mainloop()