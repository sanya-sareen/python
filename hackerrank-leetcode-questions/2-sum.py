class TwoSum:
    def two_sum(self, num_list, target_num):
        initial_sum = 0
        for i in range(len(num_list)):
            initial_sum += num_list[i]

            if initial_sum == target_num:
                return initial_sum
       
    def two_sum_hash_map(self, num_list, target_num):
        my_dict = {}
        for i in range(len(num_list)):
            val = target_num - num_list[i]
            if val in my_dict:
                return[i, my_dict[val]]
            my_dict[num_list[i]] = i



t = TwoSum()
num_list = [2,7,11,15]
target_num = 9
# print(t.two_sum(num_list, target_num))
print(t.two_sum_hash_map(num_list, target_num))