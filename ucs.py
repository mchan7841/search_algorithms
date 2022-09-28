""" Uniform Cost Search """
import queue

from general import check_goal_state, find_succesors, GameState, state_to_string


def ucs(state: GameState) -> (GameState, dict, str):
    """
    Ucs search algorithm
    :param state: Starting state
    :return: Goal State and game tree
    """
    # Initializing variables
    frontier = queue.PriorityQueue()
    explored = {}
    cost = {}
    frontier.put((0, state))
    cost[state_to_string(state)] = 0
    current = GameState([])
    counter = 0
    start = state_to_string(state)

    # Exploring the frontier using an A* algorithm
    while not frontier.empty():
        current = frontier.get()[1]
        if check_goal_state(current):
            break
        for next in find_succesors(current):
            if state_to_string(next) not in explored:
                explored[state_to_string(next)] = state_to_string(current)
                new_cost = cost[state_to_string(current)] + 1
                cost[state_to_string(next)] = new_cost
                priority = new_cost
                frontier.put((priority, next))
        counter += 1
    return current, explored, start
