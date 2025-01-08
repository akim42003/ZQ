import tkinter as tk
import speech_recognition as sr
from tkinter import filedialog
from word2number import w2n
import os
#import pyinstaller

#constructor for system events and GUI
class CustomText(tk.Text):
    def cut(self):
        self.event_generate("<<Cut>>")

    def copy(self):
        self.event_generate("<<Copy>>")

    def paste(self):
        self.event_generate("<<Paste>>")

    def select_all(self):
        self.tag_add("sel", "1.0", "end")

    def go_to_start(self):
        self.mark_set(tk.INSERT, "1.0")

    def go_to_end(self):
        self.mark_set(tk.INSERT, tk.END)

    def go_to_line(self, line_number):
        self.mark_set(tk.INSERT, f"{line_number}.0")

    def go_to_word(self, word):
        idx = "1.0"
        while True:
            idx = self.search(word, idx, stopindex=tk.END, nocase=1, count=tk.TRUE)
            if not idx:
                break
            last_idx = f"{idx}+{len(word)}c"
            self.mark_set(tk.INSERT, idx)
            self.see(tk.INSERT)
            yield idx, last_idx
            idx = last_idx

    def move_cursor_left(self):
        current_pos = self.index(tk.INSERT)
        if current_pos != "1.0":
            self.mark_set(tk.INSERT, f"{current_pos}-1c")

    def move_cursor_right(self):
        current_pos = self.index(tk.INSERT)
        if current_pos != tk.END:
            self.mark_set(tk.INSERT, f"{current_pos}+1c")

def new_file():
    text_editor.delete(1.0, tk.END)

#creates/opens file directory to access txt files
def open_file():
    dir_path = "~/ZQ_docs"
        # Expand the user home symbol ~ to full path
    full_dir_path = os.path.expanduser(dir_path)

        # Check if directory exists
    if not os.path.exists(full_dir_path):
            # Create the directory if it doesn't exist
        os.makedirs(full_dir_path)
            
        # Check if directory is empty
    if not os.listdir(full_dir_path):
            # Specify the file name
        file_name = "newfile.txt"
        file_path = os.path.join(full_dir_path, file_name)
            
            # Create the file if directory is empty
        open(file_path, 'w').close() # Create the file
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension='.txt')
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_editor.get(1.0, tk.END))

def save_as_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w") as file:
            content = text_editor.get(1.0, tk.END)
            file.write(content)
#highlights text based on speech input
def select_text(start, end):
    text_editor.tag_remove("sel", "1.0", tk.END)
    text_editor.tag_add("sel", start, end)

def delete_selected_text():
    text_editor.cut()

#writes text based on speech input
def insert_text(text):
    text_editor.insert(tk.INSERT, text)

#controls voice commands note ZQ is key phrase for initiating commands
def get_voice_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("Command:", command)
        if "zq new" in command:
            new_file()
        elif "zq open" in command:
            open_file()
        elif "zq save" in command:
            save_file()
        elif "zq save as" in command:
            save_as_file()
        elif "zq cut" in command:
            text_editor.cut()
        elif "zq copy" in command:
            text_editor.copy()
        elif "zq paste" in command:
            text_editor.paste()
        elif "zq select all" in command:
            text_editor.select_all()
        elif "zq select" in command:
            words = command.split(" ")
            start_index = words.index("select") + 1
            end_index = len(words)
            selected_text = " ".join(words[start_index:end_index])
            select_start = text_editor.search(selected_text, "1.0", tk.END)
            if select_start:
                select_end = f"{select_start}+{len(selected_text)}c"
                select_text(select_start, select_end)
            else:
                print("Text not found.")
        elif "zq delete" in command:
            delete_selected_text()
        elif "zq go to start" in command:
            text_editor.go_to_start()
        elif "zq go to end" in command:
            text_editor.go_to_end()
        elif "zq go to line" in command:
            line_number=w2n.word_to_num(command.split()[-1])
            text_editor.go_to_line(line_number)
        elif "zq go to word" in command:
            word = command.split("go to word")[-1].strip()
            for idx, last_idx in text_editor.go_to_word(word):
                select_text(idx, last_idx)
                break
        elif "zq move left" in command:
            text_editor.move_cursor_left()
        elif "zq move right" in command:
            text_editor.move_cursor_right()
        elif "zq" in command:
            pass
        else:
            insert_text(command)  # Voice typing
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"Error during recognition: {e}")

root = tk.Tk()
root.title("Voice Controlled Text Editor")

# Create a custom Text class instance
text_editor = CustomText(root, wrap=tk.WORD, bg="#000000", fg="#D5C5FE", font="Arial 20")
text_editor.pack(expand=True, fill='both')

button_frame = tk.Frame(root)
button_frame.pack(fill='both', expand=True)

voice_button = tk.Button(button_frame, text="Voice Command", command=get_voice_command, bg="#D5C5FE", fg="black", relief=tk.FLAT)
voice_button.pack(side=tk.BOTTOM, fill='both', expand = True)

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)



file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=text_editor.cut)
edit_menu.add_command(label="Copy", command=text_editor.copy)
edit_menu.add_command(label="Paste", command=text_editor.paste)
edit_menu.add_command(label="Select All", command=text_editor.select_all)

root.mainloop()