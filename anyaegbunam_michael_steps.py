def feet_to_steps(feet):
    steps = int(feet / 2.5)
    return steps

distance_in_feet = float(input('Please enter the distance travelled on foot: '))
distance_traveled = feet_to_steps(distance_in_feet)

print(f'{distance_traveled} steps')

