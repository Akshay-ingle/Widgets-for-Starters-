import tkinter as tk

def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, f"The product is: {product}")
    except ValueError:
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, "Please enter valid numbers!")

# Create the main window
window = tk.Tk()
window.title("Getting Started with Widgets")
window.geometry("400x300")
window.configure(bg="#f0f8ff")  # Light blue background

# Description label
desc_label = tk.Label(window, text="This application multiplies two numbers.",
                      bg="#f0f8ff", fg="#333366", font=("Arial", 12))
desc_label.pack(pady=10)

# First number label and entry
label1 = tk.Label(window, text="Enter first number:", bg="#f0f8ff", fg="black")
label1.pack()
entry1 = tk.Entry(window, width=20, bg="#e6f2ff")
entry1.pack(pady=5)

# Second number label and entry
label2 = tk.Label(window, text="Enter second number:", bg="#f0f8ff", fg="black")
label2.pack()
entry2 = tk.Entry(window, width=20, bg="#e6f2ff")
entry2.pack(pady=5)

# Button to calculate the product
calc_button = tk.Button(window, text="Calculate Product", command=calculate_product,
                        bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
calc_button.pack(pady=10)

# Text box to display result
result_box = tk.Text(window, height=2, width=30, bg="#fff0f5", fg="black")
result_box.pack(pady=10)

# Run the application
window.mainloop()
