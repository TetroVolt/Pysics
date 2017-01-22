#Simple implementation for now
#Vectors are just lists of numbers rightnow
#Eventually gonna make a vector class


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

