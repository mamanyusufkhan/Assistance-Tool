import tkinter as tk
from tkinter import font

def show_text():
    entered_name = name_entry.get()
    entered_tag = tag_entry.get()
    label.config(text=f"In-game Name: {entered_name}, Tag: {entered_tag}")

def clear_text():
    name_entry.delete(0, tk.END)
    tag_entry.delete(0, tk.END)
    label.config(text="")

def show_frame(frame):
    frame.tkraise()

root = tk.Tk()
root.title("Valorant Assistant App")
root.geometry("400x400")
root.configure(bg='#0F1923')

# Set the icon (make sure the icon file path is correct)
root.iconbitmap('valorant.ico')  # Replace 'path_to_icon.ico' with the actual path to your .ico file

custom_font = font.Font(family="Helvetica", size=12, weight="bold")

# Create the container frame
container = tk.Frame(root)
container.pack(fill='both', expand=True)

# Create frames for each page
main_frame = tk.Frame(container, bg='#0F1923')
teach_me_frame = tk.Frame(container, bg='#0F1923')
duo_mode_frame = tk.Frame(container, bg='#0F1923')

for frame in (main_frame, teach_me_frame, duo_mode_frame):
    frame.grid(row=0, column=0, sticky='nsew')

# Configure grid to expand with window size
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

# Main frame content
name_label = tk.Label(main_frame, text="In-game Name", font=custom_font, bg='#0F1923', fg='#FFFFFF')
name_label.pack(pady=10)
name_entry = tk.Entry(main_frame, font=custom_font, width=30, bg='#2C2F33', fg='#FFFFFF', insertbackground='#FFFFFF')
name_entry.pack(pady=5)

tag_label = tk.Label(main_frame, text="Tag", font=custom_font, bg='#0F1923', fg='#FFFFFF')
tag_label.pack(pady=10)
tag_entry = tk.Entry(main_frame, font=custom_font, width=30, bg='#2C2F33', fg='#FFFFFF', insertbackground='#FFFFFF')
tag_entry.pack(pady=5)

label = tk.Label(main_frame, text="Enter details and click a button", font=custom_font, bg='#0F1923', fg='#FFFFFF')
label.pack(pady=20)

teach_me_button = tk.Button(main_frame, text="Teach Me", command=lambda: show_frame(teach_me_frame), font=custom_font, bg='#FF4655', fg='#FFFFFF', activebackground='#E53B45', activeforeground='#FFFFFF', width=15)
teach_me_button.pack(pady=5)

duo_mode_button = tk.Button(main_frame, text="Duo Mode", command=lambda: show_frame(duo_mode_frame), font=custom_font, bg='#7289DA', fg='#FFFFFF', activebackground='#5D74E2', activeforeground='#FFFFFF', width=15)
duo_mode_button.pack(pady=5)

# Teach Me frame content
teach_me_label = tk.Label(teach_me_frame, text="Teach Me Page", font=custom_font, bg='#0F1923', fg='#FFFFFF')
teach_me_label.pack(pady=20)
back_button1 = tk.Button(teach_me_frame, text="Back", command=lambda: show_frame(main_frame), font=custom_font, bg='#FF4655', fg='#FFFFFF', activebackground='#E53B45', activeforeground='#FFFFFF', width=15)
back_button1.pack(pady=5)

# Duo Mode frame content
duo_mode_label = tk.Label(duo_mode_frame, text="Duo Mode Page", font=custom_font, bg='#0F1923', fg='#FFFFFF')
duo_mode_label.pack(pady=20)
back_button2 = tk.Button(duo_mode_frame, text="Back", command=lambda: show_frame(main_frame), font=custom_font, bg='#7289DA', fg='#FFFFFF', activebackground='#5D74E2', activeforeground='#FFFFFF', width=15)
back_button2.pack(pady=5)

show_frame(main_frame)

root.mainloop()


root.mainloop()