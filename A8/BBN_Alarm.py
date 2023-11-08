#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 18:05:32 2023

@author: milos
"""



from pgmpy.factors.discrete import TabularCPD
from pgmpy.models import BayesianNetwork
import pickle
import networkx as nx
import matplotlib.pyplot as plt



# Step 1: Define the structure of the Bayesian Network
model = BayesianNetwork([("Burglary",'Alarm'),
                         ('Earthquake', 'Alarm'),
                         ('Earthquake', 'RadioReport'),
                         ('Alarm', 'JohnCalls'),
                         ('Alarm', 'MaryCalls')])

# Step 2: Define the parameters (CPDs) of the Bayesian Network
cpd_Burglary = TabularCPD(variable='Burglary', variable_card=2, values=[[0.999], [0.001]])
cpd_Earthquake = TabularCPD(variable='Earthquake', variable_card=2, values=[[0.998], [0.002]])
cpd_Alarm = TabularCPD(variable='Alarm', variable_card=2, values=[[0.999, 0.71, 0.06, 0.05],[0.001, 0.29, 0.94, 0.95]],
                       evidence=['Burglary', 'Earthquake'], evidence_card=[2, 2])
cpd_RadioReport = TabularCPD(variable='RadioReport', variable_card=2, values=[[0.95, 0.01], [0.05, 0.99]],
                             evidence=['Earthquake'], evidence_card=[2])
cpd_JohnCalls = TabularCPD(variable='JohnCalls', variable_card=2, values=[[0.95, 0.1], [0.05, 0.9]],
                             evidence=['Alarm'], evidence_card=[2])
cpd_MaryCalls = TabularCPD(variable='MaryCalls', variable_card=2, values=[[0.99, 0.3], [0.01, 0.7]],
                             evidence=['Alarm'], evidence_card=[2])

# Step 3: Add the parameters to the model
model.add_cpds(cpd_Burglary, cpd_Earthquake, cpd_Alarm, cpd_RadioReport, cpd_JohnCalls, cpd_MaryCalls)

# Step 4: Validate the model
assert model.check_model()

# Step 1: Store model
with open('bayesian_network_model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Step 2: Load model
with open('bayesian_network_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)
    
    
        
# Visualize the Bayesian Network
G = nx.DiGraph()
G.add_edges_from(model.edges())
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos, with_labels=True, node_size=800, node_color='skyblue')
nx.draw_networkx_labels(G, pos)
plt.show()

# variable elimination algorithm

from pgmpy.inference import VariableElimination

# Step 1: Initialize the Variable Elimination method
ve_infer = VariableElimination(model)

# Step 2: Query the Bayesian Network to find the conditional probability of 'Earthquake' given that 'JohnCalls is True and MaryCall is True
result = ve_infer.query(variables=['Earthquake'], evidence={"MaryCalls":1, "JohnCalls":1})
print(result)



