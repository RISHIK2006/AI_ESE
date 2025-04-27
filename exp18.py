import numpy as np

def random_mlp(n_inputs, n_hidden, n_outputs, n_steps):
    W1 = None
    b1 = None
    W_out = None
    b_out = None
    
    for step in range(n_steps):
        print(f"Step {step + 1}: ")
        
        W1 = np.random.rand(n_inputs, n_hidden)
        b1 = np.random.rand(1, n_hidden)
        W_out = np.random.rand(n_hidden, n_outputs)
        b_out = np.random.rand(1, n_outputs)
        
        print("Weight Matrix W1: ", W1)
        print("Bias Vector b1: ", b1)
        print("Weight Matrix W_out: ", W_out)
        print("Bias Vector b_out: ", b_out)
        
    return W1, b1, W_out, b_out, n_steps
        

n_inputs = 4
n_hidden = 5
n_outputs = 2
n_steps = 5


W1, b1, W_out, b_out, n_steps = random_mlp(n_inputs, n_hidden, n_outputs, n_steps)

print("Final Weight Matrix W1: ", W1)
print("Final Bias Vector b1: ", b1)
print("Final Weight Matrix W_out: ", W_out)
print("Final Bias Vector b_out: ", b_out)
print("No. of steps: ", n_steps)
