import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation

finished_min_and_mean = False
finished_genetic_diversity = False
finished_best_ind_stats = False

def plot_min_and_mean_fitness(q):

    global finished_min_and_mean

    finished_min_and_mean = False

    # generations
    gens = []

    # fitnesses
    min_fitness = []
    mean_fitness = []
    max_fitness = []

    fig = plt.figure()
    #creating a subplot 
    ax1 = fig.add_subplot(1,1,1)

    def animate(i): 
        global finished_min_and_mean

        if finished_min_and_mean:
            return

        gen = q.get()

        if gen == "STOP":
            finished_min_and_mean = True
            return

        gens.append(gen.number)
        min_fitness.append(gen.min_fitness())
        mean_fitness.append(gen.mean_fitness())
        max_fitness.append(gen.max_fitness())

        ax1.clear()

        plt.xlabel("Generation")
        plt.ylabel("Fitness")
        plt.title("Fitness real-time")

        l1, = ax1.plot(gens, min_fitness, 'r-')
        l2, = ax1.plot(gens, mean_fitness, 'g-')
        l3, = ax1.plot(gens, max_fitness, 'b-')

        plt.legend([l3, l2, l1],["Maximum Fitness", "Mean Fitness", "Minimum Fitness"])
        
    ani = animation.FuncAnimation(fig, animate, interval=100) 
    plt.show()

    return

def plot_genetic_diversity(q):

    global finished_genetic_diversity

    finished_genetic_diversity = False

    # generations
    gens = []

    # heights
    heights_divs = []

    # fitnesses
    weapons_divs = []
    boots_divs = []
    helmets_divs = []
    gloves_divs = []
    breastplates_divs = []

    fig = plt.figure()
    #creating a subplot 
    ax1 = fig.add_subplot(1,1,1)

    def animate(i): 
        global finished_genetic_diversity        

        if finished_genetic_diversity:
            return

        gen = q.get()

        if gen == "STOP":
            finished_genetic_diversity = True
            return

        div = gen.genetic_diversity()

        gens.append(gen.number)
        
        heights_divs.append(div['heights'])
        weapons_divs.append(div['weapons'])
        boots_divs.append(div['boots'])
        helmets_divs.append(div['helmets'])
        gloves_divs.append(div['gloves'])
        breastplates_divs.append(div['breastplates'])

        ax1.clear()

        plt.xlabel("Generation")
        plt.ylabel("Diversity")
        plt.title("Genetic diversity")

        l0, = ax1.plot(gens, heights_divs, color='#2efff8', linestyle='solid')
        l1, = ax1.plot(gens, weapons_divs, color='#2a5de8', linestyle='solid')
        l2, = ax1.plot(gens, boots_divs, color='#daff1f', linestyle='solid')
        l3, = ax1.plot(gens, helmets_divs, color='#e61ee2', linestyle='solid')
        l4, = ax1.plot(gens, gloves_divs, color='#18f545', linestyle='solid')
        l5, = ax1.plot(gens, breastplates_divs, color='#ffd336', linestyle='solid')

        plt.legend([l0, l1, l2, l3, l4, l5],["Heights diversity", "Weapons diversity", "Boots diversity", "Helmets diversity", "Gloves diversity", "Breastplates diversity"])
        
    ani = animation.FuncAnimation(fig, animate, interval=100) 
    plt.show()

    return


def plot_best_ind_stats(q):

    global finished_best_ind_stats

    finished_best_ind_stats = False

    # generations
    gens = []

    best_strength = []
    best_agility = []
    best_expertise = []
    best_resistance = []
    best_life = []
    best_attack = []
    best_defense = []

    # Create 2x2 sub plots
    gs = gridspec.GridSpec(2, 2)

    fig = plt.figure()
    ax1 = plt.subplot(gs[0, 0]) # row 0, col 0
    ax3 = plt.subplot(gs[0, 1]) # row 0, col 1
    ax2 = plt.subplot(gs[1, :]) # row 1, span all columns

    # fig, (ax1, ax2, ax3) = plt.subplots(3)

    def animate(i): 
        global finished_best_ind_stats

        if finished_best_ind_stats:
            return

        gen = q.get()

        if gen == "STOP":
            finished_best_ind_stats = True
            return

        bests_ind_stats = gen.max_ind_stats()
        gens.append(gen.number)
        
        best_strength.append(bests_ind_stats['strength'])
        best_agility.append(bests_ind_stats['agility'])
        best_expertise.append(bests_ind_stats['expertise'])
        best_resistance.append(bests_ind_stats['resistance'])
        best_life.append(bests_ind_stats['life'])
        best_attack.append(bests_ind_stats['attack'])
        best_defense.append(bests_ind_stats['defense'])
     
        ax1.clear()
        ax2.clear()
        ax3.clear()

        ax1.set(xlabel='Generation', ylabel='Stats')
        ax2.set(xlabel='Generation', ylabel='Stats')
        ax3.set(xlabel='Generation', ylabel='Stats')

        ax1.set_title("Best Individual's Main Stats real-time")
        ax2.set_title("Best Individual's Attack and Defence real-time")
        ax3.set_title("Best Individual's Secondary Stats Defence real-time")

        l1, = ax1.plot(gens, best_strength, color='#de3c14', linestyle='solid') #rojito
        l2, = ax3.plot(gens, best_agility, color='#2a5de8', linestyle='solid') #azulcito
        l3, = ax3.plot(gens, best_expertise, color='#daff1f', linestyle='solid') #amarillo
        l4, = ax3.plot(gens, best_resistance, color='#e61ee2', linestyle='solid') #violeta
        l5, = ax1.plot(gens, best_life, color='#18f545', linestyle='solid') #verde
        l6, = ax2.plot(gens, best_attack, color='#ffd336', linestyle='solid') #naranja
        l7, = ax2.plot(gens, best_defense, color='#2efff8', linestyle='solid') #celeste

        ax1.legend([l5, l1],["Life", "Strength"])
        ax3.legend([l4, l3, l2],["Resistance","Expertise", "Agility"])
        ax2.legend([l7, l6],["Defense","Attack"])
        
    ani = animation.FuncAnimation(fig, animate, interval=100) 
    plt.show()

    return



def plot_data(matrix, avg_array, title):

    print(f"Generating graph '{title}'")

    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.title(title)

    for i in range(0, len(matrix)):
        plt.plot(matrix[i], color='#2efff8', linestyle='solid')
    
    plt.plot(avg_array, "k-")

    plt.show()

    return

def plot_all_data(max_fitness_matrix, mean_fitness_matrix, min_fitness_matrix, avg_max_fitness, avg_mean_fitness, avg_min_fitness, title):
    
    print(f"Generating graph '{title}'")
    
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.title(title)
    
    for i in range(0, len(max_fitness_matrix)):
        plt.plot(max_fitness_matrix[i], color='#f59c95', linestyle='solid')
        plt.plot(mean_fitness_matrix[i], color='#bcf5b3', linestyle='solid')
        plt.plot(min_fitness_matrix[i], color='#b5e0ff', linestyle='solid')
    
    plt.plot(avg_max_fitness, "r-")
    plt.plot(avg_mean_fitness, "g-")
    plt.plot(avg_min_fitness, "b-")

    plt.show()

    return