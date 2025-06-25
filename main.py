import pygame
import numpy as np
import random
from environment import Environment
from agent import Agent

POPULATION = 20
GENERATIONS = 50
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

COLORS = {
    "bg": (240, 240, 240),
    "agent": (50, 100, 200),
    "food": (255, 100, 0),
    "text": (0, 0, 0),
    "border": (100, 100, 100),
    "glow": (0, 255, 0)
}

def draw_text(screen, text, size, x, y):
    font = pygame.font.SysFont('Arial', size)
    surf = font.render(text, True, COLORS["text"])
    screen.blit(surf, (x, y))

def draw_agent(screen, agent, max_fitness):
    pos = agent.position.astype(int)
    puntaje = agent.fitness
    size = int(8 + 10 * (puntaje / max_fitness)) if max_fitness > 0 else 8
    color = COLORS["glow"] if agent.glow_timer > 0 else COLORS["agent"]
    pygame.draw.circle(screen, color, pos, size)
    eye_radius = max(2, size // 4)
    eye_x_offset = size // 3
    eye_y_offset = size // 4
    pygame.draw.circle(screen, (255, 255, 255), (pos[0] - eye_x_offset, pos[1] - eye_y_offset), eye_radius)
    pygame.draw.circle(screen, (255, 255, 255), (pos[0] + eye_x_offset, pos[1] - eye_y_offset), eye_radius)
    pupil_radius = max(1, eye_radius // 2)
    pygame.draw.circle(screen, (0, 0, 0), (pos[0] - eye_x_offset, pos[1] - eye_y_offset), pupil_radius)
    pygame.draw.circle(screen, (0, 0, 0), (pos[0] + eye_x_offset, pos[1] - eye_y_offset), pupil_radius)

def tournament_selection(agents, k=3):
    selected = []
    for _ in range(len(agents)):
        aspirants = random.sample(agents, k)
        selected.append(max(aspirants, key=lambda a: a.fitness))
    return selected

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Simulación Evolutiva")
    clock = pygame.time.Clock()

    env = Environment(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, n_food=50, n_agents=POPULATION)
    env.reset()

    for gen in range(GENERATIONS):
        env.reset_food()
        step = 0
        running = True

        while running:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            env.step()
            step += 1

            screen.fill(COLORS["bg"])
            pygame.draw.rect(screen, COLORS["border"], (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), 2)

            for food in env.food_positions:
                pygame.draw.circle(screen, COLORS["food"], food.astype(int), 6)

            max_fitness = max(agent.fitness for agent in env.agents) or 1
            for agent in env.agents:
                if agent.alive:
                    draw_agent(screen, agent, max_fitness)
                    if agent.glow_timer > 0:
                        agent.glow_timer -= 1

            draw_text(screen, f"Generación: {gen + 1}", 20, 10, 10)
            draw_text(screen, f"Mejor: {max_fitness}", 18, 10, 35)

            pygame.display.flip()

            if all(not agent.alive for agent in env.agents) or step > 350:
                running = False

        print(f"Generación {gen + 1}\n - Mejor puntaje: {max_fitness}")

        selected = tournament_selection(env.agents, k=3)
        new_agents = []
        while len(new_agents) < POPULATION:
            p1, p2 = random.sample(selected, 2)
            brain = Agent.crossover(p1, p2)
            child = Agent(input_size=8, brain=brain)  # input_size corregido a 8
            child.mutate(rate=0.08)
            child.position = np.random.rand(2) * [SCREEN_WIDTH, SCREEN_HEIGHT]
            child.velocity = np.zeros(2)
            child.fitness = 0
            child.alive = True
            new_agents.append(child)

        env.agents = new_agents

    pygame.quit()

if __name__ == "__main__":
    main()

