def marcsCakewalk(calorie):
    # Write your code here
    ans = 0
    calorie.sort(reverse=True)
    for i, j in enumerate(calorie):
        ans += (2 ** i * j)
    return ans

if __name__ == '__main__':
    n = int(input().strip())
    calorie = list(map(int, input().rstrip().split()))
    result = marcsCakewalk(calorie)
    print(result)
