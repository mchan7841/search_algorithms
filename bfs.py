""" Breadth first search algorithm """
import queue

from general import check_goal_state, find_succesors, GameState, state_to_string


def bfs(state: GameState) -> (GameState, dict, str):
    """
    Breadth first search algorithm
    :param state: Starting state
    :return: Goal State and game tree
    """
    # Initializing variables
    frontier = queue.Queue()
    explored = {}
    frontier.put(state)
    current = GameState([])
    start = state_to_string(state)
    # Exploring the frontier using an dfs algorithm
    while not frontier.empty():
        current = frontier.get()
        if check_goal_state(current):
            break
        for next in find_succesors(current):
            if state_to_string(next) not in explored:
                explored[state_to_string(next)] = state_to_string(current)
                frontier.put(next)
    return current, explored, start
