"""
polygon.py
"""

import math

class Polygon():
    def __init__(self, num_edges, circumradius):
        self.circumradius = circumradius
        self.num_edges = num_edges

    @property
    def circumradius(self):
        return self._circumradius

    @circumradius.setter
    def circumradius(self, circumradius):
        self._circumradius = circumradius
        
        
    @property
    def num_edges(self):
        return self._num_vertices

    
    @property
    def num_vertices(self):
        return self._num_vertices

    
    @property
    def int_angle(self):
        return self._int_angle

    
    @property
    def edge_len(self):
        return self._edge_len


    @property
    def apothem(self):
        return self._apothem


    @property
    def area(self):
        return self._area        


    @property
    def perimeter(self):
        return self._perimeter

        
    @num_edges.setter
    def num_edges(self, num_edges):
        self._num_edges = num_edges
        
        self._num_vertices = num_edges
        
        self._int_angle = (self._num_edges - 2) * (180 / self._num_edges)
        
        self._edge_len = 2 * self._circumradius * math.sin(math.pi/self._num_edges)
        
        self._apothem = self._circumradius * math.cos(math.pi/self._num_edges)
        
        self._area = 0.5 * self._edge_len * self._apothem
        
        self._perimeter = self._num_edges * self._edge_len        


    def __repr__(self):
        return f"Polygon class with {self._num_edges} edges, {self._circumradius} circumradius, {self._int_angle} interior angle, {self._edge_len} edge length, {self._apothem} apothem, {self._area} area and {self._perimeter} perimeter"


    def __eq__(self, polygon2):
        if type(polygon2) is not Polygon:
            raise TypeError("Expected type of Polygon.")
        return (self._num_vertices == polygon2._num_vertices and self._circumradius == polygon2._circumradius)


    def __gt__(self, polygon2):
        if type(polygon2) is not Polygon:
            raise TypeError("Expected type of Polygon.")
        return (self._num_vertices > polygon2._num_vertices)