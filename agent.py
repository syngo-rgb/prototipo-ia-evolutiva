import numpy as np

class Agent:
    def __init__(self, input_size=8, brain=None):
        self.input_size = input_size
        self.brain = brain if brain is not None else np.random.randn(2, input_size) * 0.1
        self.position = np.zeros(2)
        self.velocity = np.zeros(2)
        self.fitness = 0
        self.alive = True
        self.glow_timer = 0

    def act(self, inputs):
        output = np.dot(self.brain, inputs)
        self.velocity += output
        speed_limit = 5
        speed = np.linalg.norm(self.velocity)
        if speed > speed_limit:
            self.velocity = self.velocity / speed * speed_limit
        self.position += self.velocity

    def mutate(self, rate=0.1):
        mutation = (np.random.randn(*self.brain.shape) * rate)
        self.brain += mutation

    @staticmethod
    def crossover(parent1, parent2):
        mask = np.random.rand(*parent1.brain.shape) > 0.5
        child_brain = np.where(mask, parent1.brain, parent2.brain)
        return child_brain

