import tkinter as tk
from tkinter import font

# Calculator functions
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def delete():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])  # Remove the last character


def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("350x450")  # Slightly taller to accommodate the new button
root.configure(bg="#2E3440")

# Custom font
custom_font = font.Font(family="Helvetica", size=16)

# Entry widget for display
entry = tk.Entry(
    root,
    width=25,
    font=custom_font,
    borderwidth=5,
    justify="right",
    bg="#4C566A",
    fg="#D8DEE9",
)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

# Button layout
buttons = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("/", 1, 3),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("-", 3, 3),
    ("0", 4, 0),
    (".", 4, 1),
    ("C", 4, 2),
    ("+", 4, 3),  # Add button
    ("⌫", 5, 0),  # Delete button
    ("=", 5, 1),
    # ("+", 5, 3),
]

# Create and place buttons
for text, row, col in buttons:
    if text == "=":
        btn = tk.Button(
            root,
            text=text,
            padx=20,
            pady=20,
            font=custom_font,
            bg="#5E81AC",
            fg="#D8DEE9",
            command=calculate,
        )
        btn.grid(row=row, column=col, columnspan=2, sticky="nsew")  # Span 2 columns
    elif text == "C":
        btn = tk.Button(
            root,
            text=text,
            padx=20,
            pady=20,
            font=custom_font,
            bg="#BF616A",
            fg="#D8DEE9",
            command=clear,
        )
        btn.grid(row=row, column=col, sticky="nsew")
    elif text == "⌫":
        btn = tk.Button(
            root,
            text=text,
            padx=20,
            pady=20,
            font=custom_font,
            bg="#4C566A",
            fg="#D8DEE9",
            command=delete,
        )
        btn.grid(row=row, column=col, sticky="nsew")
    else:
        btn = tk.Button(
            root,
            text=text,
            padx=20,
            pady=20,
            font=custom_font,
            bg="#4C566A",
            fg="#D8DEE9",
            command=lambda t=text: button_click(t),
        )
        btn.grid(row=row, column=col, sticky="nsew")

# Configure grid weights for responsiveness
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Run the application
root.mainloop()
