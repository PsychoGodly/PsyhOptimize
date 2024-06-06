import os
import subprocess
import tkinter as tk
from tkinter import messagebox

# Function to apply selected tweaks
def apply_tweaks():
    selected_items = listbox.curselection()
    if not selected_items:
        messagebox.showinfo("No Selection", "Please select at least one tweak.")
        return
    
    for index in selected_items:
        tweak = tweaks[index]
        reg_file = os.path.join("tweaks", tweak["file"])
        try:
            subprocess.run(["reg", "import", reg_file], check=True)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Failed to apply tweak: {tweak['name']}")
            return
    
    messagebox.showinfo("Success", "Tweaks applied successfully.")

# Load tweaks from files in the 'tweaks' folder
def load_tweaks():
    tweaks = []
    for file_name in os.listdir("tweaks"):
        if file_name.endswith(".reg"):
            with open(os.path.join("tweaks", file_name), "r") as file:
                lines = file.readlines()
                name = lines[0].strip().split('"')[1]
                description = lines[1].strip().split('"')[1]
                tweaks.append({"name": name, "description": description, "file": file_name})
    return tweaks

# Create the main window
root = tk.Tk()
root.title("Registry Tweaks")

# Load tweaks
tweaks = load_tweaks()

# Create a listbox to display tweaks
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
for tweak in tweaks:
    listbox.insert(tk.END, tweak["name"] + ": " + tweak["description"])
listbox.pack(padx=10, pady=10)

# Create an "Apply" button to apply selected tweaks
apply_button = tk.Button(root, text="Apply", command=apply_tweaks)
apply_button.pack(pady=5)

# Run the application
root.mainloop()
