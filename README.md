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

Antes de ejecutar el programa, se estable un archivo de configuración bajo el nombre de `config.yaml`.

En este archivo se configuran todos los parametros de ejecución del programa, así como la ubicación de los datos de los items.

A continuación, se muestra un ejemplo de configuración:

```yaml
genetic_operators:
  crossover:
    # all options: one_point, two_point, anular, uniform
    opt: uniform
  mutation:
    # all options: gen, multi_limited, multi_uniform, full 
    opt: multi_uniform

selection: 
  # [0.0-1.0]
  A: 0.3
  B: 0.7
  # all options: elite, roulette, universal, boltzmann, det_tournaments, prob_tournaments, ranking
  method1: elite
  method2: roulette
  method3: universal
  method4: ranking

implementation: 
  # all options: fill_all, fill_parent
  opt: fill_parent

stop:
  # all options: time, gens, acceptable, struct, content
  opt: time
  # in case of time, declared in seconds:
  max_time: 30

# path to tsv dile conataining all items info
items_dataset: 
  path: allitems
  weapons_filename: armas.tsv
  boots_filename: botas.tsv
  helmets_filename: cascos.tsv
  gloves_filename: guantes.tsv
  breastplates_filename: pecheras.tsv

# all options: warrior, archer, defender, infiltrate
character_class: warrior

# natural number greater than zero
initial_population: 160
```

### Ejecución

Finalmente, para correr el trabajo se debe ejecutar el comando:

```python
python .\main.py
```

Si todos los parámetros son correctos, el programa comienza a ejecutar y se nos mostrará una ventana con un gráfico en tiempo real representando:

- Fitness mínimo por generación
- Fitnes medio por generación
- Diversidad genética