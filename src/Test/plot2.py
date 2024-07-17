import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

# Create the main window
root = tk.Tk()
root.title("Tkinter and Matplotlib Example")

# Create a frame for the plot
frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, expand=1)

# Create a Matplotlib figure and attach it to the Tkinter canvas
fig = plt.Figure()
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1)


ax = fig.add_subplot(111)
ax.set_title('f(x) = random() % 5')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')


click_count = 0
lines = []

# Function to plot the graph
def plot():
    global click_count
    click_count += 1
    
    # Generate data
    x = [0, 1, 2]
    y = [random.random() % 5 for _ in x]

    line, = ax.plot(x, y, marker='o', linestyle='-', label=f'Plot {click_count}')
    lines.append(line)

    ax.legend()

    canvas.draw()

def delete():
    if lines:
        line = lines.pop(0)
        line.remove()
        ax.legend()
        canvas.draw()



plot_button = ttk.Button(root, text="Plot", command=plot)
plot_button.pack()

delete_button = ttk.Button(root, text="Delete First Plot", command=delete)
delete_button.pack()
# Run the Tkinter main loop
root.mainloop()

