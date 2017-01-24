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

	def __str__(self):
		return "X: {}, Y: {}, Z: {}".format(self.x, self.y, self.z)
	def __add__(self, other):
		return Vector(x = self.x + other.x,y = self.y +other.y,z = self.z + other.z)
	def __sub__(self, other):
		return Vector(x = self.x - other.x, y = self.y - other.y, z = self.z - other.z)
	def __mul__(self, other):
		if isinstance(other, int):
			return Vector(x = other * self.x, y =  other * self.y, z = other * self.z)
		else:
			print("Only Scalar multiplication is currently supported")
			return None
	__rmul__ = __mul__

class VectorFactory:
	def __init__(self):
		pass
	def vectorFromList(self, L):
		while len(L) < 3:
			L.append(0)
		return Vector(x=L[0], y=L[1], z=L[2])
	#this will only be a 2D vector
	def vectorFromMagAndAngle(self, mag, ang):
		ang = radians(ang)
		L = [mag*cos(ang), mag*sin(ang), 0]
		return Vector(x=L[0], y=L[1], z=L[2])



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
	return Vector(i, -j, k)

''' Uses dot product method to calculate angle. acos( (A*B) / (|A||B|) )'''
def angleBetween(vec1, vec2):
	dot = dotProduct(vec1, vec2)
	mag = vec1.getMag() * vec2.getMag()
	return degrees(acos(dot / mag))
