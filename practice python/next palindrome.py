# def next_palindrome(a):
#     num = int("".join(map(str, a)))

#     while True:
#         num += 1
#         if str(num) == str(num)[::-1]:
#             return list(map(int, str(num)))

# def main():
#     a = eval(input("Enter list: "))
#     result = next_palindrome(a)
#     print(result)

# if __name__ == "__main__":
#     main()

def next_palindrome(a):
    num = int("".join(map(str, a)))
    while True:
        num += 1 
        if str(num) == str(num)[::-1]:
            return list(map(int, str(num)))

if __name__ == "__main__":
    a = eval(input())
    result = next_palindrome(a)
    print(result)