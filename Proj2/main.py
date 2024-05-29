import pandas as pd
from deap import base, creator, tools, algorithms
import numpy as np
import logging
import random
import multiprocessing
import time

POPULATION = 500
MUTAION_PROBABILITY = 0.2
CROSSOVER_PROBABILITY = 0.7
NUMBER_OF_GENERATIONS = 500
TOURNAMENT_SIZE = 10

INPUT_FILE = 'Project2_DistancesMatrix.xlsx'
ECO_POINTS_FILE = 'eco_points.csv'

distance_matrix = pd.read_excel(INPUT_FILE, header=0, index_col=0).values
eco_points = pd.read_csv(ECO_POINTS_FILE, header=None).values.flatten()

# Central point index
CENTRAL = 0
LOG_LEVEL = logging.INFO
# LOG_LEVEL = logging.DEBUG
logging.basicConfig(level=LOG_LEVEL, format='%(levelname)s: %(message)s')


# After 30, the penalty is 40%
PENALITY = (30, 1.4)
PENALITY_POINTS = [3, 43, 52, 53, 58, 69, 71, 72, 73, 74, 75, 76, 77, 78, 92]

def get_distance(i, j, matrix=distance_matrix):
	"""
	Retrieves the distance between two EcoPoints from the distance matrix.
	"""
	return matrix[i, j]

# Define the fitness function
def eval_route(individual):
    total_distance = 0
    num_points = len(individual)
    current_point = CENTRAL

    for visited, next_point in enumerate(individual):
        total_distance += distance_matrix[current_point, eco_points[next_point]]
        current_point = eco_points[next_point]

        if current_point in PENALITY_POINTS and visited > PENALITY[0]:
            total_distance *= PENALITY[1]

    total_distance += distance_matrix[current_point, CENTRAL]  # Return to the central point
    return total_distance,

# Genetic Algorithm Setup
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()

toolbox.register("indices", random.sample, range(len(eco_points)), len(eco_points))

toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=TOURNAMENT_SIZE)
toolbox.register("evaluate", eval_route)

def save_route(individual):
	route = [CENTRAL] + [eco_points[idx]  for idx in individual] + [CENTRAL]
	distances = [distance_matrix[route[i], route[i + 1]] for i in range(len(route) -1)]
	total_distance = sum(distances)

	route_str = 'C, '
	for idx, distance in enumerate(distances[:-1]):
		route_str += f'{distance:.1f}E{eco_points[idx]}, '
	route_str += f'{distances[-1]:.1f}C, Total={total_distance:.1f}'
	logging.debug(route_str)

	with open('best_route.txt', 'w') as f:
		f.write(route_str)
	return route_str

if '__main__' == __name__:
	start_time = time.time()
	pool = multiprocessing.Pool()
	toolbox.register("map", pool.map)

	random.seed(42)
	pop = toolbox.population(n=POPULATION)
	hof = tools.HallOfFame(1)

	stats = tools.Statistics(lambda ind: ind.fitness.values)
	stats.register("min", np.min)
	stats.register("avg", np.mean)

	algorithms.eaSimple(pop, toolbox, cxpb=CROSSOVER_PROBABILITY, mutpb=MUTAION_PROBABILITY, ngen=NUMBER_OF_GENERATIONS, stats=stats, halloffame=hof, verbose=LOG_LEVEL == logging.DEBUG)

	logging.debug(hof[0])

	best_ind = hof[0]
	logging.debug(f"Best individual is: {best_ind} with distance: {best_ind.fitness.values[0]}")
	logging.info(f"Execution time: {time.time() - start_time:.2f} seconds")
	logging.info(save_route(best_ind))
