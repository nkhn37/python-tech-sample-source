"""関数基礎
lambda関数（無名関数）のメリット

[説明ページ]
https://tech.nkhn37.net/python-lambda/#lambda-3
"""


def sum_func_value(val_list1, val_list2, func):
    ret = []
    for v1, v2 in zip(val_list1, val_list2):
        ret.append(func(v1, v2))
    return ret


def main():
    l1 = [1, 2, 3, 4, 5]
    l2 = [6, 7, 8, 9, 10]

    ret_list1 = sum_func_value(l1, l2, lambda val1, val2: val1 + val2)
    print(f'ret_list1 = {ret_list1}')

    ret_list2 = sum_func_value(l1, l2, lambda val1, val2: 2 * val1 + 2 * val2)
    print(f'ret_list2 = {ret_list2}')

    ret_list3 = sum_func_value(l1, l2, lambda val1, val2: 3 * val1 + 3 * val2)
    print(f'ret_list3 = {ret_list3}')


if __name__ == '__main__':
    main()
