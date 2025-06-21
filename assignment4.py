# Define class
class Point:
	def __init__ (self, x, y):
		self.x = x
		self.y = y
	def __eq__ (self, other):
	    return self.x == other.x and self.y == other.y

# Create three points
point1 = Point(3,4)
point2 = Point(3,4)
point3 = Point(4,5)

# Compare the points
print(point1 == point2)
print(point1 == point3)	