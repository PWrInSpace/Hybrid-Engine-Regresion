import tkinter as tk
import tkinter.messagebox
import customtkinter # type: ignore
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from src.Solvers.AbstractSolver import AbstractSolver
from src.Solvers.Solver1 import Solver1

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class Controller(customtkinter.CTk):
    OperationHashmap = dict()
    OperationCurrent = None
    
    def __init__(self):
        super().__init__()
        self.state('normal')

    def run(self):

        # configure window
        self.title("Rocket Engine Simulation Platform")
        self.geometry(f"{1100}x{580}")

        # Create a menu bar
        menubar = tk.Menu(self)

        # Create a File menu and add it to the menu bar
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New")
        filemenu.add_command(label="Open")
        filemenu.add_command(label="Save")
 
        menubar.add_cascade(label="File", menu=filemenu)

        # Create an Edit menu and add it to the menu bar
        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo")
        editmenu.add_command(label="Redo")

        menubar.add_cascade(label="Edit", menu=editmenu)

        # Display the menu bar
        self.config(menu=menubar)

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure(0, minsize=300)  # set the minimum width of the 0th column to 200 pixels

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=300, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.sidebar_frame.grid_columnconfigure(0, weight=1)
        self.sidebar_frame.grid_columnconfigure(1, weight=1)  # make the 1st column take up any extra space

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="RESP", font=customtkinter.CTkFont(size=20, weight="bold"), anchor="center")
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 20), sticky="nsew")

        self.SidebarButtonGenerate = customtkinter.CTkButton(self.sidebar_frame, command=self.ButtonGenerateAction, text="Generate")
        self.SidebarButtonGenerate.grid(row=1, column=0, padx=20, pady=10)

        self.OperationItemList = tk.Listbox(self.sidebar_frame)
        self.OperationItemList.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")


        self.SidebarButtonAdd = customtkinter.CTkButton(self.sidebar_frame, command=self.ButtonAddOperationAction, text="Add")
        self.SidebarButtonAdd.grid(row=3, column=0, padx=20, pady=10)
        self.SidebarButtonDelete = customtkinter.CTkButton(self.sidebar_frame, command=self.ButtonDeleteOperationAction, text="Delete")
        self.SidebarButtonDelete.grid(row=3, column=1, padx=20, pady=10)



        # create textbox
        # self.textbox = customtkinter.CTkTextbox(self, width=250)
        # self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # create Graph
        self.graph_frame = customtkinter.CTkFrame(self, width=250)
        self.graph_frame.grid(row=0, column=1, rowspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")

        fig = plt.Figure()
        ax = fig.add_subplot(111)

        x = [1, 2, 3, 4, 5]
        y = [10, 20, 55, 30, 20]

        ax.plot(x, y, linestyle='-', color='grey', marker='o')
        ax.set_title("Force Graph")

        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.get_tk_widget().pack(side='top', fill='both', expand=True)
        canvas.draw()


        # self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Tab 2"), text="CTkLabel on Tab 2")
        # self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)
        

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=2, rowspan=2, column=1, padx=(20, 0), pady=20, sticky="nsew")
        self.textbox.configure()

        # insert the initial text symbol
        self.textbox.insert("end", "Welcome to RESP terminal. For help insert: help")

        # create input for textbox
        self.inputTerminal = customtkinter.CTkEntry(self)
        self.inputTerminal.grid(row=4, rowspan=1, column=1, padx=(20, 0), pady=20, sticky="nsew")
        self.inputTerminal.bind("<Return>", self.on_return)

        # create scrollable frame
        self.InputFrame = customtkinter.CTkScrollableFrame(self, label_text="Input Frame", corner_radius=0)
        self.InputFrame.grid(row=1, column=0, rowspan=3, sticky="nsew")
        self.InputFrame.grid_columnconfigure(0, weight=0)

        '''
        for i in range(100):
            ScrollTempLabel = customtkinter.CTkLabel(self.InputFrame, text=f"InputData {i}") 
            ScrollTempLabel.grid(row=i, column=0, padx=10, pady=10, sticky="w")
            self.SidebarInputItemList.append(ScrollTempLabel)

            ScrollTempEntry = customtkinter.CTkEntry(self.InputFrame)
            ScrollTempEntry.grid(row=i, column=1, padx=10, pady=10, sticky="w")
            self.SidebarInputItemList.append(ScrollTempEntry)
        '''

        # create scrollable frame for checkbox graphs
        self.ScrollableFrameGraphChekcbox = customtkinter.CTkScrollableFrame(self, label_text="Graph Checkbox", corner_radius=0, width=250, height=250)
        self.ScrollableFrameGraphChekcbox.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.ScrollableGraphList = []
        for i in range(10):
            ScrollTempCheckbox = customtkinter.CTkCheckBox(self.ScrollableFrameGraphChekcbox)
            ScrollTempCheckbox.grid(row=i, column=0, padx=10, pady=10, sticky="w")
            self.ScrollableGraphList.append(ScrollTempCheckbox)

        # create scrollable frame for output data
        self.ScrollableFrameOutput = customtkinter.CTkScrollableFrame(self, label_text="Output Data", corner_radius=0, width=250)
        self.ScrollableFrameOutput.grid(row=1, column=2, rowspan=3, padx=(20, 0), pady=(0, 20), sticky="nsew")
        
        '''
        self.ScrollableOutputList = []
        for i in range(10):
            ScrollTempLabel = customtkinter.CTkLabel(self.ScrollableFrameOutput, text=f"OutputData {i}") 
            ScrollTempLabel.grid(row=i, column=0, padx=10, pady=10, sticky="w")
            self.ScrollableOutputList.append(ScrollTempLabel)
        '''
        # set default values
        #self.optionmenu_1.set("CTkOptionmenu")
        #self.combobox_1.set("CTkComboBox")

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def ButtonAddOperationAction(self):
        self.OperationCurrent = Solver1(self)
        self.OperationItemList.insert(tk.END, "Solver1")
        
        self.OperationHashmap['Skib'] = self.OperationCurrent

    def ButtonDeleteOperationAction(self):
        pass

    def ButtonGenerateAction(self):
        self.OperationCurrent.RunSimulation()

    def on_return(self, event):
        command = ""
        # get the command and strip the newline character from the end
        command = self.inputTerminal.get()
        self.inputTerminal.delete(0, "end")
        self.textbox.insert("insert", command)

        # check the command and act on it
        self.check_command(command)


    def check_command(self, command):
        # check the command and act on it
        print(command)
        if command == "help":
            print("SUCC")
            self.textbox.insert("insert", "\n\nAvailable commands:\n\n")
            self.textbox.insert("insert", "help - display this message\n")