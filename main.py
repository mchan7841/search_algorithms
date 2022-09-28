""" """
import sys

from a_star import a_star
from bfs import bfs
from dfs import dfs
from gbfs import gbfs
from ids import ids
from general import get_sequence, read_input, get_results
from ucs import ucs

if __name__ == '__main__':
    filename = sys.argv[1]
    dfs_goal_state, dfs_tree, dfs_start = dfs(read_input(filename))
    ids_goal_state, ids_tree, ids_start = ids(read_input(filename))
    bfs_goal_state, bfs_tree, bfs_start = bfs(read_input(filename))
    ucs_goal_state, ucs_tree, ucs_start = ucs(read_input(filename))
    gbfs_goal_state, gbfs_tree, gbfs_start = gbfs(read_input(filename), True)
    a_goal_state, a_tree, a_start = a_star(read_input(filename), True)
    my_a_goal_state, my_a_tree, my_a_start = a_star(read_input(filename), False)
    with open(sys.argv[2], 'w') as sys.stdout:
        print(get_sequence(dfs_goal_state, dfs_tree, dfs_start))
    with open(sys.argv[3], 'w') as sys.stdout:
        print(get_sequence(ids_goal_state, ids_tree, ids_start))
    with open(sys.argv[4], 'w') as sys.stdout:
        print(get_sequence(bfs_goal_state, bfs_tree, bfs_start))
    with open(sys.argv[5], 'w') as sys.stdout:
        print(get_sequence(ucs_goal_state, ucs_tree, ucs_start))
    with open(sys.argv[6], 'w') as sys.stdout:
        print(get_sequence(gbfs_goal_state, gbfs_tree, gbfs_start))
    with open(sys.argv[7], 'w') as sys.stdout:
        print(get_sequence(a_goal_state, a_tree, a_start))
    with open(sys.argv[8], 'w') as sys.stdout:
        print(get_sequence(my_a_goal_state, my_a_tree, my_a_start))
