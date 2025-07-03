import numpy as np
import random


class QLearningAgent:
    def __init__(self, road_length=5, actions=None, episodes=1000, alpha=0.8, gamma=0.9, epsilon=0.3):
        self.road_length = road_length
        self.actions = actions if actions else ["left", "right"]
        self.num_actions = len(self.actions)
        self.Q = np.zeros((self.road_length, self.num_actions))
        self.episodes = episodes
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def select_action(self, state):
        if random.random() < self.epsilon:
            return random.randint(0, self.num_actions - 1)  # Explore
        return np.argmax(self.Q[state])  # Exploit

    def take_action(self, state, action):
        if self.actions[action] == "left":
            return max(0, state - 1)
        elif self.actions[action] == "right":
            return min(self.road_length - 1, state + 1)
        else:
            raise ValueError(f"Invalid action: {action}")

    def reward(self, state):
        return 1 if state == self.road_length - 1 else 0

    def train(self):
        for episode in range(self.episodes):
            state = 0  # Start
            while state != self.road_length - 1:
                action = self.select_action(state)
                next_state = self.take_action(state, action)
                r = self.reward(next_state)

                # Q-learning update rule
                best_next_q = np.max(self.Q[next_state])
                self.Q[state, action] += self.alpha * (r + self.gamma * best_next_q - self.Q[state, action])
                state = next_state

    def test_policy(self):
        state = 0
        steps = 0
        path = []
        print("\n🚗 Agent's path to goal:")
        while state != self.road_length - 1:
            action = np.argmax(self.Q[state])
            direction = self.actions[action]
            path.append(direction)
            state = self.take_action(state, action)
            steps += 1
            print(f"Step {steps}: Move {direction} → Position {state}")
        print(f"\n✅ Final path: {' → '.join(path)}")
        print(f"🎯 Goal reached in {steps} steps!")

    def display_q_table(self):
        print("\n🧠 Learned Q-table:")
        print(pd.DataFrame(self.Q, columns=self.actions))


if __name__ == "__main__":
    import pandas as pd

    agent = QLearningAgent()
    agent.train()
    agent.display_q_table()
    agent.test_policy()
