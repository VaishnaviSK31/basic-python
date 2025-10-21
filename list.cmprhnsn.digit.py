a="abc123def456"
b=[ ]
for data in a:
    if data.isdigit():
        b.append(data)
print(b)