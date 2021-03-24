import yaml
import os
import csv

from models import Config, Weapon, Boots, Helmet, Gloves, Breastplate, AllItems

config_filename = 'config.yaml'

def get_val_from_config(d, key):
    v = d.get(key, None)

    errored = False

    if v is None:
        print(f'Error: Missing "{key}" key at config file')
        errored = True

    return v, errored

def read_config():

    with open(config_filename) as file:
        config = yaml.load(file, Loader=yaml.FullLoader)

        err = False

        genetic_operators, errored = get_val_from_config(config, 'genetic_operators')
        if errored:
            err = errored

        crossover, errored = get_val_from_config(genetic_operators, 'crossover')
        if errored:
            err = errored

        crossover_opt, errored = get_val_from_config(crossover, 'opt')
        if errored:
            err = errored

        mutation, errored = get_val_from_config(genetic_operators, 'mutation')
        if errored:
            err = errored

        mutation_opt, errored = get_val_from_config(mutation, 'opt')
        if errored:
            err = errored

        selection, errored = get_val_from_config(config, 'selection')
        if errored:
            err = errored

        A, errored = get_val_from_config(selection, 'A')
        if errored:
            err = errored

        B, errored = get_val_from_config(selection, 'B')
        if errored:
            err = errored

        selection_method1, errored = get_val_from_config(selection, 'method1')
        if errored:
            err = errored

        selection_method2, errored = get_val_from_config(selection, 'method2')
        if errored:
            err = errored

        selection_method3, errored = get_val_from_config(selection, 'method3')
        if errored:
            err = errored

        selection_method4, errored = get_val_from_config(selection, 'method4')
        if errored:
            err = errored

        implementation, errored = get_val_from_config(config, 'implementation')
        if errored:
            err = errored

        implementation_opt, errored = get_val_from_config(implementation, 'opt')
        if errored:
            err = errored

        stop, errored = get_val_from_config(config, 'stop')
        if errored:
            err = errored

        stop_opt, errored = get_val_from_config(stop, 'opt')
        if errored:
            err = errored

        # optional
        stop_max_time, _ = get_val_from_config(stop, 'max_time')

        items_dataset, errored = get_val_from_config(config, 'items_dataset')
        if errored:
            err = errored

        items_dataset_path, errored = get_val_from_config(items_dataset, 'path')
        if errored:
            err = errored

        items_dataset_weapons_filename, errored = get_val_from_config(items_dataset, 'weapons_filename')
        if errored:
            err = errored

        items_dataset_boots_filename, errored = get_val_from_config(items_dataset, 'boots_filename')
        if errored:
            err = errored

        items_dataset_helmets_filename, errored = get_val_from_config(items_dataset, 'helmets_filename')
        if errored:
            err = errored

        items_dataset_gloves_filename, errored = get_val_from_config(items_dataset, 'gloves_filename')
        if errored:
            err = errored

        items_dataset_breastplates_filename, errored = get_val_from_config(items_dataset, 'breastplates_filename')
        if errored:
            err = errored

        character_class, errored = get_val_from_config(config, 'character_class')
        if errored:
            err = errored

        initial_population, errored = get_val_from_config(config, 'initial_population')
        if errored:
            err = errored

        if err:
            exit(1)
            
        return Config(crossover_opt, mutation_opt, A, B, selection_method1, selection_method2, selection_method3, selection_method4, implementation_opt, stop_opt, items_dataset_path, items_dataset_weapons_filename, items_dataset_boots_filename, items_dataset_helmets_filename, items_dataset_gloves_filename, items_dataset_breastplates_filename, character_class, initial_population, stop_max_time)

def read_items(path, filename, item_contructor):
    full_path = os.path.join(path, filename)

    try:
        tsv_file = open(full_path)
        read_tsv = csv.reader(tsv_file, delimiter="\t")

        items = []

        i = 0
        for row in read_tsv:
            if i != 0:
                items.append(item_contructor(i-1, float(row[0]), float(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5]))) # TODO: Check whether to use float or FIXED_POINT!
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


