def linear_search(arr, target):
    # 遍历列表的每一个元素及其索引
    for index in range(len(arr)):
        # 检查当前元素是否等于目标值
        if arr[index] == target:
            return index  # 找到目标，返回索引
    return -1  # 遍历结束未找到，返回 -1

# 测试代码
numbers = [4, 2, 7, 1, 9, 5]
target = 10
result = linear_search(numbers, target)

if result != -1:
    print(f"目标数 {target} 的索引是: {result}")
else:
    print(f"目标数 {target} 不在列表中")