"""
[Copyright (c) 2014 Josh Willhite]
Repository: https://github.com/Josh-Willhite/Algorithm-Implementation Email: jwillhite@gmail.com

This program is released under the MIT license. See COPYING for specifics.
"""

import random
import pygraphviz as pgv

def matrix_generator(size):
    return [[rb() for i in range(size)] for j in range(size)]

def rb():
    return random.choice([1,0])

def graph_generator(matrix):
    G = pgv.AGraph(directed=False)
    for row in range(len(matrix)):
        G.add_node(str(row))
        for col in range(len(matrix[0])):
            if matrix[row][col]:
                G.add_edge(str(row),str(col))
    G.layout('circo')
    G.draw('graph.png')

#takes N x N matrix returns true if it matches one of the 3 given topologies
def topology_check(matrix):
    row_total = [0 for i in range(len(matrix))]
    col_total = [0 for i in range(len(matrix))]

    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if row == col and matrix[row][col] == 1:
                return False  #node can't be connected to itself
            if not(row == col) and not(matrix[row][col]== matrix[col][row]):
                return False  #verify symmetry

            row_total[row] += matrix[row][col]
            col_total[col] += matrix[row][col]

    if row_total[0] == (len(matrix) - 1) and col_total[0] == [len(matrix) - 1]:
        return True  #star shape topology
    elif all(total == 2 for total in row_total) and all(total == 2 for total in col_total):
        return True  #ring shape topology
    elif all(total == (len(matrix) - 1) for total in row_total) and all(total ==(len(matrix)-1) for total in col_total):
        return True  #net shape, all nodes connected to each other

    return False


def main():
    #m = matrix_generator(4)
    #print m
    print topology_check([  [0,1,0,1],
                            [1,0,0,0],
                            [0,0,0,0],
                            [1,0,0,0]])

main()