import tkinter as tk
from math import sqrt

# Function for button click
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

# Function to clear the entry
def clear_entry():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def evaluate_expression():
    try:
        current = entry.get()
        result = eval(current)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function for square root
def square_root():
    try:
        current = float(entry.get())
        result = sqrt(current)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget for the input
entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Define buttons and layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0), ('sqrt', 5, 1), ('%', 5, 2), ('**', 5, 3),
]

# Add buttons to the window
for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), 
                  command=evaluate_expression).grid(row=row, column=col)
    elif text == 'C':
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), 
                  command=clear_entry).grid(row=row, column=col)
    elif text == 'sqrt':
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), 
                  command=square_root).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), 
                  command=lambda val=text: button_click(val)).grid(row=row, column=col)

# Start the Tkinter event loop
root.mainloop()
