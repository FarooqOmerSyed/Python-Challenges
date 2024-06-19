def highestAltitude(gain):
    current = 0
    highest = 0
    for x in gain:
        current += x
        highest = max(current, highest)
    return highest


print(highestAltitude([-5,1,5,0,-7]))