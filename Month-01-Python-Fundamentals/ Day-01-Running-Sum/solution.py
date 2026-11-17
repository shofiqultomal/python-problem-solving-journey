def running_sum(nums):
    total = 0
    result = []

    for num in nums:
        total += num
        result.append(total)

    return result


# Input
numbers = [1, 2, 3, 4]

# Function Call
answer = running_sum(numbers)

# Output
print("Final Result:", answer)