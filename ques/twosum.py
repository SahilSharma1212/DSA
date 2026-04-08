nums = []
target = 7

mp = {}

for i in range(len(nums)):
    tofind = target - nums[i]
    if tofind not in mp:
        mp[nums[i]] = i
    else:
        print([mp[tofind], i])
        break