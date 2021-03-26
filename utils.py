import yaml
import os
import csv

from models import Config, Weapon, Boots, Helmet, Gloves, Breastplate, AllItems

config_filename = 'config.yaml'

def get_val_from_config(d, key, required = False):
    v = d.get(key, None)

    if required and v is None:
        print(f'Error: Missing "{key}" key at config file')
        exit(1)

    return v

def read_config():

    with open(config_filename) as file:
        config = yaml.load(file, Loader=yaml.FullLoader)

        genetic_operators = get_val_from_config(config, 'genetic_operators', True)

        crossover = get_val_from_config(genetic_operators, 'crossover', True)
        crossover_opt = get_val_from_config(crossover, 'opt', True)
        crossover_params = get_val_from_config(crossover, 'params', False)

        mutation = get_val_from_config(genetic_operators, 'mutation', True)
        mutation_opt = get_val_from_config(mutation, 'opt', True)
        mutation_params = get_val_from_config(mutation, 'params', False)

        selection = get_val_from_config(config, 'selection', True)
        K = get_val_from_config(selection, 'K', True)
        A = get_val_from_config(selection, 'A', True)
        B = get_val_from_config(selection, 'B', True)
        selection_method1 = get_val_from_config(selection, 'method1', True)
        selection_method1_opt = get_val_from_config(selection_method1, 'opt', True)
        selection_method1_params = get_val_from_config(selection_method1, 'params', False)
        selection_method2 = get_val_from_config(selection, 'method2', True)
        selection_method2_opt = get_val_from_config(selection_method2, 'opt', True)
        selection_method2_params = get_val_from_config(selection_method2, 'params', False)
        selection_method3 = get_val_from_config(selection, 'method3', True)
        selection_method3_opt = get_val_from_config(selection_method3, 'opt', True)
        selection_method3_params = get_val_from_config(selection_method3, 'params', False)
        selection_method4 = get_val_from_config(selection, 'method4', True)
        selection_method4_opt = get_val_from_config(selection_method4, 'opt', True)
        selection_method4_params = get_val_from_config(selection_method4, 'params', False)

        implementation = get_val_from_config(config, 'implementation', True)
        implementation_opt = get_val_from_config(implementation, 'opt', True)

        stop = get_val_from_config(config, 'stop', True)
        stop_opt = get_val_from_config(stop, 'opt', True)
        stop_params = get_val_from_config(stop, 'params', False)

        items_dataset = get_val_from_config(config, 'items_dataset', True)
        items_dataset_path = get_val_from_config(items_dataset, 'path', True)
        items_dataset_weapons_filename = get_val_from_config(items_dataset, 'weapons_filename', True)
        items_dataset_boots_filename = get_val_from_config(items_dataset, 'boots_filename', True)
        items_dataset_helmets_filename = get_val_from_config(items_dataset, 'helmets_filename', True)
        items_dataset_gloves_filename = get_val_from_config(items_dataset, 'gloves_filename', True)
        items_dataset_breastplates_filename = get_val_from_config(items_dataset, 'breastplates_filename', True)
        character_class = get_val_from_config(config, 'character_class', True)

        initial_population = get_val_from_config(config, 'initial_population', True)
            
        return Config(crossover_opt, crossover_params, mutation_opt, mutation_params, K, A, B, selection_method1_opt, selection_method1_params, selection_method2_opt, selection_method2_params, selection_method3_opt, selection_method3_params, selection_method4_opt, selection_method4_params, implementation_opt, stop_opt, stop_params, items_dataset_path, items_dataset_weapons_filename, items_dataset_boots_filename, items_dataset_helmets_filename, items_dataset_gloves_filename, items_dataset_breastplates_filename, character_class, initial_population)

def read_items(path, filename, item_contructor):
    full_path = os.path.join(path, filename)

    try:
        tsv_file = open(full_path)
        read_tsv = csv.reader(tsv_file, delimiter="\t")

        items = []

        i = 0
        for row in read_tsv:
            if i == 0:
                first_row = row
                for j in range(0, len(first_row)):
                    first_row[j] = first_row[j].lower()
            else:
                it = {}
                for j in range(0, len(row)):
                    it[first_row[j]] = float(row[j])
                items.append(item_contructor(i-1, it['id'], it['fu'], it['ag'], it['ex'], it['re'], it['vi'])) # TODO: Check whether to use float or FIXED_POINT!
            i += 1
    except:
        print(f'Error: An error ocurred reading items from file "{full_path}"')
        exit(1)

    return items

def read_all_items(path, items_filenames):

        weapons = read_items(path, items_filenames.weapons, Weapon)
        boots = read_items(path, items_filenames.boots, Boots)
        helmets = read_items(path, items_filenames.helmets, Helmet)
        gloves = read_items(path, items_filenames.gloves, Gloves)
        breastplates = read_items(path, items_filenames.breastplates, Breastplate)

        return AllItems(weapons, boots, helmets, gloves, breastplates)


