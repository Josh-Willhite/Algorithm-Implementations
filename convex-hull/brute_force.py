"""
[Copyright (c) 2014 Josh Willhite]
Repository: https://github.com/Josh-Willhite/Algorithm-Implementation Email: jwillhite@gmail.com

This program is released under the MIT license. See COPYING for specifics.
"""
def brute_force(points):
    convex_hull = []
    for pt_a in points:
        for pt_b in points:
            on_hull = True
            prev_cross_prod = None
            if pt_a != pt_b:
                for pt_c in points:
                    if pt_c != pt_a and pt_c != pt_b:
                        v1 = [pt_a[0] - pt_b[0], pt_a[1] - pt_b[1]]
                        v2 = [pt_b[0] - pt_c[0], pt_b[1] - pt_c[1]]
                        cross_prod = v1[0]*v2[1] - v2[0]*v1[1]
                        if cross_prod > 0:
                            cross_prod = 1
                        else:
                            cross_prod = -1
                        if cross_prod == prev_cross_prod or type(prev_cross_prod) is type(None) or abs(cross_prod) == 0:
                            prev_cross_prod = cross_prod
                        else:
                            on_hull = False
                            break
                if on_hull and (pt_a not in convex_hull):
                    convex_hull.append(pt_a)
                if on_hull and (pt_b not in convex_hull):
                    convex_hull.append(pt_b)
    return convex_hull
