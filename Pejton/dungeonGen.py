import random

wall = "w"

gridY = random.randint(5, 20)
gridX = random.randint(5, 20)

print(f"grid size: {gridX} x {gridY}")

grid = [["wall" for _ in range(gridX)] for _ in range(gridY)]

for row in grid:
    print("".join(row))

