import random

wall = "w"
floor = "."

def generateGrid():
    gridY = random.randint(10, 20)
    gridX = random.randint(10, 20)

    print(f"grid size: {gridX} x {gridY}")

    grid = [[wall for _ in range(gridX)] for _ in range(gridY)]
    return grid



def rooms_overlap(x1, y1, w1, h1, x2, y2, w2, h2, buffer=1):
    """Check if two rooms overlap, including a buffer space around them."""
    return (
        x1 < x2 + w2 + buffer and  # Left edge of room1 is left of room2’s right edge
        x1 + w1 + buffer > x2 and  # Right edge of room1 is right of room2’s left edge
        y1 < y2 + h2 + buffer and  # Top edge of room1 is above room2’s bottom edge
        y1 + h1 + buffer > y2      # Bottom edge of room1 is below room2’s top edge
    )

def add_room(grid, max_rooms=5, min_size=3, max_size=6, max_attempts=50):
    """ Adds random rooms to the dungeon, ensuring no overlaps. """
    rooms = []  # Store valid room positions

    for _ in range(max_rooms):
        attempts = 0
        while attempts < max_attempts:  # Limit attempts to avoid infinite loops
            room_width = random.randint(min_size, max_size)
            room_height = random.randint(min_size, max_size)

            x = random.randint(1, len(grid[0]) - room_width - 1)
            y = random.randint(1, len(grid) - room_height - 1)

            # Check if the new room overlaps with existing rooms
            if any(rooms_overlap(x, y, room_width, room_height, rx, ry, rw, rh) for rx, ry, rw, rh in rooms):
                attempts += 1  # Try again with a new position
                continue  # Skip to next iteration
            
            # If no overlap, place the room
            for i in range(y, y + room_height):
                for j in range(x, x + room_width):
                    grid[i][j] = floor

            # Store the room
            rooms.append((x, y, room_width, room_height))
            break  # Stop trying after successfully placing a room

    return rooms

dungeon = generateGrid()
rooms = add_room(dungeon)

for row in dungeon:
    print("".join(row))

# I have no idea whats going on I trying to understand this but I have no idea but it works somehow so ig is fine