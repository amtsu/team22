def print_matrix(matrix):
    for column in zip(*matrix):
        print(*column)

def ten_times():
    def helper(count):
        if count <= 10:
            print(f"Вызов номер {count}")
            helper(count + 1)
    helper(1)

def print_haiku(haiku, transform=lambda x: x):
    for line in haiku:
        print(transform(line))

