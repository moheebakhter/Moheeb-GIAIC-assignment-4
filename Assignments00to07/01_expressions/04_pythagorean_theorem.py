import math

def main():
    ab = float(input("Enter the length of the side AB:"))
    ac = float(input("Enter the length of the side AC:"))
    
    bc = math.sqrt(ab**2 + ac**2)

    print(f"\033[1;3m The length of BC the hypotenuse is: {bc} \033[0m")

if __name__ == "__main__":
    main()