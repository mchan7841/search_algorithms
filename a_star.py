""" A* search algorithm """
import queue

from gbfs import manhattan, my_heuristic
from general import check_goal_state, find_succesors, GameState, state_to_string


def a_star(state: GameState, heuristic: bool) -> (GameState, dict, str):
    """
    A star search algorithm
    :param heuristic: Which heuristic function to use
    :param state: Starting state
    :return: Goal State and game tree
    """
    # Initializing variables
    frontier = queue.PriorityQueue()
    explored = {}
    cost = {}
    frontier.put((manhattan(state), state))
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
                if heuristic:
                    priority = manhattan(next) + new_cost
                else:
                    priority = my_heuristic(next) + new_cost
                frontier.put((priority, next))
        counter += 1
    return current, explored, start
