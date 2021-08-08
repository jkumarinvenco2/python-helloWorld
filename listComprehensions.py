squares = [n**2 for n in range(10)]

print(squares)

for n in range(10):
    print(n**2, end=" ")

squares_again = []
for n in range(10):
    squares_again.append(n**2)
print("\n", squares_again)