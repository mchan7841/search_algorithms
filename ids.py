""" """
import queue

from general import check_goal_state, find_succesors, GameState, state_to_string


def ids(state: GameState) -> (GameState, dict, str):
    """
    Iterative depth first search algorithm
    :param state: Starting state
    :return: Goal State and game tree
    """
    found = False
    limit = 0
    explored = {}
    current = GameState([])
    start = state_to_string(state)
    while not found:
        # Initializing variables
        frontier = queue.LifoQueue()
        explored = {}
        limit_dict = {state_to_string(state): 0}
        frontier.put(state)
        current = GameState([])
        # Exploring the frontier using an dfs algorithm
        while not frontier.empty():
            current = frontier.get()
            if check_goal_state(current):
                found = True
                break
            elif limit_dict[state_to_string(state)] == limit:
                break
            for next in find_succesors(current):
                if state_to_string(next) not in explored:
                    explored[state_to_string(next)] = state_to_string(current)
                    frontier.put(next)
                    limit_dict[state_to_string(next)] = limit_dict[state_to_string(current)] + 1
    return current, explored, start
