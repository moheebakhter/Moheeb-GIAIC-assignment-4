# def main():
#     side3 = float(input("Enter the length of side 3? "))
#     side1 = float(input("Enter the length of side 1? "))
#     side2 = float(input("Enter the length of side 2? "))
# print("The perimeter of the triangle is" + str(side1 + side2 + side3))

# if __name__ == "__main__":
#     main()
    
def main():
    side1 = float(input("\033[1;3m  Enter the length of side 1? \033[0m"))
    side2 = float(input("\033[1;3m  Enter the length of side 2? \033[0m"))
    side3 = float(input("\033[1;3m  Enter the length of side 3? \033[0m"))
    
    print("The perimeter of the triangle is " + str(side1 + side2 + side3))

if __name__ == "__main__":
    main()