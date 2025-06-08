a=str(input())

b = [float (c.strip()) for c in a.split(",") if c.strip()]

d=max(b)

print(d)
