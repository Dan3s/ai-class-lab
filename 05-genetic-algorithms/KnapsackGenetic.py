import random
import math


class KnapsackGenetic:
    def __init__(self, params):
        self.ALL_NUMBERS = list(range(params["max_per_item"] + 1))
        self.params = params
        self.specimen = [None] * self.params["generation_size"]

        self.create_initial_population()

    def create_initial_population(self):
        self.specimen = list(map(
            lambda _: list(map(
                lambda _: random.choice(self.ALL_NUMBERS),
                [None] * len(self.params["items"])
            )),
            self.specimen
        ))

    def fitness(self, specimen):
        # Use params: self.params["max_weight"] to check the max weight of the specimen
        # Use params: self.params["items"]

        lista = list(zip(specimen, self.params["items"]))
        sum_values = int()
        sum_weights = int()

        for z in lista:
            sum_values = sum_values + z[0]*z[1].value
            sum_weights = sum_weights + z[0]*z[1].weight

        if (sum_weights > self.params["max_weight"]):
            return 0
        else:
            return sum_values/self.params["max_weight"]


    def is_converged(self):
        if any(self.fitness(specimen) >= self.params["fit_threshold"] for specimen in self.specimen):
            return True

        return False

    def get_fit(self):
        evaluations = self.fitness_all()

        max_evaluation = max(evaluations)

        max_index = evaluations.index(max_evaluation)

        return self.specimen[max_index], max_evaluation

    def fitness_all(self):
        return list(map(self.fitness, self.specimen))

    def select_specimen(self, specimen_evaluations):
        specimen_and_evaluations = list(zip(self.specimen, specimen_evaluations))

        specimen_and_evaluations.sort(key=lambda e: e[1], reverse=True)

        n_top = int(math.ceil(len(self.specimen) * self.params["select_top"]))

        return list(map(lambda s: s[0], specimen_and_evaluations[:n_top]))

    def mutate(self, specimen):
        # Use parameter: self.params["max_per_item"] to check maximum for gene
        # Use parameter: self.params["mutation_percentage"]
        n_digits = int(self.params["mutation_percentage"] * (len(specimen)))

        digit_indexes = random.sample(list(range(len(specimen))), n_digits)

        mutated = specimen[:]

        for idx in digit_indexes:
            mutated[idx] = random.choice(self.ALL_NUMBERS)

        return mutated

    def generate_children(self, selected_specimen):
        mutated_specimen = [None] * len(self.specimen)

        for i in range(len(mutated_specimen)):
            mutated_specimen[i] = self.mutate(random.choice(selected_specimen))

        return mutated_specimen

    def run(self):
        generation_number = 1

        while generation_number <= self.params["max_generations"] and not self.is_converged():
            top_generation = self.get_fit()
            top_str = "".join(str(top_generation[0]))

            print(f"Generation #{generation_number}:\t{top_str}\t{top_generation[1]}")

            specimen_evaluations = self.fitness_all()
            selected_specimen = self.select_specimen(specimen_evaluations)

            self.specimen = self.generate_children(selected_specimen)

            generation_number += 1

        return self.get_fit()