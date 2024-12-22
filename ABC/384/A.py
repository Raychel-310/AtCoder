n, c1, c2 = input().split()
s = input()

ans = ""
for i in range(len(s)):
    if s[i] != c1:
        ans += c2
    else:
        ans += c1

print(ans)