#Creacion de la primera poblacion
#Funcion 1
import scipy as sp #Se renombra el Scipy

def creacion_alelos(N, p):
    """La poblacion esta conformada por N individuos, lo que indica que cada individuo esta conformado con 2 cromosomas A o a
    """
    population = []
    for i in range(N):
        allele1 = "A"
        if sp.random.rand() > p:
            allele1 = "a"
        allele2 = "A"
        if sp.random.rand() > p:
            allele2 = "a"
        population.append((allele1, allele2))
    return population

# Conteo de pares de baces 
#Funcion 2
def compute_frequencies(population):
    """ Devuelve un diccionario de frecuencias genotípicas"""
    AA = population.count(("A", "A"))
    Aa = population.count(("A", "a"))
    aA = population.count(("a", "A"))
    aa = population.count(("a", "a"))
    return({"AA": AA, "aa": aa, "Aa": Aa, "aA": aA})

# Para compensar la nueva generacion 
#Funcion 3

def reproduce_population(population):
    """ Se crea una nueva generacion por ende cada nuevo decendiente N recibe un cromosoma de cada uno de los padres.
    """
    new_generation = []
    N = len(population)
    for i in range(N):
        # random integer between 0 and N-1
        dad = sp.random.randint(N)
        mom = sp.random.randint(N)
        # which chromosome comes from mom
        chr_mom = sp.random.randint(2)
        offspring = (population[mom][chr_mom], population[dad][1 - chr_mom])
        #if offspring == ("a", "a"): 
          #next()
        new_generation.append(offspring)
    return new_generation
