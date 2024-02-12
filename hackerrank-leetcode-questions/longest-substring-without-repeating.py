def unique_chars(str):
    return len(set(str)) == len(str)

def brute_force_approach(substring):
    size = len(substring)
    max_len = 0
    result_string = ""

    for i in range(size):
        for j in range(i, size):
            substring = str[i:j+1]
            print(substring)
            if unique_chars(substring):
                if(len(substring) > max_len):
                    result_string = substring
                    max_len = len(substring)

    return result_string

str = "abcbcbb"
print(brute_force_approach(str))
