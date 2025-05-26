def binary_search(arr, target):
    # 初始化搜索范围的左右边界
    # left从数组的第一个元素(索引0)开始
    # right从数组的最后一个元素(索引len(arr)-1)开始
    left, right = 0, len(arr) - 1
    
    # 当左边界小于等于右边界时继续循环
    # 这表示搜索范围仍然有效
    while left <= right:
        # 计算当前搜索范围的中间位置
        # 使用整数除法(//)确保结果是整数索引
        mid = (left + right) // 2
        
        # 检查中间元素是否等于目标值
        if arr[mid] == target:
            # 如果找到目标值，返回它的索引
            return mid
        # 如果中间元素小于目标值
        elif arr[mid] < target:
            # 调整左边界到中间位置的右侧
            # 因为数组是有序的，目标值只能在右半部分
            left = mid + 1
        # 如果中间元素大于目标值
        else:
            # 调整右边界到中间位置的左侧
            # 因为数组是有序的，目标值只能在左半部分
            right = mid - 1
    
    # 如果循环结束仍未找到目标值
    # 返回-1表示未找到
    return -1
arr = [1,3,4,5,7,8,9,11,14,19,22,23,26]
target = 3
print(f"查找{target}在{arr}中 -> 结果索引: {binary_search(arr, target)} ")