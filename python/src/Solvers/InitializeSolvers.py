from src.Solvers.Solver1 import Solver1
from src.Solvers.Solver2 import Solver2

SolverList = ['Solver1', 'Solver2']

def InitializeSolvers(SolverHashmap):
    SolverHashmap['Solver1'] = Solver1
    SolverHashmap['Solver2'] = Solver2

def GetSolverList():
    return SolverList
