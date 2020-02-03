
def b_s_iter(arr, find_val):
    arr_len = len(arr)
    mid_index = int(arr_len / 2)
    mid_value = arr[mid_index]
    itm_found = False

    if find_val == mid_value:
        print("found")

    elif find_val < mid_value:
        for val in range(0, mid_index):
            if arr[val] == find_val:
                print("found")
                itm_found = True
        if not itm_found:
            print("not found")

    elif find_val > mid_value:
        for val in range(mid_index+1,arr_len):
            if arr[val] == find_val:
                print("found")
                itm_found = True
        if not itm_found:
            print("not found")


arr = [10,20,30,40,50,60,70,80,90,100]
b_s_iter(arr,90)
