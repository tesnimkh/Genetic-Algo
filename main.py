import random
import matplotlib.pyplot as plt

# define problem inputs
values = [10, 5, 20, 15, 30]
weights = [1, 2, 3, 4, 5]
max_weight = 10
num_items = len(values)

# define genetic algorithm parameters and functions
population_size = 100
num_generations = 50
mutation_rate = 0.01

def fitness_function(individual):
    # calculate total value and weight for individual
    total_value = sum([values[i] * individual[i] for i in range(num_items)])
    total_weight = sum([weights[i] * individual[i] for i in range(num_items)])

    # calculate fitness as total value if weight limit is not exceeded, 0 otherwise
    if total_weight > max_weight:
        return 0
    else:
        return total_value

def generate_individual():
    # generate random binary string of length num_items
    return [random.randint(0, 1) for i in range(num_items)]

def generate_population(population_size):
    # generate population of random individuals
    return [generate_individual() for i in range(population_size)]

def mutate_individual(individual):
    # flip each bit in individual with probability mutation_rate
    for i in range(num_items):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]
    return individual

def select_parent(population):
    # select parent using roulette wheel selection
    fitness_scores = [fitness_function(individual) for individual in population]
    total_fitness = sum(fitness_scores)
    selection_probabilities = [fitness / total_fitness for fitness in fitness_scores]
    return random.choices(population, weights=selection_probabilities)[0]

def crossover(parent1, parent2):
    # perform single-point crossover between parents
    crossover_point = random.randint(1, num_items - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# initialize plot
plt.figure()

# generate initial population
population = generate_population(population_size)

# run genetic algorithm and plot progress
best_fitnesses = []
for i in range(num_generations):
    # select parents and perform crossover
    offspring = []
    for j in range(population_size // 2):
        parent1 = select_parent(population)
        parent2 = select_parent(population)
        child1, child2 = crossover(parent1, parent2)
        offspring.append(mutate_individual(child1))
        offspring.append(mutate_individual(child2))

    # replace population with offspring
    population = offspring

    # calculate and plot progress
    best_individual = max(population, key=fitness_function)
    best_fitness = fitness_function(best_individual)
    best_fitnesses.append(best_fitness)
    plt.clf()
    plt.plot(best_fitnesses)
    plt.xlabel('Generation')
    plt.ylabel('Best Fitness')
    plt.title('Knapsack Problem - Genetic Algorithm Progress')
    plt.pause(0.01)

# print final result
best_individual = max(population, key=fitness_function)
best_fitness = fitness_function(best_individual)
print("Best solution:", best_individual)
print("Best fitness:", best_fitness)

# show final plot
plt.show()
