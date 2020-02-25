s = input()

l = len(s)

for i in range(l//2):
    if s[i] != s[-1-i]:
        print("строка не палиндром")

print("строка - палиндром.")