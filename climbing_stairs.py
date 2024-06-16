def climbStairs(n):
    # Base cases for 0 and 1 step
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Initialize variables to store the ways to climb for 1 step and 2 steps
    one_step = 1
    two_steps = 1

    # Loop through each step starting from the 3rd step
    for i in range(2, n + 1):
        # Calculate the total ways to reach the current step by adding the ways from previous 1 step and 2 steps
        current = one_step + two_steps
        # Update one_step and two_steps for the next iteration
        two_steps = one_step
        one_step = current

    return one_step


# Test the function with n = 5
n = 5
print(climbStairs(n))
