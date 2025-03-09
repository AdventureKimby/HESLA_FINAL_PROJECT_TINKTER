#import tinkter and random font generator
import tkinter as tk
import tkinter.font as font
import random

#definition of random font
def generate_random_font(text):
    font_families = list(font.families())
    random_font = random.choice(font_families)
    random_size = random.randint(10, 30)
    return (random_font, random_size)

#defintion of main window into new windows with exit button
def create_font_window(text):
    new_window = tk.Toplevel()
    new_window.title("Generated Font")
    generated_font = generate_random_font(text)
    label = tk.Label(new_window, text=text, font=generated_font)
    label.pack(padx=20, pady=20)

    exit_button = tk.Button(new_window, text="Exit", command=new_window.destroy)
    exit_button.pack(pady=10)

#definition of text input button
def handle_button_click(text_input, button_type):
     text = text_input.get()
     if text:
        create_font_window(text)

#definition of main window, text label, and text input box
def main_window():
    root = tk.Tk()
    root.title("Random Font Generator")

    text_input_label = tk.Label(root, text="Enter text:")
    text_input_label.pack(pady=10)

    text_input = tk.Entry(root)
    text_input.pack(pady=5)

    #button creation
    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)

    button_texts = ["Font 1", "Font 2", "Font 3"]
    for button_text in button_texts:
        button = tk.Button(button_frame, text=button_text, command=lambda text=text_input, button_type=button_text: handle_button_click(text, button_type))
        button.pack(side=tk.LEFT, padx=10)

    #loop outside of main window
    root.mainloop()

if __name__ == "__main__":
    main_window()
