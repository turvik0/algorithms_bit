def canJump(nums):       
    max_jumps = 0
    for i in range(len(nums)-1):
        max_jumps = max(max_jumps - 1, nums[i])
        if max_jumps == 0:
            return 0
    return 1
if __name__ == "__main__":
    N = int(input())
    numlist = list(map(int, input().split(" ")))
    print(canJump(numlist))