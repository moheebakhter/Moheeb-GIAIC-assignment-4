C = 299_792_458

while True:
    try:
        # Ask user for mass input
        mass_input = input("\nEnter kilos of mass (or type 'exit' to quit):")
        if mass_input.lower() == 'exit':
            print("Exiting program.")
            break
        
        # Convert the input to a float
        m = float(mass_input)

        # Calculate energy using E = m * c^2
        E = m * C**2

        # Display the results
        print("\n\033[1;3m e = m * C^2...\033[0m")
        print(f"\033[1;3m m = {m} kg\033[0m")
        print(f"\033[1;3m C = {C} m/s\033[0m")
        print(f"\033[1;3m {E} joules of energy!\033[0m")

    except ValueError:
        print("Please enter a valid number or type 'exit' to quit.")
