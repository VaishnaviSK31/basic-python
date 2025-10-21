a="abc123def456"
b=[ ]
for data in a:
    if data.isalpha():
        b.append(data)
print(b)