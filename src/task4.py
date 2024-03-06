count: int = 0
for i in range(1,101):
    if i % 4 == 0 or i % 3 == 0:
        print(i)
        count += 1

print(f"count: {count}")