# formatting using concantenation, format method and f-string
weight = 0.2
animal = 'newt'

print(str(weight) + " kg is the weight of the " + animal)

print("{} kg is the weight of the {}" .format(weight, animal))

print(f"{weight} kg is the weight of the {animal}")