import tkinter as tk
from tkinter import messagebox, filedialog
import webbrowser

def save_note():
    note = text_box.get("1.0", tk.END).strip()
    if note == "":
        messagebox.showwarning("Error", "There are no notes to save!")
        return
    
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(note)
        text_box.delete("1.0", tk.END)
        messagebox.showinfo("Success", f"The note has been saved as {file_path}!")

def open_note():
    file_path = filedialog.askopenfilename(title="Choose a Note", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            note_content = file.read()
            text_box.delete("1.0", tk.END)
            text_box.insert(tk.END, note_content)

def open_github():
    webbrowser.open("https://github.com/luxacreative/notes-app")

def toggle_light_mode():
    global light_mode
    light_mode = not light_mode
    if light_mode:
        root.configure(bg="#FFFFFF")
        text_box.configure(bg="#F0F0F0", fg="#000000", insertbackground='black')
        save_button.configure(bg="#DDDDDD", fg="#000000")
        open_button.configure(bg="#DDDDDD", fg="#000000")
        credit_button.configure(bg="#CCCCCC", fg="#000000")
        light_mode_button.configure(bg="#DDDDDD", fg="#000000")
    else:
        root.configure(bg="#2E2E2E")
        text_box.configure(bg="#333333", fg="#FFFFFF", insertbackground='white')
        save_button.configure(bg="#444444", fg="#FFFFFF")
        open_button.configure(bg="#444444", fg="#FFFFFF")
        credit_button.configure(bg="#555555", fg="#FFFFFF")
        light_mode_button.configure(bg="#444444", fg="#FFFFFF")

root = tk.Tk()
root.title("Notes Application")
root.state('zoomed')
root.configure(bg="#2E2E2E")

light_mode = False

text_box = tk.Text(root, height=25, width=80, bg="#333333", fg="#FFFFFF", insertbackground='white', font=('Arial', 12))
text_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

save_button = tk.Button(root, text="Save Note", command=save_note, bg="#444444", fg="#FFFFFF", font=('Arial', 12))
save_button.pack(pady=10)

open_button = tk.Button(root, text="Open Note", command=open_note, bg="#444444", fg="#FFFFFF", font=('Arial', 12))
open_button.pack(pady=10)

credit_button = tk.Button(root, text="Credit", command=open_github, bg="#555555", fg="#FFFFFF", font=('Arial', 12))
credit_button.pack(pady=10)

light_mode_button = tk.Button(root, text="Toggle Light Mode", command=toggle_light_mode, bg="#444444", fg="#FFFFFF", font=('Arial', 12))
light_mode_button.pack(pady=10)

def toggle_full_screen(event=None):
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))
    text_box.config(width=root.winfo_width() // 10, height=root.winfo_height() // 30)

root.bind("<F11>", toggle_full_screen)
root.mainloop()