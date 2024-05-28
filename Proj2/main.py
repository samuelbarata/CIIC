import pandas as pd
from deap import base, creator, tools, algorithms
import numpy as np
import logging
import random

INPUT_FILE = 'Project2_DistancesMatrix.xlsx'
ECO_POINTS_FILE = 'eco_points.csv'

distance_matrix = pd.read_excel(INPUT_FILE, header=0, index_col=0).values
eco_points = pd.read_csv(ECO_POINTS_FILE, header=None).values.flatten()

# Central point index
CENTRAL = 0
LOG_LEVEL = logging.INFO
LOG_LEVEL = logging.DEBUG
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
        total_distance += distance_matrix[current_point, next_point]
        current_point = next_point

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
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", eval_route)

def save_route(individual):
	route = [CENTRAL] + individual
	logging.debug(route)
	distances = [distance_matrix[route[i], route[i + 1]] for i in range(len(route) - 1)]
	total_distance = sum(distances)

	route_str = 'C, ' + ', '.join(f'{d:.1f}E{eco_points[i]}' for i, d in enumerate(distances)) + f', Total={total_distance:.1f}'
	with open('best_route.txt', 'w') as f:
		f.write(route_str)

if '__main__' == __name__:
	random.seed(42)
	pop = toolbox.population(n=300)
	hof = tools.HallOfFame(1)

	stats = tools.Statistics(lambda ind: ind.fitness.values)
	stats.register("min", np.min)
	stats.register("avg", np.mean)

	algorithms.eaSimple(pop, toolbox, cxpb=0.7, mutpb=0.2, ngen=500, stats=stats, halloffame=hof, verbose=True)

	logging.debug(hof[0])

	best_ind = hof[0]
	logging.info(f"Best individual is: {best_ind} with distance: {best_ind.fitness.values[0]}")
	save_route(best_ind)
