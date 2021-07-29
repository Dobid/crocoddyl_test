import matplotlib
import numpy as np
import matplotlib.pylab as plt
import crocoddyl
from unicycle_utils import plotUnicycle
import inspect
import os

x = np.random.rand(3) # états [pos_x, pos_y, yaw]
u = np.random.rand(2) # commande [lin_vel, ang_vel]

v, w = u
c, s = np.cos(x[2]), np.sin(x[2]) # [composantes x et y du yaw (cap) du robot]
dt = 1e-2 # timestep period
dx = np.array([v * c, v * s, w]) # déplacement après commande : [composante pos_x, composante pos_y, angle yaw]
xnext = x + dx * dt # step : état prochain du systeme au pas de temps prochain

print("x (état) = ", x)
print("cos = ", c)
print("sin = ", s)

print("u (controle) = ", u)
print("v (lin vel)= ", v)
print("w (ang vel) = ", w)

print("dx = ", dx)

stateWeight = 1
ctrlWeight = 1
costResiduals = np.concatenate([stateWeight * x, ctrlWeight * u])
print("costResiduals = ", costResiduals, " ** 2 = ", costResiduals ** 2)
cost = .5 * sum(costResiduals ** 2)
print("cost = ", cost)

model = crocoddyl.ActionModelUnicycle() # pas trouvé où est la fonction (notebook peut etre pas à jour), unicycle.py introuvable
data = model.createData()
print(os.path.abspath(inspect.getfile(crocoddyl.ActionModelUnicycle)))
print(os.path.abspath(inspect.getfile(crocoddyl.ActionModelUnicycle.createData)))