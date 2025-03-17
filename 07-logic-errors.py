def calculate_average(nums):
    sum = 0

    for i in range(len(nums) + 1):
        sum += nums[i]

    avg = sum / len(nums)
    return avg

numbers = [1, 2, 3, 4, 5]
avg = calculate_average(numbers)
print(f"The average is {avg}.")