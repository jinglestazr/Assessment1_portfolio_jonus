def even_or_odd(number):
    return f"The number {number} is even." if number % 2 == 0 else f"The number {number} is odd."

def main():                                                               
    number = int(input("Enter a number: "))
    print(even_or_odd(number))

if __name__ == "__main__":
    main()
