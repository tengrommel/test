# 小分堆
def sift(li, low, high):
    """
    :param li:列表
    :param low: 堆的根节点位置
    :param high: 堆的最后一个元素的位置
    :return:
    """
    i = low
    # i最开始指向根节点
    j = 2 * i + 1
    # j开始是左孩子
    tmp = li[low]
    # 把堆顶存起来
    while j <= high:
        # 只要j位置有数
        if j + 1 <= high and li[j + 1] < li[j]:
            # 如果右孩子有并且比较大
            j = j + 1
            # j指向右孩子
        if li[j] < tmp:
            li[i] = li[j]
            i = j
            # 往下看一层
            j = 2 * i + 1
        else:
            # tmp更大，把tmp放到i的位置上
            li[i] = tmp  # 把tmp放到某一级位置上
            break
    else:
        li[i] = tmp
        # 把tmp放到叶子节点上


def topk(li, k):
    heap = li[0:k]
    for i in range((k-2)//2, -1, -1):
        sift(heap, i, k-1)
    # 建堆
    for i in range(k, len(li)-1):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k-1)
    # 遍历
    for i in range(k-1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(li, 0, i-1)
    return heap


if __name__ == '__main__':
    import random
    li = list(range(1000))
    random.shuffle(li)
    print(topk(li, 10))