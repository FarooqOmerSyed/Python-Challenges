# Euclidean approach
def gcd(a, b):  # start with a,b params
    while b:  # while b is not zero
        a, b = b, a % b  # replace a with b and b with a % b (reminder of a divided by b)
    return a  # when b becomes zero a contents the gcd of two numbers


print(gcd(48, 18))
