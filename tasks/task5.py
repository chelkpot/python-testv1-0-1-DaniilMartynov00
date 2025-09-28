# tasks/task1.py



def solve():
# Ниже пишите решение задачии(Обязательно поставьте четыре пробела после функции Solve())
    numbers_input = input("Введите числа, разделённые пробелами: ")
    numbers = map(int, numbers_input.split())
    squares = [num ** 2 for num in numbers]
    print("Результат:", ' '.join(map(str, squares)))


# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()