C = 299_792_458

while True:
    try:
        # Ask user for mass input
        mass_input = input("\nEnter kilos of mass (or type 'exit' to quit): ")
        if mass_input.lower() == 'exit':
            print("Exiting program.")
            break
        
        # Convert the input to a float
        m = float(mass_input)

        # Calculate energy using E = m * c^2
        E = m * C**2

        # Display the results
        print("\ne = m * C^2...")
        print(f"m = {m} kg")
        print(f"C = {C} m/s")
        print(f"{E} joules of energy!")

    except ValueError:
        print("Please enter a valid number or type 'exit' to quit.")
