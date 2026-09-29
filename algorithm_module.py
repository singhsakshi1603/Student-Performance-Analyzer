def factorial(number):
    result=1
    for value in range(2,number+1):
        result *=value
        return result
def fibonacci(count):
    sequence=[]
    first,second=0,1
    for _ in range(count):
        sequence.append(first)
        first, second = second, first + second
        return sequence
def reverse_text(text):
    result=""
    for character in text:
        result = character + result
        return result
def decimal_to_binary(number):
    if number==0:
        return "0"
    binary=""
    while number>0:
        number,remainder=divmod(number,2)
        binary=str(remainder)+binary
        return binary
def exchange_values (first,second):
        first,second=second,first
        return first,second
def read_number(prompt,minimum=None,maximum=None):
    while True:
        try:
            value=int(input(prompt).strip())
            if minimum is not None and value < minimum:
                print(f"Enter a value of at least {minimum}.")
                continue

            if maximum is not None and value > maximum:
                print(f"Enter a value of at most {maximum}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")
def algorithm_menu():
    while True:
        print("\nAlgorithm Toolkit")
        print("1. Factorial")
        print("2. Fibonacci Sequence")
        print("3. Reverse Text")
        print("4. Decimal to Binary")
        print("5. Exchange Two Values")
        print("0. Return to Main Menu")
        choice = input("Choose an algorithm: ").strip()
        if choice == "1":
            number = read_number(
                "Enter a non-negative number: ",
                minimum=0,
                maximum=100
            )
            print(f"{number}!={factorial(number)}")
        elif choice=="2":
            count = read_number(
                "How many Fibonacci terms? ",
                minimum=0,
                maximum=50
            )
            print("Fibonacci Sequence:", fibonacci(count))
        elif choice=="3":
            text=input("Enter text: ")
            print("Reversed:", reverse_text(text))
        elif choice=="4":
            number=read_number(
                "Enter a non-negative decimal number: ",
                minimum=0
            )
            print(
                "Binary representation:",
                decimal_to_binary(number)
            )
        elif choice == "5":
            first = input("First value:")
            second = input("Second value:")
            print(
                "After exchange:",
                exchange_values (first, second)
            )
        elif choice=="0":
            break
        else:
            print("Invalid algorithm choice.")