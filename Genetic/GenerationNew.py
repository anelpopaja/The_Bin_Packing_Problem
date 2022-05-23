'''
0. Pocetna generacija se generise nasumicno nakon cega se FFD primjenjuje na jedinke koje imaju greske (prepunjenost) u binovima
    0.1. Item se vadi iz bina (stack) koji je prepunjen i stavlja u stack koji cemo s FFD rasporediti u skup binova
1. Dio prolazi selekcijom npr 30% ukupne pocetne generacije (30 jedinki pocetno)
2. Ostali dio se salje u crossover i vrti dok se ne dobiju validne jedinke (od dva nasumicna roditelja nastaju dvije nove jedinke) dok se ne dobije trazeni broj jedinki
3. Nakon sto se dobije validna jedinka Provjeravamo da li dolazi do mutacije te validne jednike
4. Ponovno sve
'''
import random

from The_Bin_Packing_Problem.Genetic.Individual import Individual



class GenerationNew:

    population_count = 30
    gen_count = 0
    max_gen_count = 1000
    population = []
    mutation_chance = 0.1
    no_improvement_count = 0
    stagnation_max = 30
    best_fitness_value = 0
    fitness_over_time = []

    # TODO needs a constructor class that takes in Individuals list i.e. Individuals of a generation as argument

    def __init__(self, items, bin_capacity, item_count):
        self.items = items
        self.bin_capacity = bin_capacity
        self.item_count = item_count
        GenerationNew.gen_count += 1
        print("Generation number: " + str(GenerationNew.gen_count))
        self.doGeneration()


        #bcs we have sorted the generation by fitness, the 1st element has the highest fitness

        current_fitness = GenerationNew.population[0].getFitness()
        print("Best fitness: ")
        print(current_fitness)
        self.fitness_over_time.append(current_fitness)



        # TODO Stagnation Check
        if current_fitness == GenerationNew.best_fitness_value:
            GenerationNew.no_improvement_count += 1
        else:
            GenerationNew.best_fitness_value = current_fitness
            GenerationNew.no_improvement_count = 0

        print("\nBest Result: ")
        print(self.bestResult())


        #if self.gen_count == 200:
            # print("Best genes: ", best_individual.getGenes())
            #print("Sorted in ", self.bestResult(), " bins")

    # def stagnationCheck(self):


    def bestResult(self):
        result = self.item_count
        for el in self.population:
            if el.full_bins < result:
                result = el.full_bins
        return result

    def getPopulation(self):
        return GenerationNew.population

    def doGeneration(self):

        offspring_list = []
        # While our offspring are less than our current population count, create new offspring
        while (len(offspring_list) < self.population_count):

            # get parents
            mother = self.getParent()
            father = self.getParent()

            while (mother == father):
                father = self.getParent()

            # perform crossover

            offspring_a, offspring_b = self.generateOffspring(mother, father)


            # mutate

            offspring_a, offspring_b = self.mutate(offspring_a, offspring_b)


            offspring_list.append(offspring_a)
            offspring_list.append(offspring_b)

        # improving on the algorithm by mixing newly created gen with parents and selecting the best #population_count

        GenerationNew.population.extend(offspring_list)
        # GenerationNew.population = offspring_list

        GenerationNew.population = sorted(GenerationNew.population, key=lambda x: x.fitness, reverse=True)[:self.population_count]
        # print("Size of new population " + str (len(GenerationNew.population)))
        # Generation
        # print("Duzina: ", len(self.population))



    def generateOffspring(self, individual_a, individual_b):
        # crossover_position = random.randint(1, len(individual_a.genes) - 1)
        offspring_a = self.doCrossover(individual_a, individual_b)
        offspring_b = self.doCrossover(individual_b, individual_a)

        return offspring_a, offspring_b

    def doCrossover(self, individual_a, individual_b):
        crossover_position = random.randint(1, len(individual_a.genes) - 1)
        offspring_gene_sequence = individual_a.getGenes()[:crossover_position]
        offspring_gene_sequence.extend(individual_b.getGenes()[crossover_position:])

        return Individual(self.bin_capacity, self.item_count, self.items, offspring_gene_sequence)

    def getParent(self):

        return self.tournamentSelection()

    def tournamentSelection(self):

        candidate_1 = GenerationNew.population[random.randint(0, self.population_count - 1)]
        candidate_2 = GenerationNew.population[random.randint(0, self.population_count - 1)]

        while (candidate_1 == candidate_2):
            candidate_2 = GenerationNew.population[random.randint(0, self.population_count - 1)]

        if (candidate_1.getFitness() > candidate_2.getFitness()):
            return candidate_1
        else:
            return candidate_2

    def mutate(self, offspring_a, offspring_b):


        if(random.uniform(0,1) <= self.mutation_chance):
            offspring_a = self.mutateIndividual(offspring_a)
            # print("Mutation")

        if (random.uniform(0, 1) <= self.mutation_chance):
            offspring_b = self.mutateIndividual(offspring_b)
            # print("Mutation")

        new_offspring_a = Individual(self.bin_capacity, self.item_count, self.items, offspring_a.getGenes())
        new_offspring_b = Individual(self.bin_capacity, self.item_count, self.items, offspring_b.getGenes())

        return new_offspring_a, new_offspring_b

    def mutateIndividual(self, individual):
        genes = individual.getGenes()
        index = random.randint(0,len(genes)-1)
        new_bin = random.randint(0,self.item_count-1)
        while (genes[index] == new_bin):
            new_bin = random.randint(0, self.item_count - 1)
        genes[index] = new_bin
        return individual


    def getGenCount(self):
        return GenerationNew.gen_count
