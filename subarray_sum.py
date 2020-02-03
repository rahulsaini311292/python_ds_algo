#code

def get_sub_array_sum(arr,total):
    start_elem = 0
    end_elem = 0
    res_sum = 0
    for i in range(0, len(arr)):
        res_sum = 0
        start_elem = arr[i]
        for j in range(i, len(arr)):
            if res_sum == total:
                break
            else:
                res_sum = res_sum + arr[j]
                end_elem = arr[j]
        if res_sum == total:
            break
    if res_sum != total:
        print(-1)
    else:
        print(arr.index(start_elem) + 1, arr.index(end_elem) + 1)

my_arr = [1,2,3,7,5]
my_arr2 = [1,2,3,4,5,6,7,8,9,10]
my_arr3 = [135,101, 170, 125, 79, 159, 163, 65, 106, 146, 82, 28, 162, 92, 196, 143, 28, 37, 192, 5, 103, 154, 93, 183,
           22, 117, 119, 96, 48, 127, 172, 139, 70, 113, 68, 100, 36, 95, 104, 12, 123, 134]
my_arr4 = [142, 112, 54, 69, 148, 45, 63, 158, 38, 60, 124, 142, 130, 179, 117, 36, 191, 43, 89, 107, 41, 143, 65, 49,
           47, 6, 91, 130, 171, 151, 7, 102, 194, 149, 30, 24, 85, 155, 157, 41, 167, 177, 132, 109, 145, 40, 27, 124,
           138, 139, 119, 83, 130, 142, 34,116, 40, 59, 105, 131, 178, 107, 74, 187, 22, 146, 125, 73, 71, 30, 178, 174,
           98, 113]
get_sub_array_sum(my_arr,12)
get_sub_array_sum(my_arr2,15)
get_sub_array_sum(my_arr3,468)
# get_sub_array_sum(my_arr4,20)
