from tkinter import *
from tkinter import messagebox
from tkinter import ttk 

root = Tk()
root.title("Color Meaning Finder")
root.geometry("400x400")

label1 = Label(root, font=("Arial", 16, "bold"))
label1.pack(pady=10)

combobox = ttk.Combobox(root, font=("Arial", 14), state="readonly")
combobox['values'] = ["Red", "Blue", "Green", "Yellow", "Black"]
combobox.pack(pady=5)

color_meanings = {
    "Red": "Passion and energy",
    "Blue": "Calmness and trust",
    "Green": "Growth and harmony",
    "Yellow": "Happiness and optimism",
    "Black": "Power and elegance"
}

def colour_changer():
    selected_color = combobox.get()
    if selected_color in color_meanings:
        root.configure(bg=selected_color.lower())  # ✅ Fix here
        meaning = color_meanings[selected_color]
        label1.config(text=f"{selected_color}: {meaning}")
    else:
        messagebox.showerror("Error", "Color not found in the dictionary.")

btn = Button(root, text="Get Meaning", font=("Arial", 14), command=colour_changer)
btn.pack(pady=10)

root.mainloop()
