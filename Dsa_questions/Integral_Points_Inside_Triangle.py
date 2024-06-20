# Integral Points Inside Triangle

import math

class Solution:
    def InternalCount(self, p, q, r):
        # Calculate the area of the triangle using integer arithmetic
        double_area =  abs(p[0] * (q[1] - r[1]) + q[0] * (r[1] - p[1]) + r[0] * (p[1] - q[1]))
        
        # Calculate the number of lattice points on each boundary segment
        Boundry_PQ = math.gcd(abs(p[0] - q[0]), abs(p[1] - q[1]))
        Boundry_QR = math.gcd(abs(q[0] - r[0]), abs(q[1] - r[1]))
        Boundry_RP = math.gcd(abs(r[0] - p[0]), abs(r[1] - p[1]))
        
        # Total boundary points, including vertices, but each segment's endpoints are counted only once
        Boundry = Boundry_PQ + Boundry_QR + Boundry_RP
        
        # Apply Pick's theorem to find the number of internal lattice points
        # Pick's theorem: A = I + B/2 - 1
        # Rearranged to find I: I = A - B/2 + 1
        internal_points = (double_area - Boundry + 2) // 2
        
        return int(internal_points)

