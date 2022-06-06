import math
def calculate_paint(witdh, height, coverage):
    """
    Calculate the amount of paint needed to paint the walls
    """
    area = witdh * height
    return math.ceil(area / coverage)

print(calculate_paint(10, 20, 5))