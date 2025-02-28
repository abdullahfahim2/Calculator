import tkinter as tk

# Colors and Fonts
light_gray = "#F5F5F5"
label_color = "#25265E"
white = "#FFFFFF"
light_blue = "#D1E5F4"
off_white = "#F8FAFF"
digit_font = ("Arial", 24, "bold")
default_font = ("Arial", 20)
s_font = ("Arial", 16)
l_font = ("Arial", 40)
op_color = "#FF9913"
red = "#FF474C"
light = "#666362"


total_expression = ""
current_expression = ""


window = tk.Tk()
window.geometry("375x667")
window.resizable(0, 0)
window.title("Calculator By Md Abdullah Al Fahim")


def update_total_label():
    global total_expression
    expression = total_expression
    total_label.config(text=expression)

def update_label():
    label.config(text=current_expression)


def add_to_expression(value):
    global current_expression
    current_expression += str(value)
    update_label()


def append_operator(operator):
    global total_expression, current_expression
    total_expression += current_expression + operator
    current_expression = ""
    update_total_label()
    update_label()


def evaluate():
    global total_expression, current_expression
    total_expression += current_expression
    update_total_label()
    try:
        current_expression = str(eval(total_expression))
        total_expression = ""
    except:
        current_expression = "Error!"
    update_label()


def clear():
    global total_expression, current_expression
    total_expression = ""
    current_expression = ""
    update_label()
    update_total_label()


def square():
    global current_expression
    current_expression = str(eval(f"{current_expression}**2"))
    update_label()


def sqrt():
    global current_expression
    current_expression = str(eval(f"{current_expression}**0.5"))
    update_label()

def modulus():
    global current_expression
    current_expression = str(eval(f"({current_expression}/100)"))
    update_label()

# Create frame
display_frame = tk.Frame(window, height=221, bg=light_gray)
display_frame.pack(expand=True, fill="both")

buttons_frame = tk.Frame(window)
buttons_frame.pack(expand=True, fill="both")

# Create label
total_label = tk.Label(display_frame, text=total_expression, anchor=tk.E, bg=light_gray, fg=label_color, padx=24, font=s_font)
total_label.pack(expand=True, fill="both")

label = tk.Label(display_frame, text=current_expression, anchor=tk.E, bg=light_gray, fg=label_color, padx=24, font=l_font)
label.pack(expand=True, fill="both")

# Button layout
digits = {
    7: (1, 1), 8: (1, 2), 9: (1, 3),
    4: (2, 1), 5: (2, 2), 6: (2, 3),
    1: (3, 1), 2: (3, 2), 3: (3, 3),
    '.': (4, 1), 0: (4, 2)
}
operations = {
    "/": "\u00F7",
    "*": "\u00D7",
    "-": "-",
    "+ ": "+"
}

for digit, grid_value in digits.items():
    button = tk.Button(buttons_frame, text=str(digit), bg=white, fg=label_color, font=digit_font, borderwidth=0, command=lambda x=digit: add_to_expression(x))
    button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

i = 0
for operator, symbol in operations.items():
    button = tk.Button(buttons_frame, text=symbol, bg=op_color, fg=label_color, font=default_font, borderwidth=0, command=lambda x=operator: append_operator(x))
    button.grid(row=i, column=4, sticky=tk.NSEW)
    i += 1

clear_button = tk.Button(buttons_frame, text="C", bg=red, fg=label_color, font=default_font, borderwidth=0, command=clear)
clear_button.grid(row=0, column=1, sticky=tk.NSEW)

square_button = tk.Button(buttons_frame, text="x\u00b2", bg=op_color, fg=label_color, font=default_font, borderwidth=0, command=square)
square_button.grid(row=0, column=2, sticky=tk.NSEW)

sqrt_button = tk.Button(buttons_frame, text="\u221ax", bg=op_color, fg=label_color, font=default_font, borderwidth=0, command=sqrt)
sqrt_button.grid(row=0, column=3, sticky=tk.NSEW)

modulus_button = tk.Button(buttons_frame, text="%", bg=light_blue, fg=label_color, font=default_font, borderwidth=0, command=modulus)
modulus_button.grid(row=4, column=3, sticky=tk.NSEW)

equals_button = tk.Button(buttons_frame, text="=", bg=light_blue, fg=label_color, font=default_font, borderwidth=0, command=evaluate)
equals_button.grid(row=4, column=4, sticky=tk.NSEW)

buttons_frame.rowconfigure(0, weight=1)
for x in range(1, 5):
    buttons_frame.rowconfigure(x, weight=1)
    buttons_frame.columnconfigure(x, weight=1)

def bind_keys():
    window.bind("<Return>", lambda event: evaluate())
    for key in digits:
        window.bind(str(key), lambda event, digit=key: add_to_expression(digit))
    for key in operations:
        window.bind(str(key), lambda event, operator=key: append_operator(operator))
bind_keys()

window.mainloop()
