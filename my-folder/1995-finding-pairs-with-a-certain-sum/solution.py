class FindSumPairs:
    def __init__(self, nums1: list[int], nums2: list[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.counter2 = Counter(nums2)  # fast lookup for nums2 values

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        new_val = old_val + val

        # Update the counter
        self.counter2[old_val] -= 1
        if self.counter2[old_val] == 0:
            del self.counter2[old_val]  # clean up
        self.counter2[new_val] += 1

        # Update the nums2 array
        self.nums2[index] = new_val

    def count(self, tot: int) -> int:
        result = 0
        for num1 in self.nums1:
            complement = tot - num1
            result += self.counter2.get(complement, 0)
        return result

