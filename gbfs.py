""" Greedy best first search algorithm """
import queue

from general import check_goal_state, find_succesors, GameState, state_to_string


def manhattan(state: GameState) -> int:
    """
    Heuristic for klotski using manhattan distances
    :param state: Current game state
    :return: Manhattan distance
    """
    str_state = ''.join(state.grid)
    index = str_state.find('1')
    return abs((index % 4) - 2) + abs((index // 4) - 3)


def my_heuristic(state: GameState) -> int:
    """
    Heuristic for klotski using manhattan distances and the number of blocks in way of the goal state
    :param state: Current game state
    :return: Manhattan distance
    """
    str_state = ''.join(state.grid)
    index = str_state.find('1')
    # Manhattan distance
    manhattan_distance = abs((index % 4) - 2) + abs((index // 4) - 3)
    total = 0
    # Calculating num blocks in the goal state
    if state.grid[13] == '4' or state.grid[13] == '2' or state.grid[13] == '3':
        total += 1
    if state.grid[14] == '4' or (state.grid[14] == '2' and state.grid[13] == '2') \
            or state.grid[13] == '3':
        total += 1
    if state.grid[17] == '4' or state.grid[13] == '2':
        total += 1
    if state.grid[19] == '4' or state.grid[19] == '2':
        total += 1
    return total + manhattan_distance


def gbfs(state: GameState, heuristic: bool) -> (GameState, dict, str):
    """
    A star search algorithm
    :param heuristic: Which heuristic function to use
    :param state: Starting state
    :return: Goal State and game tree
    """
    # Initializing variables
    frontier = queue.PriorityQueue()
    explored = {}
    frontier.put((manhattan(state), state))
    current = GameState([])
    counter = 0
    start = state_to_string(state)

    # Exploring the frontier using the gbfs algorithm
    while not frontier.empty():
        current = frontier.get()[1]
        if check_goal_state(current):
            break
        for next in find_succesors(current):
            if state_to_string(next) not in explored:
                explored[state_to_string(next)] = state_to_string(current)
                if heuristic:
                    priority = manhattan(next)
                else:
                    priority = my_heuristic(next)
                frontier.put((priority, next))
        counter += 1
    return current, explored, start
