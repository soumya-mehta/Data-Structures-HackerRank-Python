#specifying matrix dimensions
n = 6
#empty list to store all the 16 hourglass sum
m = []

#for compiling all 16 hourglass sum  values into the list m 
for i in range(n):
    m.append(list(map(int, input().split()[:n])))
    
#defining a function for summation of the hourglass values
def sum_glass(m, i, j):
    # return the sum of the elements in the hourglass
    return sum(m[i][j:j+3]) + m[i+1][j+1] + sum(m[i+2][j:j+3])

#initialize by storing negative inifinity into INTEGER variable and update it with the maximum value
INTEGER = float("-inf")
for i in range(4):
    for j in range(4):
        s = sum_glass(m, i, j)
        if s > INTEGER:
            INTEGER = s
            
print (INTEGER)
