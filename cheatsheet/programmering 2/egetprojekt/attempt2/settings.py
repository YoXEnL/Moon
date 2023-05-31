# Colors hex codes
DARKGREY = '#1D201F'
WHITE = '#FFFFFF'
RED = '#990000'

# Screen settings
FPS = 60
WIDTH = 600
HEIGHT = 600
TITLE = 'Sliding Puzzle'

# Spel inställningar
GAME_SIZE = 3
TILE_SIZE = 200

# Reference positions
pos = {
    1: [0, 0],
    2: [0, 1],
    3: [0, 2],
    4: [1, 0],
    5: [1, 1],
    6: [1, 2],
    7: [2, 0],
    8: [2, 1],
    9: [2, 2],
}

# Positions grannar, för att kolla ifall den är tom så kollar man genom 
# alla dessa och säger, okej denna är en nolla och kan då flytta dit
ref = {
    1: [
        [0, 1], #2
        [1, 0]  #4
    ], 
    2: [
        [0, 0], #1
        [0, 2], #3
        [1, 1]  #5
        ],
    3: [
        [0, 1], #2
        [1, 2]  #6
    ],
    4: [
        [0, 0], #1
        [1, 1], #5
        [2, 0]  #7
    ],
    5: [
        [0, 1], #2
        [1, 0], #4
        [1, 2], #6
        [2, 1]  #8
    ],
    6: [
        [0, 2], #3
        [1, 1], #5
        [2, 2]  #9
    ],
    7: [
        [1, 0], #4
        [2, 1]  #8
    ],
    8: [
        [1, 1], #5
        [2, 0], #7
        [2, 2]  #9
    ],
    9: [
        [2, 1], #8
        [1, 2]  #6
    ],
}

# Pre-made olösta pussel
shuffled = {
    1: [[2, 0, 1], [8, 3, 4], [7, 5, 6]],
    2: [[8, 1, 3], [6, 2, 4], [7, 0, 5]],
    3: [[7, 0, 5], [6, 4, 1], [8, 1, 3]],
    4: [[8, 0, 4], [5, 7, 3], [6, 2, 1]],
    5: [[6, 3, 4], [1, 2, 7], [0, 5, 8]],
    6: [[6, 0, 8], [3, 5, 4], [1, 2, 7]],
    7: [[1, 0, 3], [6, 5, 8], [7, 4, 2]],
    8: [[0, 7, 3], [8, 4, 2], [1, 5, 6]],
    9: [[6, 4, 3], [7, 2, 1], [5, 0, 8]],
    10: [[8, 6, 5], [2, 4, 3], [1, 7, 0]],
    11: [[8, 3, 4], [2, 5, 1], [7, 0, 6]],
    12: [[3, 6, 5], [2, 4, 7], [0, 1, 8]],
    13: [[7, 0, 8], [1, 5, 4], [2, 6, 3]],
    14: [[4, 2, 8], [1, 0, 6], [7, 5, 3]],
    15: [[1, 0, 3], [6, 4, 7], [5, 2, 8]]
}