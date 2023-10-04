def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        # Если число элементов четное, усреднить два средних.
        middle1 = numbers[n // 2]
        middle2 = numbers[n // 2 - 1]
        median = (middle1 + middle2) / 2
    else:
        # Если элементов нечетное количество, просто возьмите средний.
        median = numbers[n // 2]
    return median

# Проверить функцию
numbers = [5, 2, 9, 1, 5]
median = calculate_median(numbers)
print(f"Median: {median}")
