"""
题号：001
题目：两数之和
难度：Easy
核心考点：列表遍历、哈希表
适配场景：三维重建-特征点坐标匹配、点云邻域查找
解题思路：用哈希表存储已遍历元素的索引，一次遍历完成查找，时间复杂度O(n)
"""
def twoSum(nums: list[int], target: int) -> list[int]:
    num_dict = {}  # key: 数值, value: 索引
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], idx]
        num_dict[num] = idx
    return []

# 测试用例（必加，体现代码完整性）
if __name__ == "__main__":
    assert twoSum([2,7,11,15], 9) == [0,1]
    assert twoSum([3,2,4], 6) == [1,2]
    print("所有测试用例通过！")