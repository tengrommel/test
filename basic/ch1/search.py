def linear_search(list_ex, val):
    for index, value in enumerate(list_ex):
        if val == value:
            return index
    else:
        return None


def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right:
        # 候选区有值
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            # 待查找的值在mid左侧
            right = mid - 1
        else:
            # li[mid] < val 待查找的值在mid右侧
            left = mid + 1
    else:
        return None


if __name__ == '__main__':
    # print(linear_search([1,2,3], 1))
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binary_search(li, 3))
