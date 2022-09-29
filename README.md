# Overview

## Game
Klotski is a simple wooden sliding block puzzle game originating from the 2oth century. In the case of this project, Klotski refers to a specific layout of 10 blocks where the goal is to move the largest block out of the board. In this configuration, there is 1 2x2 block, 5 1x2 blocks, 4 1x1 blocks, and two empty spaces in a 3x5 grid. To get the special 2x2 piece to the goal, the empty spaces must be manipulated to slide the rest of the blocks out of the way.

<p align="center">
  <img width="240" height="300" src="klotski.png">
</p>

## Notation and Formatting

### Input Formatting
The input format for this program is a text file with five lines and four numbers on each line (no spaces). 0 represents an empty space, 1 represents 1/4 of the 2x2 piece, 2-6 repersent 1/2 of a 1x2 piece and 7 represents a 1x1 piece. An example of this format can be found in start_state.txt.

### Output Formatting
The output format for this program is similar to the input with five lines and four numbers on each line (no spaces). However, 0 represents an empty space, 1 represents 1/4 of the 2x2 piece, 2 repersent 1/2 of a 1x2 pieces that are horizontal, 3 reperents 1/2 of the 1x2 pieces that are vertical, and 7 represents a 1x1 piece. The outputs are formatted with the cost of the solution (the number of steps to reach the goal) and the number of states explored to reach the goal at the top. This is then followed by the sequence of moves the algorithm used to get to the goal. An example of this format can be found in any of the output files.

## Running the program
This program can be run with the following code below in the command line (when you are in the directory with main.py). It will create 7 different text files, one for each search and different heuristics that will store the ouput of the different search algorithms. The text files for the outputs can be renamed if desired however the search outputs are mapped to the text files in the order shown in the code. All of the outputs are labeled as the search function and the reason there are two A* outputs is the use of different heuristic functions.
```
python3 main.py input.txt dfs_ouput.txt ids_ouput.txt bfs_output.txt ucs_output.txt gbfs_output.txt a_star_ouput.txt my_a_star_output.txt
```

## Search Pseudo Code
All of the algorithms implemented for this project are based on the basic search algorithm shown below:
```
Successor_States(State) -> list[States]:
  return list of possible next states
  
Goal_Test(State) -> bool:
  return [if state is the goal state]
  
Search(Intial_State) -> Final_State:
  frontier = [intial state]
  while frontier is not empty:
    select and remove state current from frontier
    if Goal_Test(current):
      return current
    frontier.add(Successor_States(current))
  return no solution
```

# Uninformed Search Algorithms

## Depth-First Search

## Iterative Depth First Search

## Breadth-First Search

## Uniform Cost Search

# Heuristic Search Algorithms

## Heuristics

## Greedy Breadth-First Search

## A* Search

# References
