from AbstractSolver import AbstractSolver
import customtkinter # type: ignore
from python.src.Controllers.Controller import Controller


class Solver1(AbstractSolver):
    Controller = None

    def __init__(self, Controller):
        self.Controller = Controller

    def CreateInput(self):
        
        ScrollTempLabel = customtkinter.CTkLabel(self.scrollable_frame, text=f"InputData {i}") 
        ScrollTempLabel.grid(row=i, column=0, padx=10, pady=10, sticky="w")
        Controller.SidebarInputItemList.append(ScrollTempLabel)

        ScrollTempEntry = customtkinter.CTkEntry(self.scrollable_frame)
        ScrollTempEntry.grid(row=i, column=1, padx=10, pady=10, sticky="w")
        Controller.SidebarInputItemList.append(ScrollTempEntry)