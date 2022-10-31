def is_consecutive(a_list):
    for index in range(len(a_list)-1): #subtract minus one from the length of the list to avoid an invalid index of a_list[5]
        if a_list[index] + 1 != a_list[index + 1]:
            return False
    return True #if the code block never returns False and ends the function (due to being non-consecutive), the list is therefore assumed to be consecutive, and True is returned at after the for loop has completed.

print(is_consecutive([2,3,4,5]))