#1st WHILE LOOP
# Input simple
def input_simple():
    n = int(input('Enter a number:'))
    return n
# input_simple()

# ERROR if you called your function is same name with input() :)
def input_number():
    n = 0
    while True:
        try:
            n = int(input("Enter a number: "))
            break
        except:
            print('Not integer number')
            continue
    print(f'Your number is legel {n}')
    return n

# input_number()
# Input a number  0 < number <= 100, calculate sum of odd number
def calculate_sum_odds():
    n = 0
    while True:
        try:
            n = int(input("Enter a number: "))
            if 0 < n <= 100:
                break
            else:
                print("Please enter again")
        except:
            print('Not integer number')
            continue
    print(f'Your number is legel {n}')
    sum_odds = 0
    i = 1
    while i <= n:
        sum_odds = sum_odds + i
        i = i + 2
    print(f'Sum of odd number <= {n} is {sum_odds}')


def measure_cat_len():
    strs = ['cat', 'dogs', 'banana', 'laptop']
    i = 0
    while i < len(strs):
        print(f'{strs[i]} , {len(strs[i])}')
        i = i + 1

def is_prime_number(n):
    i = 2
    while i < n:
        if n % i != 0:
            i = i + 1
            continue
        else:
            return False
    return True

def print_prime_numbers(n):
    prime_nums = []
    i = 0
    while i < n:
        if is_prime_number(i):
            print(f' {i} ')
            prime_nums.append(i)
        i = i + 1
    return prime_nums

# region EXECUTE FUNCTION
# check_prime_number()
print_prime_numbers(input_number())
# endregion

