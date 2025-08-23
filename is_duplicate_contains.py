"""a python program to check, if a list of numbers positive contains any duplicates of same"""

from typing import List


def is_duplicates(nums:List[int])->bool:
    set_container = set()
    for num in nums:
        if num in set_container:
            return True   # true for there are duplicates 
        else:
            set_container.add(num)
    
    return False   # flase for if there are no duplicates 


nums = [5,7,3,8,3,9,2,6,3,1,7]
nums_list_two = [4,6,3,1,7]
print(is_duplicates(nums))
print(is_duplicates(nums_list_two))