# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 22:26:27 2023

@author: SALVATORE TUTI
"""
import pyomo.environ as pyomo
# Model definition - must be done at the beginning!
model = pyomo.ConcreteModel();

#Variable declaration
model.x1 = pyomo.Var(); # Number of comedy ads purchased
model.x2 = pyomo.Var(); # Number of football ads purchased

# Objective function definition
model.obj = pyomo.Objective(expr = 50*model.x1 + 100*model.x2, sense = pyomo.minimize);

#Constraint definition
def rule1(model):
    return 7*model.x1 + 2*model.x2 >= 28
model.eq1 = pyomo.Constraint(rule = rule1, doc = 'Constraint 1');

def rule2(model):
    return 2*model.x1 + 12*model.x2 >= 24
model.eq2 = pyomo.Constraint(rule = rule2, doc = 'Constraint 2');

# Solver options
# When running in Colab, add the PATH for the solver executable file
results = pyomo.SolverFactory('glpk').solve(model);

# Printing results
results.write()
print("\n RESULTS \n");
print("Cost of advertisement campaign = ",model.obj());
print("Number of comedy ads purchased = ",model.x1());
print("Number of football ads purchased = ",model.x2());