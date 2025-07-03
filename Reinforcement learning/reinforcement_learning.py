# Reinforcement Learning (RL) - Q-Learning Example

import numpy as np
import random

# -------------------------------
# Environment Setup
# -------------------------------
n_positions = 5  # Positions: 0 (start) to 4 (goal)
actions = ["left", "right"]
n_actions = len(actions)

# Initialize Q-table: shape (state, action)
Q = np.zeros((n_positions, n_actions))

# -------------------------------
# Hyperparameters
# -------------------------------
episodes = 1000           # Number of training episodes
learning_rate = 0.8       # Learning rate (alpha)
gamma = 0.9               # Discount factor
epsilon = 0.3             # Exploration rate (epsilon)

# -------------------------------
# Training Phase
# -------------------------------
for episode in range(episodes):
    state = random.randint(0, n_positions - 2)  # Start anywhere except goal

    while state != n_positions - 1:  # Until the agent reaches the goal
        # Epsilon-greedy action selection
        if random.uniform(0, 1) < epsilon:
            action = random.randint(0, n_actions - 1)  # Explore
        else:
            action = np.argmax(Q[state])  # Exploit

        # Simulate environment step
        if action == 0:  # Move left
            next_state = max(0, state - 1)
        else:  # Move right
            next_state = min(n_positions - 1, state + 1)

        # Define rewards
        reward = 10 if next_state == n_positions - 1 else -1

        # Q-learning update
        Q[state, action] += learning_rate * (
            reward + gamma * np.max(Q[next_state]) - Q[state, action]
        )

        # Move to next state
        state = next_state

# -------------------------------
# Display Learned Q-table
# -------------------------------
print("Learned Q-table:")
print(Q)

# -------------------------------
# Testing Phase
# -------------------------------
print("\nTesting trained agent:")
state = 0
steps = 0
path = [state]

while state != n_positions - 1:
    action = np.argmax(Q[state])
    if action == 0:
        next_state = max(0, state - 1)
    else:
        next_state = min(n_positions - 1, state + 1)

    print(f"Step {steps}: Position {state} → Action: {actions[action]} → Next: {next_state}")
    state = next_state
    path.append(state)
    steps += 1

print(f"\nAgent reached the goal in {steps} steps.")
print(f"Path taken: {' → '.join(map(str, path))}")
