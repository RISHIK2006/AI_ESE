import numpy as np

def random_mlp_two_hidden_layers(n_inputs, n_hidden1, n_hidden2, n_outputs, n_steps):
    W1 = None
    b1 = None
    W2 = None
    b2 = None
    W_out = None
    b_out = None

    for step in range(n_steps):
        print(f"\n--- Step {step + 1} ---")

        # Randomize weights and biases
        W1 = np.random.rand(n_inputs, n_hidden1)
        b1 = np.random.rand(1, n_hidden1)

        W2 = np.random.rand(n_hidden1, n_hidden2)
        b2 = np.random.rand(1, n_hidden2)

        W_out = np.random.rand(n_hidden2, n_outputs)
        b_out = np.random.rand(1, n_outputs)

        # Display them
        print("Weight Matrix W1:\n", W1)
        print("Bias Vector b1:\n", b1)
        print("Weight Matrix W2:\n", W2)
        print("Bias Vector b2:\n", b2)
        print("Weight Matrix W_out:\n", W_out)
        print("Bias Vector b_out:\n", b_out)

    return W1, b1, W2, b2, W_out, b_out, n_steps


# === Setup for your 2 hidden layer network ===
n_inputs = 2
n_hidden1 = 3
n_hidden2 = 2
n_outputs = 1
n_steps = 5  # or more if needed

# Run
W1, b1, W2, b2, W_out, b_out, steps = random_mlp_two_hidden_layers(n_inputs, n_hidden1, n_hidden2, n_outputs, n_steps)

# === Final output ===
print("\n--- Final Results ---")
print("Final Weight Matrix W1:\n", W1)
print("Final Bias Vector b1:\n", b1)
print("Final Weight Matrix W2:\n", W2)
print("Final Bias Vector b2:\n", b2)
print("Final Weight Matrix W_out:\n", W_out)
print("Final Bias Vector b_out:\n", b_out)
print("Number of Steps:", steps)