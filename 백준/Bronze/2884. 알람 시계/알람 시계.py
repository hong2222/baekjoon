a, b = map(int, input().split())

if a==0:
    if b < 45:
        hour=23
        minute=15+b
    else:
        hour=a
        minute=b-45

else:
    if b < 45:
        hour=a-1
        minute=15+b
    else:
        hour=a
        minute=b-45

print(hour,minute)