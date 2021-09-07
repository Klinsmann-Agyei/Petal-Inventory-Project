import codecademylib
import pandas as pd
inventory = pd.read_csv('inventory.csv')
staten_island = inventory.head(10)
product_request = staten_island.product_description
seed_request = inventory[inventory.location == 'Brooklyn']
#inventory['in_stock'] = inventory.apply(lambda row: True if inventory.quantity > 0 else False, axis = 1)
print(inventory.head())
inventory['total_value'] = inventory.apply(lambda row: inventory.price * inventory.quantity, axis = 1)
combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)
inventory['full_description'] = inventory.apply(combine_lambda)
