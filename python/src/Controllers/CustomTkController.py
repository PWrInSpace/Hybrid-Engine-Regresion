import tkinter as tk
import tkinter.messagebox
import customtkinter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CustomTkinter complex_example.py")
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

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="CustomTkinter", font=customtkinter.CTkFont(size=20, weight="bold"), anchor="center")
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 20), sticky="nsew")

        self.SidebarButtonGenerate = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, text="Generate")
        self.SidebarButtonGenerate.grid(row=1, column=0, padx=20, pady=10)

        self.OperationItemList = tk.Listbox(self.sidebar_frame)
        self.OperationItemList.insert(1, "MyProject")
        self.OperationItemList.insert(2, "MyAnalysis")
        self.OperationItemList.insert(3, "MyComparison")
        self.OperationItemList.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")


        self.SidebarButtonAdd = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, text="Add")
        self.SidebarButtonAdd.grid(row=3, column=0, padx=20, pady=10)
        self.SidebarButtonDelete = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, text="Delete")
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
        ax.set_title("CTkGraph")

        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.get_tk_widget().pack(side='top', fill='both', expand=True)
        canvas.draw()


        '''
        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("CTkTabview")
        self.tabview.add("Tab 2")
        self.tabview.add("Tab 3")
        self.tabview.tab("CTkTabview").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)

        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("CTkTabview"), dynamic_resizing=False,
                                                        values=["Value 1", "Value 2", "Value Long Long Long"])
        self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.combobox_1 = customtkinter.CTkComboBox(self.tabview.tab("CTkTabview"),
                                                    values=["Value 1", "Value 2", "Value Long....."])
        self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("CTkTabview"), text="Open CTkInputDialog",
                                                           command=self.open_input_dialog_event)
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Tab 2"), text="CTkLabel on Tab 2")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)
        '''

        # create textbox
        self.textbox = tk.Text(self, width=250)
        self.textbox.grid(row=2, rowspan=2, column=1, padx=(20, 0), pady=20, sticky="nsew")

        # bind the Return key to the on_return function
        self.textbox.bind("<Return>", self.on_return)

        # insert the initial "> " symbol
        self.textbox.insert("end", "> ")

        # make the initial "> " symbol read-only
        self.textbox.mark_set("insert", "end")
        self.textbox.bind("<Key>", lambda e: "break")

        # create scrollable frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="Input Frame", corner_radius=0)
        self.scrollable_frame.grid(row=1, column=0, rowspan=3, sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=0)
        self.SidebarInputItemList = []
        for i in range(100):
            ScrollTempLabel = customtkinter.CTkLabel(self.scrollable_frame, text=f"InputData {i}") 
            ScrollTempLabel.grid(row=i, column=0, padx=10, pady=10, sticky="w")
            self.SidebarInputItemList.append(ScrollTempLabel)

            ScrollTempEntry = customtkinter.CTkEntry(self.scrollable_frame)
            ScrollTempEntry.grid(row=i, column=1, padx=10, pady=10, sticky="w")
            self.SidebarInputItemList.append(ScrollTempEntry)

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
        self.ScrollableOutputList = []
        for i in range(10):
            ScrollTempLabel = customtkinter.CTkLabel(self.ScrollableFrameOutput, text=f"OutputData {i}") 
            ScrollTempLabel.grid(row=i, column=0, padx=10, pady=10, sticky="w")
            self.ScrollableOutputList.append(ScrollTempLabel)

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

    def sidebar_button_event(self):
        print("sidebar_button click")

    def on_return(self, event):
        command = ""
        # get the command and strip the newline character from the end
        command = self.textbox.get("insert linestart", "insert lineend").rstrip("\n")

        # check the command and act on it
        self.check_command(command)

        # insert the "> " symbol at the end of the textbox
        self.textbox.insert("end", "\n> ")

        # make the previous commands and the "> " symbol read-only
        self.textbox.mark_set("insert", "end")

        # remove the "<Key>" binding
        self.textbox.unbind("<Key>")

        # reapply the "<Key>" binding before the user starts typing
        self.textbox.after(1, lambda: self.textbox.bind("<Key>", self.on_key))

        # prevent the default Return key action
        return "break"
    
    def on_key(self, event):
        # if the insertion cursor is in the read-only part of the textbox, ignore the key press
        if self.textbox.index("insert") < self.textbox.index("end-1c"):
            return "break"


    def check_command(self, command):
        # check the command and act on it
        print(command)
        if command == "> help":
            print("SUCC")
            self.textbox.insert("insert", "\n\nAvailable commands:\n\n")
            self.textbox.insert("insert", "help - display this message\n")


if __name__ == "__main__":
    app = App()
    app.mainloop()