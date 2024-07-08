from src.Solvers.AbstractSolver import AbstractSolver
import customtkinter # type: ignore


class Solver1(AbstractSolver):

    def __init__(self, Controller):
        self.Controller = Controller
        self.CreateInput()
        self.CreateOutput()

    def CreateInput(self):
        self.AddInputItem("Force", 0)
    
    def CreateOutput(self):
        self.AddOutput("Impulse", 0)

    def CreateGrahps(self):
        pass

    def ShowGraph(self, GraphName):
        pass

    def RunSimulation(self):
        pass