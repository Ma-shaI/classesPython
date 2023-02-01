n = int(input())
count = 0
nums = [int(input()) for _ in range(n)]
for i in nums:
    if i <= 100:
        count += i
        nums.pop(nums.index(i))
    else:
        count += i
        nums.pop(nums.index(i))
        break
s = max(nums)
nums.pop(nums.index(s))
summa = sum(nums) + count
print(summa)
