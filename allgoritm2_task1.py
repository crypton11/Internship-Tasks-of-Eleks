# Функція, яка знаходить координати точки виходу
def find_exit_point(matrix, entry_point):
    # отримуємо розмір матриці
    n = len(matrix)

    # задаємо напрямок руху кулі від входу, на початку - вправо
    direction = (1, 0)

    # задаємо початкові координати кулі
    x, y = entry_point

    # виконуємо рух кулі по полю
    while True:
        # рухаємо кулю на одну клітинку в заданому напрямку
        x += direction[0]
        y += direction[1]

        # перевіряємо, чи куля виходить за межі поля
        if x < 0 or x >= n or y < 0 or y >= n:
            return (x - direction[0], y - direction[1])  # повертаємо попередні координати як точку виходу

        # отримуємо символ, який зустрічається на клітинці
        symbol = matrix[x][y]

        # перевіряємо, який символ зустрівся і змінюємо напрямок руху кулі, якщо потрібно
        if symbol == "\\":
            direction = (-direction[1], -direction[0])
        elif symbol == "/":
            direction = (direction[1], direction[0])
        elif symbol == "_":
            direction = (-direction[0], direction[1])
        elif symbol == "|":
            direction = (direction[0], -direction[1])
