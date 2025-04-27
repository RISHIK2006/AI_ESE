import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

def train_mlp(n_inputs, n_hidden1, n_hidden2, learning_rate, n_steps, training_data):
    W1 = np.random.rand(n_inputs, n_hidden1)
    b1 = np.random.rand(1, n_hidden1)
    W2 = np.random.rand(n_hidden1, n_hidden2)
    b2 = np.random.rand(1, n_hidden2)
    W_out = np.random.rand(n_hidden2, 1)
    b_out = np.random.rand(1, 1)

    for step in range(n_steps):
        input_vector, target = training_data[np.random.randint(len(training_data))]
        input_vector = input_vector.reshape(1, -1)
        target = np.array([[target]])

        # Forward
        h1 = sigmoid(np.dot(input_vector, W1) + b1)
        h2 = sigmoid(np.dot(h1, W2) + b2)
        output = sigmoid(np.dot(h2, W_out) + b_out)

        # Backward
        error = target - output
        d_output = error * sigmoid_derivative(output)

        d_h2 = d_output.dot(W_out.T) * sigmoid_derivative(h2)
        d_h1 = d_h2.dot(W2.T) * sigmoid_derivative(h1)

        # Update
        W_out += h2.T.dot(d_output) * learning_rate
        b_out += np.sum(d_output, axis=0, keepdims=True) * learning_rate
        W2 += h1.T.dot(d_h2) * learning_rate
        b2 += np.sum(d_h2, axis=0, keepdims=True) * learning_rate
        W1 += input_vector.T.dot(d_h1) * learning_rate
        b1 += np.sum(d_h1, axis=0, keepdims=True) * learning_rate

    return W1, b1, W2, b2, W_out, b_out, n_steps


n_inputs = 2
n_hidden1 = 3
n_hidden2 = 2
learning_rate = 0.1
n_steps = 5

training_data = [
    (np.array([0, 0]), 0),
    (np.array([0, 1]), 0),
    (np.array([1, 0]), 0),
    (np.array([1, 1]), 1)
]

W1, b1, W2, b2, W_out, b_out, steps = train_mlp(
    n_inputs, n_hidden1, n_hidden2, learning_rate, n_steps, training_data
)

print("\n--- Final Results ---")
print("Final Weight Matrix W1:\n", W1)
print("Final Bias Vector b1:\n", b1)
print("Final Weight Matrix W2:\n", W2)
print("Final Bias Vector b2:\n", b2)
print("Final Weight Matrix W_out:\n", W_out)
print("Final Bias Vector b_out:\n", b_out)
print("Number of Training Steps:", steps)