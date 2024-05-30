import random as rd

number_of_ecopoints = 60

# Random list of non_repeatable points between 1 and 99
eco_points_list = rd.sample(range(1, 100), number_of_ecopoints)
print(eco_points_list)

with open('eco_points.csv', 'w') as f:
    for eco_point in eco_points_list:
        f.write(f'{eco_point}\n')
