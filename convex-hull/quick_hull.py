"""
[Copyright (c) 2014 Josh Willhite]
Repository: https://github.com/Josh-Willhite/Algorithm-Implementation Email: jwillhite@gmail.com

This program is released under the MIT license. See COPYING for specifics.
"""
import math

def quick_hull(generated_points):
    hull = []

    def max_min(all_points):
        min_x_pt = all_points[0]
        max_x_pt = all_points[0]
        for pt in all_points:
            if pt[0] > max_x_pt[0]:
                max_x_pt = pt
            elif pt[0] < min_x_pt[0]:
                min_x_pt = pt
        return [min_x_pt, max_x_pt]

    def get_determinant(a,b,c):
        #x1y2 + x3y1 + x2y3 - x3y2 -x3y1 -x1y3
        return a[0]*b[1] + c[0]*a[1] + b[0]*c[1] - c[0]*b[1] - b[0]*a[1] - a[0]*c[1]

    def get_subset(edge, point_set, side):
        subset = []
        for pt in point_set:
            curr_side = get_determinant(edge[0], edge[1], pt)
            if pt not in edge:
                if side > 0 and curr_side > 0:
                    subset.append(pt)
                if side < 0 and curr_side < 0:
                    subset.append(pt)
                if math.fabs(curr_side) == 0:
                    subset.append(pt)
        return subset

    def get_pivot_point(edge, subset):
        max_distance = 0
        pivot_pt = None
        for pt in subset:
            curr_distance = math.fabs(get_determinant(edge[0],edge[1], pt))
            if (curr_distance > max_distance or curr_distance == 0) and pt not in hull:
                max_distance = curr_distance
                pivot_pt = pt
        return pivot_pt

    def dome(edge, point_set, upper):
        if len(point_set) > 0:
            pivot = get_pivot_point(edge, point_set)

            if pivot is not None:
                hull.append(pivot)
                if edge[0][0] > edge[1][0]:
                    right_edge = [pivot, edge[0]]
                    left_edge = [pivot, edge[1]]
                else:
                    right_edge = [pivot, edge[1]]
                    left_edge = [pivot, edge[0]]
                if upper:
                    right_subset = get_subset(right_edge, point_set, 1)
                    left_subset = get_subset(left_edge, point_set, -1)
                else:
                    right_subset = get_subset(right_edge, point_set, -1)
                    left_subset = get_subset(left_edge, point_set, 1)

                if len(right_subset) > 0:
                    dome(right_edge, right_subset, upper)
                if len(left_subset) > 0:
                    dome(left_edge, left_subset, upper)

    base_edge = max_min(generated_points)
    hull.append(base_edge[0])
    hull.append(base_edge[1])
    upper_hull = get_subset(base_edge, generated_points, 1)
    lower_hull = get_subset(base_edge, generated_points, -1)

    dome(base_edge, upper_hull, True)
    dome(base_edge, lower_hull, False)

    return hull
