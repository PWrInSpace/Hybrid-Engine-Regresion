from src.Solvers.AbstractSolver import AbstractSolver
import customtkinter # type: ignore


class Solver1(AbstractSolver):
    InputItemList = dict()

    def __init__(self, Controller):
        super().__init__(Controller)

        self.CreateInput()
        self.CreateOutput()
        self.CreateCheckboxFrame()

    def CreateInput(self):
        self.AddInputItem("Force", 0)
        print("Solver1.CreateInput")
    
    def CreateOutput(self):
        self.AddOutput("Impulse", 0)

    def CreateGrahps(self):
        pass

    def ShowGraph(self, GraphName):
        pass

    def CreateCheckboxFrame(self):
        self.AddCheckbox("Force", 0)

    def RunSimulation(self):
        time = [0, 1, 2]
        
        force = int(self.InputItemList["Force"].get())
        forceGraph = [force, 0.7 * force, 0.1*force]
        
        self.SimulationData["Force"] = self.SimulationDataFrame(time, forceGraph)
        

        print("Run() ok")
