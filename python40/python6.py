myarray = [2,5,1,7,3,8,1,2,3,4,5,7,4,9,1,2,3,5]
# for idx, a in enumerate(myarray):
#     if myarray[idx:idx+4] == [a,a+1,a+2,a+3]:
#         print([a, a+1,a+2,a+3])
#         break

# print(myarray[0:4])


my_sorted_list = [2, 3, 0, 4, 5, 6, 7]

def longest_increasing_subsequence(nums):
    n = len(nums)
    print(n)
    if n == 1:
        return 1
    dp = [1] * n
    print(dp)
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

print(longest_increasing_subsequence(my_sorted_list))   

