import numpy as np
from agent import Agent

class Environment:
    def __init__(self, width=600, height=600, n_food=50, n_agents=20):
        self.width = width
        self.height = height
        self.n_food = n_food
        self.n_agents = n_agents
        self.food_positions = []
        self.agents = []

    def reset(self):
        self.food_positions = [np.random.rand(2) * [self.width, self.height] for _ in range(self.n_food)]
        self.agents = []
        for _ in range(self.n_agents):
            agent = Agent(input_size=8)  # input_size corregido a 8
            agent.position = np.random.rand(2) * [self.width, self.height]
            agent.velocity = np.zeros(2)
            agent.fitness = 0
            agent.alive = True
            self.agents.append(agent)

    def reset_food(self):
        self.food_positions = [np.random.rand(2) * [self.width, self.height] for _ in range(self.n_food)]

    def step(self):
        for agent in self.agents:
            if not agent.alive:
                continue

            if len(self.food_positions) == 0:
                continue

            closest_food = min(self.food_positions, key=lambda food: np.linalg.norm(agent.position - food))
            direction = (closest_food - agent.position)
            norm = np.linalg.norm(direction)
            direction = direction / norm if norm > 0 else np.zeros(2)

            inputs = np.concatenate([
                direction,
                [agent.position[0] / self.width, agent.position[1] / self.height],
                [1.0 - agent.position[0] / self.width, 1.0 - agent.position[1] / self.height],
                agent.velocity / 10
            ])  # Total 8 inputs

            agent.act(inputs)

            # Desactivamos agente si sale del área
            if agent.position[0] < 0 or agent.position[0] > self.width or \
               agent.position[1] < 0 or agent.position[1] > self.height:
                agent.alive = False
                continue

            # Verificamos si come comida
            for i, food in enumerate(self.food_positions):
                if np.linalg.norm(agent.position - food) < 10:
                    agent.fitness += 1
                    agent.glow_timer = 10
                    self.food_positions.pop(i)
                    break

