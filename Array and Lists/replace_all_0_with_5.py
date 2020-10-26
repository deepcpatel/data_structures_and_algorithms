# Link: https://practice.geeksforgeeks.org/problems/replace-all-0s-with-5/1/

# Approach: Extract digits from last from num and add that to a new number by replacing all 5s

# Function should return an integer value
def convertFive(n):
    num, tens = 0, 1
    while n != 0:
        d, n = n%10, n//10
        
        if d == 0:
            d = 5
        num += tens*d
        tens *= 10
    return num