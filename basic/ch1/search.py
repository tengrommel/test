def linear_search(list_ex, val):
    for index, value in enumerate(list_ex):
        if val == value:
            return index
    else:
        return None


if __name__ == '__main__':
    print(linear_search([1,2,3], 1))