"""
polygonsequence.py
"""

from polygon import Polygon
from functools import lru_cache

class PolySeq:
    def __init__(self, m, R):
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._R = R
        self._polygons = []
        
    def __len__(self):
        return self._m - 2
    
    def __iter__(self):
        return self.PolygonIterator(self)
    
    def __repr__(self):
        return f'PolySeq(m = {self._m}, R = {self._R})'
    
    @property
    def max_efficiency_polygon(self):
        sorted_polygons = sorted(self._polygons, 
                                 key = lambda p: p.area / p.perimeter,
                                reverse = True)
        return sorted_polygons[0]
    
    class PolygonIterator:
        def __init__(self, polygon_obj):
            self._polygon_obj = polygon_obj
            self._index = 0
            
        def __iter__(self):
            return self
        
        def __next__(self):
            if self._index > self._polygon_obj._m:
                raise StopIteration
            else:
                if self._index < 3 :
                    self._index += 1
                    return 0
                
                p = Polygon(self._index, self._polygon_obj._R)
                self._polygon_obj._polygons.insert(self._index, p)
                self._index += 1
                return p.area / p.perimeter