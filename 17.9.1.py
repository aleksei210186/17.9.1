numbers = [int(c) for c in input("Введите числа от 0 до 1000 в любом порядке, через пробел: ").split()]

def merge_sort(numbers):
    if len(numbers) < 2:
        return numbers[:]
    else:
        middle = len(numbers) // 2
        left = merge_sort(numbers[:middle])
        right = merge_sort(numbers[middle:])
        return merge(left, right)
def merge(left, right):
    result = []
    a, b = 0, 0
    while a < len(left) and b < len(right):
        if left[a] < right[b]:
            result.append(left[a])
            a += 1
        else:
            result.append(right[b])
            b += 1
    while a < len(left):
        result.append(left[a])
        a += 1
    while b < len(right):
        result.append(right[b])
        b += 1
    return result
print(merge_sort(numbers))

while True:
    try:
        digit = int(input("Введите число от 0 до 1000: "))
        if digit <= 0 or digit >= 1000:
            raise Exception
        break
    except ValueError:
        print("Нужно ввести число!!!")
    except Exception:
        print("Неправильный диапазон!!!")
    
def binary_search(numbers, digit, left, right):
    if left > right:
        return False
    middle = (right + left) // 2 
    if numbers[middle] == digit:
        return middle 
    elif digit < numbers[middle]: 
        return binary_search(numbers, digit, left, middle - 1)
    else:  
        return binary_search(numbers, digit, right, middle + 1)

print(binary_search(numbers, digit, 0, len(numbers)))