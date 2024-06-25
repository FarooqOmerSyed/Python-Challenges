from collections import Counter


def isanagram(s, t):
    if len(s) != len(t):
        return False

    s_dict = Counter(s)
    t_dict = Counter(t)

    return s_dict == t_dict


print(isanagram('nagaram', 'anagram'))