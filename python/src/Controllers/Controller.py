import tkinter as tk
import tkinter.messagebox
import customtkinter # type: ignore
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from src.Solvers.AbstractSolver import AbstractSolver
from src.Solvers.Solver1 import Solver1
from src.Solvers.InitializeSolvers import InitializeSolvers
from src.Solvers.InitializeSolvers import GetSolverList

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class Controller(customtkinter.CTk):
    SolverHashMap = dict()
    OperationHashmap = dict()
    OperationCurrent = None
    
    def __init__(self):
        super().__init__()
        self.state('normal')
        InitializeSolvers(self.SolverHashMap)

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

        self.OperationItemList = customtkinter.CTkComboBox(self.sidebar_frame, values=[], command=self.OperationSelectAction)
        self.OperationItemList.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")
        self.OperationItemList.set("Set Operation")

        self.SidebarButtonAdd = customtkinter.CTkButton(self.sidebar_frame, command=self.ButtonAddOperationAction, text="Add")
        self.SidebarButtonAdd.grid(row=3, column=0, padx=20, pady=10)
        self.SidebarButtonDelete = customtkinter.CTkButton(self.sidebar_frame, command=self.ButtonDeleteOperationAction, text="Delete")
        self.SidebarButtonDelete.grid(row=3, column=1, padx=20, pady=10)


        # create Graph
        self.graph_frame = customtkinter.CTkFrame(self, width=250)
        self.graph_frame.grid(row=0, column=1, rowspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
    

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
        
    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def ButtonAddOperationAction(self):
        solverType = None
        operationName = None

        self.OperationCreationPopUp(solverType, operationName)

    def OperationCreationPopUp(self, solverType, operationName):
        self.popup = tk.Toplevel(self.master, bg="#303030")
        self.popup.title("Create Operation")
        self.popup.geometry(f"{180}x{200}")

        # Combobox
        self.solverTypeLabel = customtkinter.CTkLabel(self.popup, text="Choose Operation:")
        self.solverTypeLabel.pack()
        self.solverTypeCombo = customtkinter.CTkComboBox(self.popup, values=GetSolverList())
        self.solverTypeCombo.set(GetSolverList()[0])
        self.solverTypeCombo.pack()


        self.operationNameLabel = customtkinter.CTkLabel(self.popup, text="Operation name:")
        self.operationNameLabel.pack()
        self.operationNameEntry = customtkinter.CTkEntry(self.popup)
        self.operationNameEntry.pack()

        # Use a lambda to defer the execution of ClosePopup
        self.okButton = customtkinter.CTkButton(self.popup, text="OK", command=lambda: self.ClosePopup(solverType, operationName))
        self.okButton.pack()

    def ClosePopup(self, solverType, operationName):
        solverType = self.solverTypeCombo.get()
        operationName = self.operationNameEntry.get()

        self.popup.destroy()

        print(solverType)
        print(operationName)
        
        SolverClassTemp = self.SolverHashMap[solverType]

        currentVal = self.OperationItemList.cget("values")
        if operationName not in currentVal:
            currentVal.append(operationName)
            self.OperationItemList.configure(values=currentVal)

        if self.OperationCurrent != None:
            self.OperationCurrent.DeleteInput()
            self.OperationCurrent.DeleteCanvas()

        self.OperationCurrent = SolverClassTemp(self)

        self.OperationHashmap[operationName] = self.OperationCurrent
        self.OperationItemList.set(operationName)
        

    def ButtonDeleteOperationAction(self):
        self.OperationCurrent.DeleteInput()
        

    def ButtonGenerateAction(self):
        self.OperationCurrent.RunSimulation()

    def OperationSelectAction(self, event):
        value = self.OperationItemList.get()
        print(f"New selection: {value}")

        self.OperationCurrent.DeleteCanvas()
        self.OperationCurrent.DeleteInput()
        self.OperationCurrent = self.OperationHashmap[value]
        
        self.OperationCurrent.CreateInput()
        self.OperationCurrent.CreateOutput()
        self.OperationCurrent.CreateCanvas()



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
            print("help")
            self.textbox.insert("insert", "\n\nAvailable commands:\n\n")
            self.textbox.insert("insert", "help - display this message\n")
