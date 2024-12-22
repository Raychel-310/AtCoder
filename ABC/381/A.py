n = int(input())
s = input()

ans = True

# 長さが偶数の場合は即座に終了
if len(s) % 2 == 0:
    ans = False

else:
    # 前半部分が "1" か確認
    for i in range(len(s)//2):
        if s[i] != "1":
            ans = False

    # 中央が "/" でない場合
    if s[len(s)//2] != "/":
        ans = False

    # 後半部分が "2" か確認
    for i in range(len(s)//2 + 1, len(s)):
        if s[i] != "2":
            ans = False

if ans:
    print("Yes")
else:
    print("No")
