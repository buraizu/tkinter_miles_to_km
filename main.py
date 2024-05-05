import tkinter as tk


def calculate_conversion():
    result_label.config(text=f"{int(user_input.get()) * 1.6}")

window = tk.Tk()
window.title("Miles to Km Converter")
window.minsize(width=500, height=300)

miles_label = tk.Label(text="Miles")
miles_label.grid(column=3, row=1)

km_label = tk.Label(text="Km")
km_label.grid(column=3, row=2)

equals_label = tk.Label(text="is equal to")
equals_label.grid(column=1, row=2)

result_label = tk.Label(text="0")
result_label.grid(column=2, row=2)

calculate_button = tk.Button(text="Calculate", command=calculate_conversion)
calculate_button.grid(column=2, row=3)

user_input = tk.Entry(width=10)
user_input.grid(column=2, row=1)

window.mainloop()