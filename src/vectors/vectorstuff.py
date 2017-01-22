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

def dotProduct(vect1, vect2):
	vect = []
	i = 0
	while i < len(vect1): #assume they are equal lengths
		vect[i] = vect1.comp[i] * vect2.comp[i]
		i += 1
	return vect

def crossProduct(vec1, vec2):
	#Compute determinants
	i = vec1.y*vec2.z - vec2.y*vec1.z
	j = vec1.x*vec2.z-vec2.x*vec1.z
	k = vec1.x*vec2.y-vec2.x*vec1.y
	return [i, -j, k]

#Magnitude of two vectors added
def VecMagApB(vec1, vec2):
	x = vec1.x + vec2.x
	y = vec1.y + vec2.y
	z = vec1.z + vec2.z
	return sqrt(x**2 + y**2 + z**2)

#Magnitude of two vectors subtracted
def VecMagAmB(vec1, vec2):
	x = vec1.x - vec2.x
	y = vec1.y - vec2.y
	z = vec1.z - vec2.z
	return sqrt(x**2 + y**2 + z**2)

#returns angle between two added vectors
def Vec2DAngApB(vec1, vec2):
	x = vec1.x + vec2.x
	y = vec1.y + vec2.y
	return degrees(atan(y/x))

#returns angle between two subtracted vectors
def Vec2DAngAmB(vec1, vec2):
	x = vec1.x - vec2.x
	y = vec1.y - vec2.y
	return degrees(atan(y/x))

"""
	The functions below are for vectors where only the
	magnitude and angle are given
"""

#function for adding two vectors and getting the magnitude
def MagApB(Amag, Aang, Bmag, Bang):
	Aang = radians(Aang)
	Bang = radians(Bang)
	x = Amag*cos(Aang) + Bmag*cos(Bang)
	y = Amag*sin(Aang) + Bmag*sin(Bang)
	return sqrt(x**2 + y**2)

#function for getting angle of new vector when two are added
def AngApB(Amag, Aang, Bmag, Bang):
	Aang = radians(Aang)
	Bang = radians(Bang)
	x = Amag*cos(Aang) + Bmag*cos(Bang)
	y = Amag*sin(Aang) + Bmag*sin(Bang)
	return degrees(atan(y/x))

#function for magnitude of resulting vector from subtracting two
def MagAmB(Amag, Aang, Bmag, Bang):
	Aang = radians(Aang)
	Bang = radians(Bang)
	x = Amag*cos(Aang) - Bmag*cos(Bang)
	y = Amag*sin(Aang) - Bmag*sin(Bang)
	return sqrt(x**2 + y**2)

#function for getting angle resulting vector from subtracting two
def AngAmB(Amag, Aang, Bmag, Bang):
	Aang = radians(Aang)
	Bang = radians(Bang)
	x = Amag*cos(Aang) - Bmag*cos(Bang)
	y = Amag*sin(Aang) - Bmag*sin(Bang)
	return degrees(atan(y/x))
