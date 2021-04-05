# Trabajo Práctico Algoritmos Genéticos para la materia Sistemas de Inteligencia Artificial

## Instalación

Para correr el programa debe ser necesario instalar python 3

[Descargar Python 3](https://www.python.org/downloads/)

Una vez instalado python, se necesitan la librería pyyaml.
Para eso, se debe tener instalado pip para python
La guía de instalación se encuentra en el siguiente link:

[Instalar Pip](https://tecnonucleous.com/2018/01/28/como-instalar-pip-para-python-en-windows-mac-y-linux/)

Una vez instalado pip, se debe correr, dentro de la carpeta del repositorio, el comando:

```python
pip install -r requirements.txt
```

## Guía de uso

### Configuración

Antes de ejecutar el programa, se establece un archivo de configuración bajo el nombre de `config.yaml`.

En este archivo se configuran todos los parametros de ejecución del programa, así como la ubicación de los datos de los items.

La carpeta donde se ubican los items debe tener la siguiente estructura: ubicada en la carpeta principal del trabajo.
Por otra parte, los nombres de esta carpeta y sus archivos tsv son parametrizables en el archivo de configuración.

![folders items structure](https://i.ibb.co/t4YCN6F/structure.png)

A continuación, se muestra un ejemplo de configuración:

```yaml
genetic_operators:
  crossover:
    # all options: one_point, two_points, anular, uniform
    opt: uniform
    params:
      # in case of anular (Cruce anular) ("l" is the number of genes to swap)
      # l must be an integer between [0 - 3] 
      l: 3 

      # in case of uniform (Cruce uniforme) ("p" is the probability to swap a gen)
      # p between [0.0 - 1.0]
      p: 0.5

  mutation:
    # all options: gen, multi_limited, multi_uniform, full 
    opt: full
    params:
      # in case of gen (pg is the probability to mutate only one gene)\
      # pg between [0.0 - 1.0]
      pg: 0.5

      # in case of multi_limited (pml is the probability to mutate [1-M] gens at random [where M is the ammount of gens])
      # pml between [0.0 - 1.0]
      pml: 0.5
      
      # in case of multi_uniform (pmu is the probability of each gene to mutate)
      # pmu between [0.0 - 1.0]
      pmu: 0.5

      # in case of full (pf is the probability of mutating all gens or none)
      # pf between [0.0 - 1.0]
      pf: 0.5


selection:
  # K is the number of individuals selected each generation
  K: 50
  # A and B must be between [0.0-1.0]
  A: 0.6
  B: 0.4
  # all options: elite, roulette, universal, boltzmann, det_tournaments, prob_tournaments, ranking
  method1: 
    opt: elite
    params:
      # in case of boltzmann
      initial_temp: 50 
      min_temp: 10
      k: 2

      # in case of probabilistic tournaments
      # pt_threshold between [0.5 - 1.0]
      pt_threshold: 0.7
  method2: 
    opt: elite
    params:
      # in case of boltzmann
      initial_temp: 50 
      min_temp: 10
      k: 2
    
      # in case of probabilistic tournaments
      # pt_threshold between [0.5 - 1.0]
      pt_threshold: 0.7
  method3: 
    opt: elite
    params:
      # in case of boltzmann
      initial_temp: 50 
      min_temp: 10
      k: 2
    
      # in case of probabilistic tournaments
      # pt_threshold between [0.5 - 1.0]
      pt_threshold: 0.7
  method4: 
    opt: elite
    params:
      # in case of boltzmann
      initial_temp: 50 
      min_temp: 10
      k: 2

      # in case of probabilistic tournaments
      # pt_threshold between [0.5 - 1.0]
      pt_threshold: 0.7

implementation: 
  # all options: fill_all, fill_parent
  opt: fill_parent

stop:
  # all options: time, gens, acceptable, struct, content
  opt: struct
  params:
    # in case of time, declared in seconds
    max_time: 10

    # in case of gens
    max_generation: 100

    # in case of acceptable
    mean_acceptable_fitness: 100

    # in case of struct
    # relevant_percentage_of_change must be between [0.0 - 1.0]
    relevant_percentage_of_change: 0.7
    considered_gens: 15

    # in case of content
    max_generations_counter: 5


# path to tsv file containing all items info
items_dataset: 
  path: allitems_test
  weapons_filename: armas.tsv
  boots_filename: botas.tsv
  helmets_filename: cascos.tsv
  gloves_filename: guantes.tsv
  breastplates_filename: pecheras.tsv

# all options: warrior, archer, defender, infiltrate
character_class: infiltrate

# natural number greater than zero
initial_population: 100

# to run multiple iterations 
multiple_times:
  run: False  #requires boolean True or False
  iterations: 40
```

El parametro ```multiple_times``` indica si se desea correr esta configuración de los algoritmos para multiples iteraciones de poblaciones. De estar **activado**, el programa mostrará los graficos de los siguientes elementos para cada poblacion en cada numero de generación: 
* El maximo 
* La media 
* El minimo fitness 
* La diversidad genetica

En cada grafico se muestra tambien el promedio de cada una de estas para poder observar la tendencia que tienen.

De estar ```multiple_times``` **desactivado** se mostrarán graficos a tiempo real de:
* Maximo, media y minimo fitness de la poblacion
* Diversidad genetica para cada uno de los genes de la población
* La vida, fuerza, resistencia, pericia y agilidad para el individuo con mayor fitness
* El ataque y la defensa para el individuo con mayor fitness

### Ejecución

Finalmente, para correr el trabajo se debe ejecutar el comando:

```python
python .\main.py
```
