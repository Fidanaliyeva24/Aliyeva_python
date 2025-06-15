def check_number():
    num = int(input("Enter a number: "))
    if num > 7:
        print("Hello")
        
def verify_name():
    name = input("Enter a name: ")
    if name == "John":
        print("Hello, John")
    else:
        print("There is no such name")

def filter_multiples():
    arr_str = input("Enter numbers separated by spaces: ")
    arr = arr_str.split()
    numbers = [int(x) for x in arr]
    multiples = [num for num in numbers if num % 3 == 0]
    if multiples:
        print("Multiples of 3:", *multiples)
    else:
        print("No multiples of 3 found.")
        
def check_bracket_sequence():
        seq = input("Enter a bracket sequence: ")
        stack = []
        for char in seq:
            if char in ['(','[']:
                stack.append(char)
            elif char == ')':
                if not stack or stack[-1] != '(':
                     print("Incorrect bracket sequence.")
                     return
                stack.pop()
            elif char == ']':
                if not stack or stack[-1] != '[':
                    print("Incorrect bracket sequence.")
                    return
                stack.pop
                
        if not stack:
            print("Correct bracket sequence.")
        else:
            print("Incorrect bracket sequence.")
        
        
def main():
    print("Checking number...")
    check_number()
    print("\nVerifying name...")
    verify_name()
    print("\nFiltering numbers divisible by 3...")
    filter_multiples()
    print("\nChecking bracket sequence...")
    check_bracket_sequence()

if __name__ == "__main__":
    main()
