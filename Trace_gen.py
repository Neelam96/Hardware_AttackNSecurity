# Python program for random binary string generation
### In order to create seed randomly, make sure that the seed should never be all zero string

import random


# Function to create the random binary string
def rand_seed(p):

	# Variable to store the string
	key1 = ""

	# Loop to find the string of desired length
	for i in range(p):
		
		# randint function to generate 0, 1 randomly and converting the result into str
		temp = str(random.randint(0, 1))

		# Concatenation the random 0, 1 to the final result
		key1 += temp
        
	return(key1)

# Driver Code
n = input("enter any number")
comb = pow(2,n) 
for k in range(comb):
    str1 = rand_seed(n)
    z=0
    for j in range(len(str1)):
        z = z + int(str1[j])
    if z != 0:
        for i in range(n):
            seed =''
            seed = ("%s%s" % (str1,'\n'))
        with open('/home/sonali/Downloads/Papers/Power Analysis Attacks/BK_Algo_py_scripts/seed1.txt', 'a') as f1: 
            f1.writelines(seed)
    f1.close()
    print("Desired length random binary string is: ", seed)
