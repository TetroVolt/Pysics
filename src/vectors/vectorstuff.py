#Simple implementation for now
#Vectors are just lists of numbers rightnow
#Eventually gonna make a vector class
from math import cos, sin, tan, asin, acos, atan, degrees, radians, sqrt

class Vector:
	def __init__(self, x=0, y=0, z=0):
		self.x=x
		self.y = y
		self.z = z
		self.comp=[x,y,z]
	def getMag(self):
		return sqrt(self.x**2+self.y**2+self.z**2)

#returns new
def add(vec1, vec2):
	return Vector(vec1.x + vec2.x, vec1.y + vec2.y, vec1.z + vec2.z)


'''
returns vec1 - vec2
if only 1 vector is given, returns the negation of that vector
'''
def subtract(vec1, vec2 = None):
	if (vec2 == None):
		return Vector(-vec1.x, -vec1.y, -vec1.z)
	return Vector(vec1.x - vec2.x, vec1.y - vec2.y, vec1.z - vec2.z)

def dotProduct(vec1, vec2):
	x = vec1.x * vec2.x
	y = vec1.y * vec2.y
	z = vec1.z * vec2.z
	return x + y + z

def crossProduct(vec1, vec2):
	#Compute determinants
	i = vec1.y*vec2.z - vec2.y*vec1.z
	j = vec1.x*vec2.z - vec2.x*vec1.z
	k = vec1.x*vec2.y - vec2.x*vec1.y
	return Vector(i, j, k)


def magnitude(vec):
	return sqrt(vec.x**2 + vec.y**2 + vec.z**2)

''' Uses dot product method to calculate angle. acos( (A*B) / (|A||B|) )'''
def angleBetween(vec1, vec2):
	dot = dotProduct(vect1, vect2)
	mag1 = magnitude(vect1)
	mag2 = magnitude(vect2)
	return acos(dot / (mag1 * mag2))
