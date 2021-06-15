
# Sets

nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3}& nums
nums = filter(lambda x: x> 1, nums)
print(len(list(nums)))

# What is the answer here 

# nums = {1, 2, 3, 4, 5, 6} &
# nums = {0, 1, 2, 3}
# nums = {1, 2, 3}

#nums = filter(lambda x: x > 1, nums)
#list(nums)= [2, 3]
#print(len(list(nums)))
#(len(list(2)))

def power(x, y):
	if y == 0:
		return 1
	else:
		return x* power(x, y-1)
print(power(2, 3))

# Recursion principle 2 to the power of 3

# y-1 so it minkes by one 2 to the power of two, 2*1, 2*0
# 0 base case + operatione ended.
