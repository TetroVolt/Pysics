#Simple implementation for now
#Vectors are just lists of numbers rightnow
#Eventually gonna make a vector class
from math import cos, sin, tan, asin, acos, atan, degrees, radians, sqrt

import math

def dotProduct(vect1, vect2):
	vect = []
	i = 0
	while i < len(vect1): #assume they are equal lengths
		vect[i] = vect1[i] * vect2[i]
		i += 1
	return vect

#only works for 3D vectors
def crossProduct(vect1, vect2):
	#Compute determinants
	i = vect1[1]*vect2[2] - vect2[1]*vect1[2]
	j = vect1[0]*vect2[2] - vect2[0]*vect1[2]
	k = vect1[0]*vect2[1] - vect2[0]*vect1[1]
	return [i, -j, k]

def magnitude(vect):
	mag = 0
	for i in vect:
		mag += i**2
	return math.sqrt(mag)

def angleBetween(vect1, vect2):
	dot = dotProduct(vect1, vect2)
	mag1 = magnitude(vect1)
	mag2 = magnitude(vect2)
	return acos(dot / (mag1 * mag2))


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
