import numpy as np
import sympy as sp

def lagrange_grado_1 (x, x0, x1, y0, y1):
    lx0 = (x-x1)/(x0-x1)
    lx1 = (x-x0)/(x1-x0)
    fx = y0 * lx0 + y1 * lx1
    return fx

def lagrange_grado_2 (x, x0, x1, x2, y0, y1, y2):
    lx0 = ((x - x1) * (x - x2)) / ((x0 - x1) * (x0 - x2))
    lx1 = ((x - x0) * (x - x2)) / ((x1 - x0) * (x1 - x2))
    lx2 = ((x - x0) * (x - x1)) / ((x2 - x0) * (x2 - x1))
    fx = y0 * lx0 + y1 * lx1 + y2 * lx2
    return fx

def lagrange_grado_3 (x, x0, x1, x2, x3, y0, y1, y2, y3):
    lx0 = ((x - x1) * (x - x2) * (x - x3)) / ((x0 - x1) * (x0 - x2) * (x0 - x3))
    lx1 = ((x - x0) * (x - x2) * (x - x3)) / ((x1 - x0) * (x1 - x2) * (x1 - x3))
    lx2 = ((x - x0) * (x - x1) * (x - x3)) / ((x2 - x0) * (x2 - x1) * (x2 - x3))
    lx3 = ((x - x0) * (x - x1) * (x - x2)) / ((x3 - x0) * (x3 - x1) * (x3 - x2))
    fx = y0 * lx0 + y1 * lx1 + y2 * lx2 + y3 * lx3
    return fx

def lagrange_grado_4 (x, x0, x1, x2, x3, x4, y0, y1, y2, y3, y4):
    lx0 = ((x - x1) * (x - x2) * (x - x3) * (x - x4)) / ((x0 - x1) * (x0 - x2) * (x0 - x3) * (x0 - x4))
    lx1 = ((x - x0) * (x - x2) * (x - x3) * (x - x4)) / ((x1 - x0) * (x1 - x2) * (x1 - x3) * (x1 - x4))
    lx2 = ((x - x0) * (x - x1) * (x - x3) * (x - x4)) / ((x2 - x0) * (x2 - x1) * (x2 - x3) * (x2 - x4))
    lx3 = ((x - x0) * (x - x1) * (x - x2) * (x - x4)) / ((x3 - x0) * (x3 - x1) * (x3 - x2) * (x3 - x4))
    lx4 = ((x - x0) * (x - x1) * (x - x2) * (x - x3)) / ((x4 - x0) * (x4 - x1) * (x4 - x2) * (x4 - x3))
    fx = y0 * lx0 + y1 * lx1 + y2 * lx2 + y3 * lx3 + y4 * lx4
    return fx