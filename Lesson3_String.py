# str = input("Enter a string:")

def play_with_str():
    name = 'Minh Hien'
    print(f'len = {len(name)}')
    print(f'begin: {name[0]} - {name[-9]}')
    print(f'end: {name[8]} - {name[-1]}')
    # locate the index of string
    print(f'first name: {name[5:]} - {name[5:9]} - {name[-4:]}')
    print(f'middle name: {name[:4]} - {name[0:5]} - {name[-9: -5]}')
    print("Reverted name = ", end = "")
    for i in range(len(name)) [::-1]:
        print(f'{name[i]}', end='')
# play_with_str()

def print_character_at_odd_index():
    str = input("Enter a string:")
    for i in range(0, len(str), 2):
        print(f'{str[i]}', end=' ')

# Enter a string => output character at even index
# print_character_at_odd_index()

# Verify whether a string is symmetric string
def verify_symmetric_str(str):
    length = len(str)
    stop = length % 2
    star = stop + 1 if length % 2 == 0 else stop + 2
    for i in (0, stop):
        for j in (-1, -(star - 1)):
            if str[i] != str[j]:
                return False
    return True

def revert_str(str):
    re_str = ''
    for i in range(len(str) - 1, -1, -1):
        re_str = re_str + str[i]
    return re_str

def test_symmertric_fun(str):
    print(f'str = {str}')
    rev_str = revert_str(str)
    print(f'reversed str = {rev_str}')
    another_string = str + rev_str
    print(f'another string = {another_string}')
    print(f'verify_symmetric_str(str) = {verify_symmetric_str(str)}')
    print(f'Another string should always be symmetric {verify_symmetric_str(str + rev_str)}')

# test_symmertric_fun(str)

# Count character
def count_character(str):
    count_dict = dict()
    for i in str:
        count_dict[i] = str.count(i)
    return count_dict

# print(f'Count number of character appears in str = {count_character(str)}')

