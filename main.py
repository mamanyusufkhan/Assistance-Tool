import tkinter as tk
from tkinter import font
import valorant_combos
import valorant_agents


valorant_combos = valorant_combos.valorant_combos
valorant_agents = valorant_agents.valorant_agents









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

def update_agent_info(*args):
    selected_agent = agent_var.get()
    if selected_agent in valorant_agents:
        abilities = valorant_agents[selected_agent]["abilities"]
        tips = valorant_agents[selected_agent]["tips"]
        abilities_text = "\n".join([f"{key}: {value}" for key, value in abilities.items()])
        tips_text = "\n".join([f"Tip: {tip}" for tip in tips])
        agent_info_label.config(text=f"Abilities:\n{abilities_text}\n\nTips:\n{tips_text}")

def update_combo_info(*args):
    agent1 = agent_var1.get()
    agent2 = agent_var2.get()
    combo_key = f"{agent1} & {agent2}"
    if combo_key in valorant_combos:
        combo_info = valorant_combos[combo_key]
        abilities_text = "\n".join(combo_info["combo_abilities"])
        tips_text = "\n".join(combo_info["combo_tips"])
        combo_info_label.config(text=f"Combo Abilities:\n{abilities_text}\n\nCombo Tips:\n{tips_text}")
    else:
        combo_info_label.config(text="No combo information available for the selected agents.")

root = tk.Tk()
root.title("Valorant Assistant App")
root.geometry("600x600")
root.configure(bg='#0F1923')

# Set the icon (make sure the icon file path is correct)
root.iconbitmap('valorant.ico')  # Replace 'valorant.ico' with the actual path to your .ico file

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
name_entry = tk.Entry(main_frame, font=custom_font, width=40, bg='#2C2F33', fg='#FFFFFF', insertbackground='#FFFFFF')
name_entry.pack(pady=5)

tag_label = tk.Label(main_frame, text="Tag", font=custom_font, bg='#0F1923', fg='#FFFFFF')
tag_label.pack(pady=10)
tag_entry = tk.Entry(main_frame, font=custom_font, width=40, bg='#2C2F33', fg='#FFFFFF', insertbackground='#FFFFFF')
tag_entry.pack(pady=5)

label = tk.Label(main_frame, text="Enter details and click a button", font=custom_font, bg='#0F1923', fg='#FFFFFF')
label.pack(pady=20)

teach_me_button = tk.Button(main_frame, text="Teach Me", command=lambda: show_frame(teach_me_frame), font=custom_font, bg='#FF4655', fg='#FFFFFF', activebackground='#E53B45', activeforeground='#FFFFFF', width=20)
teach_me_button.pack(pady=5)

duo_mode_button = tk.Button(main_frame, text="Duo Mode", command=lambda: show_frame(duo_mode_frame), font=custom_font, bg='#7289DA', fg='#FFFFFF', activebackground='#5D74E2', activeforeground='#FFFFFF', width=20)
duo_mode_button.pack(pady=5)

# Teach Me frame content
teach_me_label = tk.Label(teach_me_frame, text="Teach Me Page", font=custom_font, bg='#0F1923', fg='#FFFFFF')
teach_me_label.pack(pady=20)

agent_var = tk.StringVar()
agent_var.set("Select an Agent")
agent_var.trace("w", update_agent_info)

agent_dropdown = tk.OptionMenu(teach_me_frame, agent_var, *valorant_agents.keys())
agent_dropdown.config(font=custom_font, bg='#2C2F33', fg='#FFFFFF', activebackground='#FF4655', activeforeground='#FFFFFF')
agent_dropdown["menu"].config(font=custom_font, bg='#2C2F33', fg='#FFFFFF', activebackground='#FF4655', activeforeground='#FFFFFF')
agent_dropdown.pack(pady=10)

agent_info_label = tk.Label(teach_me_frame, text="", font=custom_font, bg='#0F1923', fg='#FFFFFF', justify="left", wraplength=500)
agent_info_label.pack(pady=10)

back_button1 = tk.Button(teach_me_frame, text="Back", command=lambda: show_frame(main_frame), font=custom_font, bg='#FF4655', fg='#FFFFFF', activebackground='#E53B45', activeforeground='#FFFFFF', width=20)
back_button1.pack(pady=5)

# Duo Mode frame content
duo_mode_label = tk.Label(duo_mode_frame, text="Duo Mode Page", font=custom_font, bg='#0F1923', fg='#FFFFFF')
duo_mode_label.pack(pady=20)

agent_var1 = tk.StringVar()
agent_var1.set("Select Your Agent")
agent_var1.trace("w", update_combo_info)

agent_var2 = tk.StringVar()
agent_var2.set("Select Partner Agent")
agent_var2.trace("w", update_combo_info)

agent_dropdown1 = tk.OptionMenu(duo_mode_frame, agent_var1, *valorant_agents.keys())
agent_dropdown1.config(font=custom_font, bg='#2C2F33', fg='#FFFFFF', activebackground='#FF4655', activeforeground='#FFFFFF')
agent_dropdown1["menu"].config(font=custom_font, bg='#2C2F33', fg='#FFFFFF', activebackground='#FF4655', activeforeground='#FFFFFF')
agent_dropdown1.pack(pady=10)

agent_dropdown2 = tk.OptionMenu(duo_mode_frame, agent_var2, *valorant_agents.keys())
agent_dropdown2.config(font=custom_font, bg='#2C2F33', fg='#FFFFFF', activebackground='#FF4655', activeforeground='#FFFFFF')
agent_dropdown2["menu"].config(font=custom_font, bg='#2C2F33', fg='#FFFFFF', activebackground='#FF4655', activeforeground='#FFFFFF')
agent_dropdown2.pack(pady=10)

combo_info_label = tk.Label(duo_mode_frame, text="", font=custom_font, bg='#0F1923', fg='#FFFFFF', justify="left", wraplength=500)
combo_info_label.pack(pady=10)

back_button2 = tk.Button(duo_mode_frame, text="Back", command=lambda: show_frame(main_frame), font=custom_font, bg='#7289DA', fg='#FFFFFF', activebackground='#5D74E2', activeforeground='#FFFFFF', width=20)
back_button2.pack(pady=5)

show_frame(main_frame)

root.mainloop()