# Sequence Types I

### Assignment

A regular strictly convex polygon is a polygon that has the following characteristics:

1. all interior angles are less than 180
2. all sides have equal length

**Objective 1:**

1. Create a Polygon Class:
   1. where initializer takes in:
      1. number of edges/vertices
      2. circumradius
   2. that can provide these properties:
      1. \# edges
      2. \# vertices
      3. interior angle
      4. edge length
      5. apothem
      6. area
      7. perimeter
   3. that has these functionalities:
      1. a proper `__repr__` function
      2. implements equality (==) based on # vertices and circumradius (`__eq__`)
      3. implements > based on number of vertices only (`__gt__`)

**Objective 2:**

1. Implement a Custom Polygon sequence type:
   1. where initializer takes in:
      1. number of vertices for largest polygon in the sequence
      2. common circumradius for all polygons
   2. that can provide these properties:
      1. max efficiency polygon: returns the Polygon with the highest **area: perimeter** ratio
   3. that has these functionalities:
      1. functions as a sequence type (`__getitem__`)
      2. supports the len() function (`__len__`)
      3. has a proper representation (`__repr__`)