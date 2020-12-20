"""
polygonsequence.py
"""

from polygon import Polygon
from functools import lru_cache

class PolySeq:
    def __init__(self, num_edges: "number of edges of largest polygon", circumradius: "common circumradius"):
        self.num_edges = num_edges
        self.circumradius = circumradius


    @property
    def num_edges(self):
        return self._num_edges


    @property
    def circumradius(self):
        return self._circumradius


    @circumradius.setter
    def circumradius(self, circumradius):
        if type(circumradius) not in [float, int]:
            raise TypeError("Circumradius must be a number.")

        if circumradius <= 0:
            raise ValueError("Circumradius must be greater than 0.")

        self._circumradius = circumradius


    @num_edges.setter
    def num_edges(self, num_edges):
        if type(num_edges) is not int:
            raise TypeError("Number of edges must be an integer.")
        if num_edges < 3:
            raise ValueError("Number of edges must be >= 3.")

        self._num_edges = num_edges


    def __len__(self):
        return self._num_edges - 2


    def __getitem__(self, s):
        if isinstance(s, int):
            if s < 0:
                s = self._num_edges - 2 + s
            if s < 0 or s >= (self._num_edges - 2):
                raise IndexError
            else:
                return self.poly(s)
        else:
            start, stop, step = s.indices(self._num_edges - 2)
            rng = range(start, stop, step)
            return [self.poly(i) for i in rng]


    @property
    @lru_cache(1)
    def max_eff_polygon(self):
        return sorted(self, key = lambda x: x.area / x.perimeter)[-1]


    @lru_cache(2 ** 10) 
    def poly(self, n):
        return Polygon(n + 3, self._circumradius)


    def __repr__(self):
        return f"[{[_ for _ in self]}]"