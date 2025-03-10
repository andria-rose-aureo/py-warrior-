


   
country_capitals = {}
visited_countries = set()

while True:
    print("1. Add a country \n2. Get a capital \n3. Mark a country as visited \n4. Show all data \n5. Exit")
    n = int(input("Enter a choice (between 1 & 5): "))

    if n == 1:
        country = input("Enter a country name: ")
        capital = input("Enter capital: ")
        country_capitals[country] = capital

    elif n == 2:
        cou = input("Enter country name: ")
        if cou in country_capitals:
            print(f"Capital of {cou} is {country_capitals[cou]}")
        else:
            print("Country not found!")

    elif n == 3:
        visited = input("Enter country name to mark as visited: ")
        visited_countries.add(visited)  # Fixed typo (visited_contries → visited_countries)
        print(f"{visited} added to visited list!")

    elif n == 4:
        print("\nStored Countries and Capitals:", country_capitals)
        print("\nVisited Countries:", visited_countries)

    elif n == 5:
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
