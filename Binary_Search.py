

def binary_search(b_list,item):
    first = 0
    last = len(b_list) - 1

    while first <= last:
        mid_point = (first + last) // 2
        if b_list[mid_point] == item:
            return True
        else:
            if item < b_list[mid_point]:
                last = mid_point - 1
            else:
                first = mid_point + 1
    return False

def binary_search_rec(b_list, start, end, item):
    if len(b_list) == 0:
        return False
    else:
        mid_point = (start+end) // 2
        if b_list[mid_point] == item:
            return True
        else:
            if item < b_list[mid_point]:
                end = mid_point - 1
                return binary_search_rec(b_list, start, end, item)
            else:
                start = mid_point + 1
                return binary_search_rec(b_list, start, end, item)



if __name__ == '__main__':
    a_list = [1, 4, 7, 10, 14, 19, 102, 2575, 10000]
    print("Binary search : ",binary_search(a_list, 4))
    print("Binary search Recursive : ",binary_search_rec(a_list, 0, len(a_list) -1 ,4))
    