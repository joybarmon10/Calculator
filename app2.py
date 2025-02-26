from tkinter import *

# UI Configuration
font = ("Helvetica", 30)
body_bg = "#2E3440"
button_bg = "#434C5E"
display_bg = "#4C566A"

root_window = Tk()
root_window.title("Calculator")
root_window.geometry("400x600")
root_window.config(bg=body_bg)

# Heading Label (grid ব্যবহৃত)
heading_label = Label(root_window, text="Calculator", font=font, bg=body_bg, fg="white")
heading_label.grid(row=0, column=0, columnspan=4, pady=10)

# Display Input (grid ব্যবহৃত)
display_input = Entry(
    root_window, justify=RIGHT, font=font, bd=5, bg=display_bg, fg="white"
)
display_input.grid(
    row=1, column=0, columnspan=4, padx=10, pady=10, ipady=10, sticky="nsew"
)


# Function to handle button clicks
def button_click(value):
    if value == "=":
        try:
            result = eval(display_input.get())
            display_input.delete(0, END)
            display_input.insert(END, str(result))
        except:
            display_input.delete(0, END)
            display_input.insert(END, "Error")
    elif value == "C":
        display_input.delete(0, END)
    else:
        display_input.insert(END, value)


# Button Layout
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "C", "+"),
    ("⌫", "="),
]

colors = {"C": "#BF616A", "⌫": "#4C566A", "=": "#5E81AC"}

# Creating buttons
for r, row in enumerate(buttons, 2):
    for c, text in enumerate(row):
        Button(
            root_window,
            text=text,
            font=("Helvetica", 16),
            padx=20,
            pady=20,
            bg=colors.get(text, button_bg),
            fg="white",
            command=lambda t=text: button_click(t),
        ).grid(row=r, column=c, sticky="nsew")

# Responsive grid
for i in range(6):
    root_window.grid_rowconfigure(i, weight=1)
for j in range(4):
    root_window.grid_columnconfigure(j, weight=1)

root_window.mainloop()
