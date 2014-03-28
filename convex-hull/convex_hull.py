"""
[Copyright (c) 2014 Josh Willhite]
Repository: https://github.com/Josh-Willhite/Algorithm-Implementation Email: jwillhite@gmail.com

This program is released under the MIT license. See COPYING for specifics.
"""
import matplotlib.pyplot as plt
import quick_hull as qh
import brute_force as bf
import random
import time


def plot(points, convex_hull, min, max):

    for pt in points:
        plt.plot(pt[0], pt[1], 'ro')
    for pt in convex_hull:
        plt.plot(pt[0], pt[1], 'bo')

    plt.axis([min+.1*min, max+.1*max, min+.1*min, max+.1*max])
    plt.show()


def generate_points(min, max, total):
    points = [[random.choice(range(min,max)), random.choice(range(min,max))] for i in range(total)]
    return points

if __name__ == '__main__':
    min_val = -100000
    max_val = 100000
    total_points = 500

    start = time.time()
    points = generate_points(min_val, max_val, total_points)
    end = time.time()
    print("generated data in %g seconds" % (end - start))

    '''
    start_time = time.time()
    BF_hull = bf.brute_force(points)
    end_time = time.time()
    print("BruteForce took: %g seconds" % (end_time - start_time))
    '''
    start_time = time.time()
    q_hull = qh.quick_hull(points)
    end_time = time.time()
    print("QuickHull took: %g seconds" % (end_time - start_time))

    plot(points, q_hull, min_val, max_val)



