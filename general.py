""" Klotski sliding puzzle general functions used across all searches """

import copy
SOLUTIONTL = 13
SOLUTIONBR = 18


class GameState:
    """Game State Object"""
    grid = list()
    parents = dict()

    def __init__(self, grid: list):
        self.grid = grid

    # Defining built in methods for the game state class to use the queue library
    def __lt__(self, other: object) -> bool:
        return True

    def __le__(self, other: object) -> bool:
        return False


def read_input(file: str) -> GameState:
    """
    Take a game board as a file input and turn it into a game state
    :param file: Game state as a file input
    :return: File input as a game state
    """
    with open(file) as f:
        lines = f.readlines()
    lst_grid = []
    for x in range(5):
        for y in range(4):
            lst_grid.append(lines[x][y])
    line = ''.join(lst_grid)
    lst_grid = []
    for x in range(20):
        if 1 < int(line[x]) < 7:
            if (x % 4 == 0 and line[x + 1] == line[x]) or (
                    x % 4 == 3 and line[x - 1] == line[x]) or ((0 < x % 4 < 3) and
                                                               line[x + 1] == line[x] or line[
                                                                   x - 1] ==
                                                               line[x]):
                lst_grid.append('2')
            else:
                lst_grid.append('3')
        elif line[x] == '7':
            lst_grid.append('4')
        else:
            lst_grid.append(line[x])
    state = GameState(lst_grid)
    return state


def check_goal_state(state: GameState) -> bool:
    """
    Checking to see if the current state is the goal state
    :param state: The given state
    :return: Goal reached
    """
    return state.grid[SOLUTIONTL] == '1' and state.grid[SOLUTIONBR] == '1'


def create_grid(grid: list, swaps: list) -> list:
    """
    Creating a possible game state by swapping position of pieces
    :param grid: Current game state grid
    :param swaps: The two positions to swap
    :return: The new grid for a new state
    """
    new_grid = copy.copy(grid)
    for swap in swaps:
        new_grid[swap[0]] = grid[swap[1]]
        new_grid[swap[1]] = grid[swap[0]]
    return new_grid


def check_position(index: int) -> tuple:
    """
    Give a coordiante based on the list index
    :param index: List index of a game state grid
    :return: Tuple in the form (row, col)
    """
    if index % 4 == 0:
        column = 0
    elif index % 4 == 1:
        column = 1
    elif index % 4 == 2:
        column = 2
    else:
        column = 3
    if index // 4 == 0:
        row = 0
    elif index // 4 == 1:
        row = 1
    elif index // 4 == 2:
        row = 2
    elif index // 4 == 3:
        row = 3
    else:
        row = 4
    return (row, column)


def get_sequence(state: GameState, explored: dict, start: str) -> str:
    """
    Given a state and a game tree return the file output as listed in A1
    :param start: The starting state
    :param state: The goal state
    :param explored: The dictionary that stores the tree
    :return: A string to be parsed to a file
    """
    # Initializing variables
    s = start
    str1 = ""
    counter = 0
    cur = state_to_string(state)
    states = len(explored)
    # Recursing up the game tree to get the sequence
    while cur != s:
        str1 = cur[0:4] + "\n" + cur[4:8] + "\n" + cur[8:12] + "\n" + cur[12:16] + "\n" + cur[
                                                                                          16:20] \
               + "\n\n" + str1
        cur = explored[cur]
        counter += 1
    # Adding the initial state
    str1 = cur[0:4] + "\n" + cur[4:8] + "\n" + cur[8:12] + "\n" + \
           cur[12:16] + "\n" + cur[16:20] + "\n\n" + str1
    str1 = "Cost of the solution: " + str(counter) + " | Number of states explored: " \
           + str(states) + "\n" + str1
    return str1.rstrip("\n")


def get_results(state: GameState, explored: dict, start: str) -> str:
    """
    Given a state and a game tree return the file output as listed in A1
    :param start: The starting state
    :param state: The goal state
    :param explored: The dictionary that stores the tree
    :return: A string to be parsed to a file
    """
    # Initializing variables
    s = start
    str1 = "Cost of solution: "
    counter = 0
    states = len(explored)
    cur = state_to_string(state)
    # Recursing up the game tree to get the sequence
    while cur != s:
        cur = explored[cur]
        counter += 1
    return str1 + str(counter) + " | Number of states explored: " + str(states)


def print_grid(grid: list) -> None:
    """
    Printing function for testing
    :param grid:
    """
    print(grid[0:4])
    print(grid[4:8])
    print(grid[8:12])
    print(grid[12:16])
    print(grid[16:20])


def state_to_string(state: GameState) -> str:
    """
    Turning a game state into its string repersentation
    :param state: A game state
    :return: That game state repersented as a string
    """
    return ''.join(state.grid)


def find_succesors(state: GameState) -> list:
    """
    Return a list of possible next moves for the current game state
    :param state: Current game state
    :return: A list of future possible game states
    """
    index = []
    x = 0
    states = []
    while len(index) != 2 and x < 20:
        if state.grid[x] == '0':
            index.append(int(x))
        x += 1
    pos1 = check_position(index[0])
    pos2 = check_position(index[1])
    if pos1[0] == pos2[0] and abs(pos1[1] - pos2[1]) == 1:  # Horizontal neighbours
        if pos1[0] < 4:  # Top 4 row
            # First position
            if state.grid[index[0] + 4] == '4':
                states.append(create_grid(state.grid, [(index[0], index[0] + 4)]))
            elif state.grid[index[0] + 4] == '2' and state.grid[index[1] + 4] == '2':
                if index[0] % 4 == 0:
                    states.append(create_grid(state.grid, [(index[0], index[0] + 4), (index[1],
                                                                                      index[
                                                                                          1] + 4)]))
                elif index[0] % 4 == 1:
                    if state.grid[index[0] + 3] == '2':
                        pass
                    else:
                        states.append(create_grid(state.grid, [(index[0], index[0] + 4),
                                                               (index[1], index[1] + 4)]))
                elif index[0] % 4 == 2:
                    if state.grid[index[1] + 3] != '2':
                        states.append(create_grid(state.grid, [(index[0], index[0] + 4),
                                                               (index[1], index[1] + 4)]))
            elif state.grid[index[0] + 4] == '3':
                states.append(create_grid(state.grid, [(index[0], index[0] + 8)]))
            elif state.grid[index[0] + 4] == '1' and state.grid[index[1] + 4] == '1':
                states.append(create_grid(state.grid, [(index[0], index[0] + 8),
                                                       (index[1], index[1] + 8)]))
                # Second position
            if state.grid[index[1] + 4] == '4':
                states.append(create_grid(state.grid, [(index[1], index[1] + 4)]))
            elif state.grid[index[1] + 4] == '3':
                states.append(create_grid(state.grid, [(index[1], index[1] + 8)]))
            else:
                pass
        if pos1[0] > 0:  # Bottom rows
            # First position
            if state.grid[index[0] - 4] == '4':
                states.append(create_grid(state.grid, [(index[0], index[0] - 4)]))
            elif state.grid[index[0] - 4] == '2' and state.grid[index[1] - 4] == '2':
                if index[0] % 4 == 0:
                    states.append(create_grid(state.grid, [(index[0], index[0] - 4),
                                                           (index[1], index[1] - 4)]))
                elif index[0] % 4 == 1:
                    if state.grid[index[0] - 2] == '2':
                        pass
                    else:
                        states.append(create_grid(state.grid, [(index[0], index[0] - 4),
                                                               (index[1], index[1] - 4)]))
                elif index[0] % 4 == 2:
                    if state.grid[index[0] - 5] != '2':
                        states.append(create_grid(state.grid, [(index[0], index[0] - 4),
                                                               (index[1], index[1] - 4)]))
            elif state.grid[index[0] - 4] == '3':
                states.append(create_grid(state.grid, [(index[0], index[0] - 8)]))
            elif state.grid[index[0] - 4] == '1' and state.grid[index[1] - 4] == '1':
                states.append(create_grid(state.grid, [(index[0], index[0] - 8),
                                                       (index[1], index[1] - 8)]))
                # Second position
            if state.grid[index[1] - 4] == '4':
                states.append(create_grid(state.grid, [(index[1], index[1] - 4)]))
            elif state.grid[index[1] - 4] == '3':
                states.append(create_grid(state.grid, [(index[1], index[1] - 8)]))
            else:
                pass
                # Check horizontals
        if pos2[1] < 3:
            if state.grid[index[1] + 1] == '4':
                states.append(create_grid(state.grid, [(index[1], index[1] + 1)]))
            elif state.grid[index[1] + 1] == '2':
                states.append(create_grid(state.grid, [(index[1], index[1] + 2)]))
            else:
                pass
        if pos1[1] > 0:
            if state.grid[index[0] - 1] == '4':
                states.append(create_grid(state.grid, [(index[0], index[0] - 1)]))
            elif state.grid[index[0] - 1] == '2':
                states.append(create_grid(state.grid, [(index[0], index[0] - 2)]))
            else:
                pass
    elif pos1[1] == pos2[1] and abs(pos1[0] - pos2[0]) == 1:  # Vertical neighbours
        # Check verticals
        if pos2[0] < 4:
            if state.grid[index[1] + 4] == '4':
                states.append(create_grid(state.grid, [(index[1], index[1] + 4)]))
            elif state.grid[index[1] + 4] == '3':
                states.append(create_grid(state.grid, [(index[1], index[1] + 8)]))
            else:
                pass
        if pos1[0] > 0:
            if state.grid[index[0] - 4] == '4':
                states.append(create_grid(state.grid, [(index[0], index[0] - 4)]))
            elif state.grid[index[0] - 4] == '3':
                states.append(create_grid(state.grid, [(index[0], index[0] - 8)]))
            else:
                pass
        if pos1[1] < 3:  # Right Side
            # First position
            if state.grid[index[0] + 1] == '4':
                states.append(create_grid(state.grid, [(index[0], index[0] + 1)]))
            elif state.grid[index[0] + 1] == '2':
                states.append(create_grid(state.grid, [(index[0], index[0] + 2)]))
            elif state.grid[index[0] + 1] == '3' and state.grid[index[1] + 1] == '3':
                if index[0] // 4 == 0:
                    states.append(create_grid(state.grid, [(index[0], index[0] + 1),
                                                           (index[1], index[1] + 1)]))
                elif index[0] // 4 == 1:
                    if state.grid[index[0] - 3] == '3':
                        pass
                    else:
                        states.append(create_grid(state.grid, [(index[0], index[0] + 1),
                                                               (index[1], index[1] + 1)]))
                elif index[0] // 4 == 2:
                    if state.grid[index[1] + 5] != '3':
                        states.append(create_grid(state.grid, [(index[0], index[0] + 1),
                                                               (index[1], index[1] + 1)]))
                elif index[0] // 4 == 3:
                    states.append(create_grid(state.grid, [(index[0], index[0] + 1),
                                                           (index[1], index[1] + 1)]))
            elif state.grid[index[0] + 1] == '1' and state.grid[index[1] + 1] == '1':
                states.append(create_grid(state.grid, [(index[0], index[0] + 2),
                                                       (index[1], index[1] + 2)]))
                # Second position
            if state.grid[index[1] + 1] == '4':
                states.append(create_grid(state.grid, [(index[1], index[1] + 1)]))
            elif state.grid[index[1] + 1] == '2':
                states.append(create_grid(state.grid, [(index[1], index[1] + 2)]))
        if pos1[1] > 0:  # Left Side
            # First position
            if state.grid[index[0] - 1] == '4':
                states.append(create_grid(state.grid, [(index[0], index[0] - 1)]))
            elif state.grid[index[0] - 1] == '2':
                states.append(create_grid(state.grid, [(index[0], index[0] - 2)]))
            elif state.grid[index[0] - 1] == '3' and state.grid[index[1] - 1] == '3':
                if index[0] // 4 == 0:
                    states.append(create_grid(state.grid, [(index[0], index[0] - 1),
                                                           (index[1], index[1] - 1)]))
                elif index[0] // 4 == 1:
                    if state.grid[index[0] - 5] == '3':
                        pass
                    else:
                        states.append(create_grid(state.grid, [(index[0], index[0] - 1),
                                                               (index[1], index[1] - 1)]))
                elif index[0] // 4 == 2:
                    if state.grid[index[1] + 3] == '3':
                        pass
                    else:
                        states.append(create_grid(state.grid, [(index[0], index[0] - 1),
                                                               (index[1], index[1] - 1)]))
                elif index[0] // 4 == 3:
                    if state.grid[index[1] - 5] != '3':
                        pass
                    else:
                        states.append(create_grid(state.grid, [(index[0], index[0] - 1),
                                                               (index[1], index[1] - 1)]))
            elif state.grid[index[0] - 1] == '1' and state.grid[index[1] - 1] == '1':
                states.append(create_grid(state.grid, [(index[0], index[0] - 2),
                                                       (index[1], index[1] - 2)]))
                # Second position
            if state.grid[index[1] - 1] == '4':
                states.append(create_grid(state.grid, [(index[1], index[1] - 1)]))
            elif state.grid[index[1] - 1] == '2':
                states.append(create_grid(state.grid, [(index[1], index[1] - 2)]))
            else:
                pass
    else:  # Not neighbors
        for x in index:
            pos = check_position(x)
            # Checking left and right
            if pos[1] < 3:
                if state.grid[x + 1] == '2':
                    states.append(create_grid(state.grid, [(x, x + 2)]))
                elif state.grid[x + 1] == '4':
                    states.append(create_grid(state.grid, [(x, x + 1)]))
            if pos[1] > 0:
                if state.grid[x - 1] == '2':
                    states.append(create_grid(state.grid, [(x, x - 2)]))
                elif state.grid[x - 1] == '4':
                    states.append(create_grid(state.grid, [(x, x - 1)]))

            if pos[0] < 4:
                if state.grid[x + 4] == '3':
                    states.append(create_grid(state.grid, [(x, x + 8)]))
                elif state.grid[x + 4] == '4':
                    states.append(create_grid(state.grid, [(x, x + 4)]))
            if pos[0] > 0:
                if state.grid[x - 4] == '3':
                    states.append(create_grid(state.grid, [(x, x - 8)]))
                elif state.grid[x - 4] == '4':
                    states.append(create_grid(state.grid, [(x, x - 4)]))
    return_states = []
    for state in states:
        return_states.append(GameState(state))
    return return_states
