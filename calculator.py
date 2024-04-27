import tkinter as tk
import math


def button_click(char):
    current = entry_box.get()
    if char == "Clear":
        entry_box.delete(0, tk.END)
    elif char == "=":
        try:
            result = eval(current)
            entry_box.delete(0, tk.END)
            entry_box.insert(0, str(result))
        except:
            entry_box.delete(0, tk.END)
            entry_box.insert(0, "Error")
    elif char == "√":
        entry_box.delete(0, tk.END)
        entry_box.insert(0, str(math.sqrt(float(current))))
    elif char == "x^2":
        entry_box.delete(0, tk.END)
        entry_box.insert(0, str(float(current) ** 2))
    elif char == "sin":
        entry_box.delete(0, tk.END)
        entry_box.insert(0, str(math.sin(math.radians(float(current)))))
    elif char == "cos":
        entry_box.delete(0, tk.END)
        entry_box.insert(0, str(math.cos(math.radians(float(current)))))
    elif char == "tan":
        entry_box.delete(0, tk.END)
        entry_box.insert(0, str(math.tan(math.radians(float(current)))))
    else:
        entry_box.insert(tk.END, char)


# Create the main window
root = tk.Tk()
root.title("Scientific Calculator")

# Entry box for displaying the input and result
entry_box = tk.Entry(root, width=35, borderwidth=5)
entry_box.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Define buttons
buttons = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("/", 1, 3),
    ("√", 1, 4),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),
    ("x^2", 2, 4),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("-", 3, 3),
    ("sin", 3, 4),
    ("0", 4, 0),
    (".", 4, 1),
    ("=", 4, 2),
    ("+", 4, 3),
    ("cos", 4, 4),
    ("Clear", 5, 0),
    ("tan", 5, 1),
]

# Create and place buttons
for text, row, col in buttons:
    button = tk.Button(
        root, text=text, padx=20, pady=20, command=lambda t=text: button_click(t)
    )
    button.grid(row=row, column=col)

# Run the application
root.mainloop()
