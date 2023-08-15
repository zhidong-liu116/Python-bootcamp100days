# Write your code above 👆
with open("file1.txt") as f:
    #lst1 = [int(x) for x in f.read().split()]
    lst1 = []
    for i in f:
        lst1.append(int(i))

with open("file2.txt") as f:
    lst2 = [int(x) for x in f.read().split()]

result = [nums for nums in lst1 if nums in lst2]

print(result)

'''
下面是另一种写法
'''

# Write your code above 👆
with open("file1.txt") as file1:
    #lst1 = [int(x) for x in f.read().split()]
    file1_data = file1.readlines()

with open("file2.txt") as file2:
    # lst2 = [int(x) for x in f.read().split()]
    file2_data = file2.readlines()

result = [int(nums) for nums in file1_data if nums in file2_data]

print(result)


'''
另一个例子，这里的for和miss_states的list comprehension是一样的概念
'''
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
    
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
