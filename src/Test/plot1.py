import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

# Function to plot the graph
def plot():
    # Generate data
    x = [0, 1, 2]
    y = [random.random() % 5 for _ in x]
    
    # Clear the figure
    fig.clear()

    # Create a new plot
    ax = fig.add_subplot(111)
    ax.plot(x, y, marker='o', linestyle='-')
    ax.set_title('f(x) = random() % 5')
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Draw the canvas
    canvas.draw()

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

# Create a button to plot the data
plot_button = ttk.Button(root, text="Plot", command=plot)
plot_button.pack()

# Run the Tkinter main loop
root.mainloop()

