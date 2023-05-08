def bin8bitStr(m):

  comb = pow(2,m)
  with open('/home/sonali/Downloads/Papers/Power Analysis Attacks/BK_Algo_py_scripts/seed8.txt', 'w') as f1:
    z=0
    for i in range(comb):
        S = ""
        S="{0:08b}".format(i)
        
        for i in range(len(S)):
            z = z + int(S[i])

        #S = S + '\n'
        if z!=0:
    
            f1.write(S) 
  f1.close()

def bin3bitStr(n):
    comb = pow(2,n)
    with open('/home/sonali/Downloads/Papers/Power Analysis Attacks/BK_Algo_py_scripts/seed3.txt', 'w') as f2:
        z=0
        for i in range(comb):

            S = ""
            S="{0:03b}".format(i)
            
            for i in range(len(S)):
                z = z + int(S[i])

            #S = S + '\n'
            if z!=0:
        
                f2.write(S)            
    f2.close()

def bin4bitStr(n):
    comb = pow(2,n)
    with open('/home/sonali/Downloads/Papers/Power Analysis Attacks/BK_Algo_py_scripts/seed4.txt', 'w') as f3:
        z=0
        for i in range(comb):

            S = ""
            S="{0:04b}".format(i)
            
            for i in range(len(S)):
                z = z + int(S[i])

           # S = S + '\n'
            if z!=0:
        
                f3.write(S)            
    f3.close()

def bin5bitStr(n):
    comb = pow(2,n)
    with open('/home/sonali/Downloads/Papers/Power Analysis Attacks/BK_Algo_py_scripts/seed5.txt', 'w') as f4:
        z=0
        for i in range(comb):

            S = ""
            S="{0:05b}".format(i)
            
            for i in range(len(S)):
                z = z + int(S[i])

            #S = S + '\n'
            if z!=0:
        
                f4.write(S)            
    f4.close()

def bin6bitStr(n):
    comb = pow(2,n)
    with open('/home/sonali/Downloads/Papers/Power Analysis Attacks/BK_Algo_py_scripts/seed6.txt', 'w') as f5:
        z=0
        for i in range(comb):

            S = ""
            S="{0:06b}".format(i)
            
            for i in range(len(S)):
                z = z + int(S[i])

            #S = S + '\n'
            if z!=0:
        
                f5.write(S)            
    f5.close()

def bin7bitStr(n):
    comb = pow(2,n)
    with open('/home/sonali/Downloads/Papers/Power Analysis Attacks/BK_Algo_py_scripts/seed7.txt', 'w') as f6:
        z=0
        for i in range(comb):

            S = ""
            S="{0:07b}".format(i)
            
            for i in range(len(S)):
                z = z + int(S[i])

            #S = S + '\n'
            if z!=0:
        
                f6.write(S)            
    f6.close()


#driver code
m= input("Enter 8")
bin8bitStr(m)
n= input("Enter 3")
bin3bitStr(n)
n= input("Enter 4")
bin4bitStr(n)
n= input("Enter 5")
bin5bitStr(n)
n= input("Enter 6")
bin6bitStr(n)
n= input("Enter 7")
bin7bitStr(n)
