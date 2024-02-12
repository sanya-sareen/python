def occurrence(nums):
    my_dict = {}
    for i in range(len(nums)):
        my_dict[nums[i]] = my_dict.get(nums[i],0) + 1
    return my_dict


def occurrence_using_count(nums):
    counting = {x:nums.count(x) for x in nums}
    return counting



nums = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]

print(occurrence(nums))
print("Occurrence using count:-",occurrence_using_count(nums))
