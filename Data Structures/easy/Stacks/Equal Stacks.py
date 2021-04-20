https://www.hackerrank.com/challenges/equal-stacks/problem

def equalStacks(h1, h2, h3):
    # Write your code here
    stacks = [h1[::-1], h2[::-1], h3[::-1]]
    stack_sums = [sum(stacks[i]) for i in range(3)]
    
    while len({stack_sums[i] for i in range(3)}) > 1:  
        tallest_stack = max(stack_sums)
        index = stack_sums.index(tallest_stack)
        removed = stacks[index].pop()
        stack_sums[index] -= removed
    
    return min([sum(stacks[i]) for i in range(3)])


h1 = [3, 2, 1, 1, 1]
h2 = [4, 3, 2]
h3 = [1, 1, 4, 1]

stacks = [h1[::-1], h2[::-1], h3[::-1]]
stack_sums = [sum(stacks[i]) for i in range(3)]
print('stacks',stacks)
print('stack_sums',stack_sums)

# stacks = [[1, 1, 1, 2, 3], [2, 3, 4], [1, 4, 1, 1]] [8, 9, 7]
# stack_sums = 5

