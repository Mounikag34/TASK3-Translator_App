import tkinter as tk
from tkinter import ttk
from googletrans import Translator

def translate_text():
    translator = Translator()
    source_text = source_text_entry.get("1.0", "end-1c")
    source_lang = source_lang_combo.get()
    target_lang = target_lang_combo.get()
    
    translation = translator.translate(source_text, src=source_lang, dest=target_lang)
    
    target_text_entry.delete("1.0", "end")
    target_text_entry.insert("1.0", translation.text)

# Create the main window
window = tk.Tk()
window.title("Language Translator")

# Create source text entry
source_text_label = ttk.Label(window, text="Source Text:")
source_text_label.pack()
source_text_entry = tk.Text(window, height=10, width=40)
source_text_entry.pack()

# Create source language selection
source_lang_label = ttk.Label(window, text="Source Language:")
source_lang_label.pack()
source_lang_combo = ttk.Combobox(window, values=["auto", "English", "French", "Spanish", "German", "Italian"])  # Add more languages if needed
source_lang_combo.pack()
source_lang_combo.current(0)

# Create target language selection
target_lang_label = ttk.Label(window, text="Target Language:")
target_lang_label.pack()
target_lang_combo = ttk.Combobox(window, values=["English", "French", "Spanish", "German", "Italian"])  # Add more languages if needed
target_lang_combo.pack()
target_lang_combo.current(0)

# Create translate button
translate_button = ttk.Button(window, text="Translate", command=translate_text)
translate_button.pack()

# Create target text entry
target_text_label = ttk.Label(window, text="Translated Text:")
target_text_label.pack()
target_text_entry = tk.Text(window, height=10, width=40)
target_text_entry.pack()

# Start the main loop
window.mainloop()

