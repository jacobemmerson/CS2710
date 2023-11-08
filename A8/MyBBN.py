#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pgmpy.factors.discrete import TabularCPD
from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination
import pickle
import networkx as nx
import matplotlib.pyplot as plt



# Step 1: Define the structure of the Bayesian Network
model = BayesianNetwork([("CovidContact",'Covid'),
                         ('Covid', 'RunnyNose'),
                         ('Covid', 'NoTaste'),
                         ('Covid', 'MuscleAches'),
                         ('Cold', 'RunnyNose'),
                         ('Cold', 'NoTaste'),
                         ('Cold', 'MuscleAches')])

# Step 2: Define the parameters (CPDs) of the Bayesian Network
cpd_CovidContact = TabularCPD(variable = "CovidContact",
                              variable_card = 2,
                              values = [[0.95],[0.05]]
                              )

cpd_Cold = TabularCPD(variable="Cold",
                      variable_card = 2,
                      values = [[0.90],[0.10]]
                      )

cpd_Covid = TabularCPD(variable = "Covid",
                       variable_card=2,
                       values = [[0.70, 0.10], [0.30, 0.90]],
                       evidence = ['CovidContact'],
                       evidence_card = [2]
                       )

cpd_RunnyNose = TabularCPD(variable = "RunnyNose",
                       variable_card=2,
                       values = [[0.98, 0.90, 0.75, 0.05], [0.02, 0.10, 0.25, 0.95]],
                       evidence = ['Covid', 'Cold'],
                       evidence_card = [2, 2]
                       )

cpd_NoTaste = TabularCPD(variable = "NoTaste",
                       variable_card=2,
                       values = [[0.60, 0.50, 0.02, 0.01], [0.40, 0.50, 0.98, 0.99]],
                       evidence = ['Covid', 'Cold'],
                       evidence_card = [2, 2]
                       )

cpd_MuscleAches = TabularCPD(variable = "MuscleAches",
                       variable_card=2,
                       values = [[0.40, 0.30, 0.10, 0.05], [0.60, 0.70, 0.90, 0.95]],
                       evidence = ['Covid', 'Cold'],
                       evidence_card = [2, 2]
                       )


# Step 3: Add the parameters to the model
model.add_cpds(cpd_CovidContact, cpd_Cold, cpd_Covid, cpd_RunnyNose, cpd_NoTaste, cpd_MuscleAches)

# Step 4: Validate the model
assert model.check_model()

# Step 1: Store model
with open('my_bayesian_network_model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Step 2: Load model
with open('my_bayesian_network_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)
    
    
        
# Visualize the Bayesian Network
G = nx.DiGraph()
G.add_edges_from(model.edges())
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos, with_labels=True, node_size=800, node_color='skyblue')
nx.draw_networkx_labels(G, pos)
plt.show()

# variable elimination algorithm
# Step 1: Initialize the Variable Elimination method
ve_infer = VariableElimination(model)

# Step 2: Query the Bayesian Network to find the conditional probability of 'Earthquake' given that 'JohnCalls is True and MaryCall is True
results = [
    ve_infer.query(variables = ["Covid"],
                   evidence = {'Cold' : 1}),
    ve_infer.query(variables = ["Covid"],
                   evidence = {'NoTaste':1, 'MuscleAches':1, 'CovidContact':1}),
    ve_infer.query(variables = ["Covid"],
                   evidence = {'RunnyNose':0, 'NoTaste':1, 'MuscleAches':0}),
    ve_infer.query(variables = ["Cold"],
                   evidence = {'RunnyNose':1, 'MuscleAches':1, 'CovidContact':1}),
    ve_infer.query(variables = ["NoTaste"],
                   evidence = {'Covid' : 0, 'Cold' : 1, 'CovidContact' : 1}),
    ve_infer.query(variables = ["MuscleAches"],
                   evidence = {'Covid' : 1, 'Cold' : 1, 'RunnyNose' : 1})
]

for r in results:
    print(r)
    print("")


