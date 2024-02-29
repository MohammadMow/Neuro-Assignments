## Neuroscience Homework 2
This Jupyter Notebook contains the code and analysis for the first homework assignment in the Neuroscience, Learning, Memory, and Cognition course at Sharif University of Technology.

# Generalized Firing-Rate-Based Network Models 
This homework assignment involves simulating a generalized firing-rate based neural network model using Python. The goals are:

- Define parameters for the network model including time constants, presynaptic firing rates, synaptic weights, etc.

- Implement functions to solve the coupled differential equations describing the network dynamics.

- Plot the results to show how the postsynaptic neuron's firing rate evolves over time based on synaptic input from presynaptic neurons.

![plot](https://s8.uupload.ir/files/capture_pesm.jpg)


# Instructions
- Import necessary packages like NumPy, SciPy, and Matplotlib.

- Define a function to set default parameter values that can be overridden. Parameters should include time constants, firing rates vector, weights matrix.

- Implement functions to solve the differential equations numerically using odeint from SciPy. Returns should be synaptic input current and postsynaptic firing rate over time.

- Generate a figure showing the time course of the postsynaptic neuron's firing rate.

- Adjust any parameter values and observe how the dynamics change. Try different synaptic weights configurations.

- Add additional analysis or plots as needed.

