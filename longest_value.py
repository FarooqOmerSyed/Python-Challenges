def longest_value(fruits: dict):
    max_key = max(fruits, key=lambda x: len(fruits[x]))
    return fruits[max_key]


print(longest_value({'fruits': 'apple', 'color': 'green'}))

# takes dictionary as an argument and return first longest value
