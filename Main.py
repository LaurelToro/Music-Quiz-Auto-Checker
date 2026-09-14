import tkinter as tk
from tkinter import filedialog
from Imagetotext import ImagetoText
from ImageManipulation import answerkey, answersheet
from CrossCheck import crosscheck
import os
import threading


answer_file_path = None
user_file_path = None

def export_to_file():
    file_path = filedialog.asksaveasfilename(
        title="Gem svar",
        initialfile=team_name.get() + ".txt",
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")],
    )
    if file_path:
        with open(file_path, "w") as output_file:
            output_file.write("Holdnavn: " + team_name.get() + "\n\n")
            output_file.write(file_contents.get("1.0", tk.END))


def import_answer_file():
    global answer_file_path
    answer_file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("All files", "*.*")])
    if answer_file_path:
        a_selected_file_label.config(text=f"Selected: {answer_file_path}")

def import_user_file():
    global user_file_path
    user_file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("All files", "*.*")])
    if user_file_path:
        u_selected_file_label.config(text=f"Selected: {user_file_path}")


def read_file():
    read_button.config(state=tk.DISABLED)
    loading_label.config(text="Reading files, please wait...")
    threading.Thread(target=process_files, daemon=True).start()


def process_files():
    answerkey(answer_file_path)
    answersheet(user_file_path)
    answer_contents, user_contents = ImagetoText()
    crosscheck_results = crosscheck(answer_contents, user_contents)

    root.after(0, show_results, answer_contents, user_contents, crosscheck_results)


def show_results(answer_contents, user_contents, crosscheck_results):

    file_contents.delete("1.0", tk.END)
    file_contents.insert("1.0", "Svar nøgle:\n" + "\n".join(answer_contents))
    file_contents.insert(tk.END, "\n\nSvar-ark:\n" + "\n".join(user_contents))
    file_contents.insert(tk.END, "\n\nResultater:\n" + crosscheck_results)
    loading_label.config(text="Finished")
    read_button.config(state=tk.NORMAL)
    os.remove("Program\\Pictures\\CleanImages\\CleanimageAnswerKey.png")
    os.remove("Program\\Pictures\\CleanImages\\CleanimageAnswerSheet.png")



root = tk.Tk()
team_name = tk.StringVar()
root.geometry("400x500")
root.title("Quiz Svar-Tjekker")
label = tk.Label(root, text="Velkommen til Quiz Svar-Tjekker!")
label.pack()

team_name_label = tk.Label(root, text="Holdnavn")
team_name_label.pack()
team_name_input = tk.Entry(root, textvariable=team_name)
team_name_input.pack()
export_button = tk.Button(root, text="Eksport til en .txt fil", command=export_to_file)
export_button.pack(pady=10)

import_button = tk.Button(root, text="Import svar-nøgle", command=import_answer_file)
import_button.pack(pady=10)
a_selected_file_label = tk.Label(root, text="Ingen svar-nøgle valgt")
a_selected_file_label.pack()
import_button = tk.Button(root, text="Import svar-ark", command=import_user_file)
import_button.pack(pady=10)
u_selected_file_label = tk.Label(root, text="Intet svar-ark valgt")
u_selected_file_label.pack()

button_frame = tk.Frame(root)
button_frame.pack(fill="x", padx=10, pady=10)

read_button = tk.Button(button_frame, text="Read File", command=read_file)
read_button.pack(side="left")
stop_button = tk.Button(button_frame, text="Luk programmet", command=root.destroy)
stop_button.pack(side="right")

loading_label = tk.Label(root, text="")
loading_label.pack()

file_contents = tk.Text(root, wrap="word", height=15, width=45)
file_contents.pack(padx=10, pady=10, fill="both", expand=True)

root.mainloop()