import tkinter as tk

window = tk.Tk()
ent_name = tk.Entry(master=window, width=40)
ent_name.pack()

ent_name.insert(0, 'What is your name?')
window.mainloop()