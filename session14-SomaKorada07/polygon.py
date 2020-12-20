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
        return self._num_edges

    
    @property
    def num_vertices(self):
        if self._num_vertices is None:
            self._num_vertices = self.num_edges
        return self._num_vertices

    
    @property
    def int_angle(self):
        if self._int_angle is None:
            self._int_angle = (self.num_edges - 2) * (180 / self.num_edges)
        return self._int_angle

    
    @property
    def edge_len(self):
        if self._edge_len is None:
            self._edge_len = 2 * self.circumradius * math.sin(math.pi / self.num_edges)
        return self._edge_len


    @property
    def apothem(self):
        if self._apothem is None:
            self._apothem = self.circumradius * math.cos(math.pi / self.num_edges)
        return self._apothem


    @property
    def area(self):
        if self._area is None:
            self._area = 0.5 * self.edge_len * self.apothem
        return self._area


    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter = self.num_edges * self.edge_len
        return self._perimeter

        
    @num_edges.setter
    def num_edges(self, num_edges):
        if(num_edges < 3):
            raise ValueError("Edge should be greater than 3!")
        else:

            self._num_edges = num_edges
            
            self._num_vertices = None
            
            self._int_angle = None
            
            self._edge_len = None
            
            self._apothem = None
            
            self._area = None
            
            self._perimeter =  None      


    def __repr__(self):
        return f"Polygon class with {self.num_edges} edges, {self.circumradius} circumradius, {self.int_angle} interior angle, {self.edge_len} edge length, {self.apothem} apothem, {self.area} area and {self.perimeter} perimeter"


    def __eq__(self, polygon2):
        if type(polygon2) is not Polygon:
            raise TypeError("Expected type of Polygon.")
        return (self.num_vertices == polygon2.num_vertices and self.circumradius == polygon2.circumradius)


    def __gt__(self, polygon2):
        if type(polygon2) is not Polygon:
            raise TypeError("Expected type of Polygon.")
        return (self.num_vertices > polygon2.num_vertices)