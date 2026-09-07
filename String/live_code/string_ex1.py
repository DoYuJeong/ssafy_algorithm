s1 = input()
s2 = input()

# 모두 있다고 가정하고, 하나라도 없으면
# 'NO'로 바꾸고 종료
ans = 'YES'
for ch in s1:
    if ch not in s2:
        ans = 'NO'
        break # for ch
print(ans)