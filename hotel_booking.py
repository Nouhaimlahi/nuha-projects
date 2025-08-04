# Constants for room prices
ECONOMIC_PRICE = 80
LUXURIOUS_PRICE = 140
SUITE_PRICE = 260
TAX_RATE = 0.15

# Initial availability of rooms
available_economic = 150
available_luxurious = 100
available_suite = 50

def display_rooms(available_economic, available_luxurious, available_suite):
    """Displays available rooms and their prices."""
    print("\nAvailable Rooms and Prices:")
    print(f"Economic room | price = {ECONOMIC_PRICE} MAD | ({available_economic}) rooms are available")
    print(f"Luxurious room | price = {LUXURIOUS_PRICE} MAD | ({available_luxurious}) rooms are available")
    print(f"Suite | price = {SUITE_PRICE} MAD | ({available_suite}) rooms are available")

def book_room(available_economic, available_luxurious, available_suite):
    """Handles room booking process without using global variables."""
    subtotal = 0

    while True:
        print("\nWhich type of room would you like to book?")
        print("1. Economic\n2. Luxurious\n3. Suite\n4. Finish booking")
        choice = input("Enter your choice (1-4): ")

        if choice == "4":
            break

        if choice not in ["1", "2", "3"]:
            print("Invalid choice! Please enter a valid option.")
            continue

        room_type = ""
        room_price = 0
        available_rooms = 0

        if choice == "1":
            room_type = "Economic"
            room_price = ECONOMIC_PRICE
            available_rooms = available_economic
        elif choice == "2":
            room_type = "Luxurious"
            room_price = LUXURIOUS_PRICE
            available_rooms = available_luxurious
        elif choice == "3":
            room_type = "Suite"
            room_price = SUITE_PRICE
            available_rooms = available_suite

        while True:
            try:
                num_rooms = int(input(f"How many {room_type} rooms would you like to book? "))
                if num_rooms > available_rooms:
                    print(f"Only {available_rooms} {room_type} rooms are available. Please enter a valid number.")
                elif num_rooms < 1:
                    print("You must book at least 1 room.")
                else:
                    break
            except ValueError:
                print("Invalid input! Please enter a number.")

        for i in range(num_rooms):
            while True:
                try:
                    nights = int(input(f"Enter number of nights for {room_type} room {i + 1}: "))
                    subtotal += room_price * nights
                    break
                except ValueError:
                    print("Invalid input! Please enter a number.")

        if choice == "1":
            available_economic -= num_rooms
        elif choice == "2":
            available_luxurious -= num_rooms
        elif choice == "3":
            available_suite -= num_rooms

    if subtotal > 0:
        tax = subtotal * TAX_RATE
        total = subtotal + tax
        print(f"\nInvoice:\nSubtotal before tax: {subtotal} MAD\nTax (15%): {tax:.2f} MAD\nTotal price: {total:.2f} MAD\n")
    else:
        print("No rooms were booked.")

    return available_economic, available_luxurious, available_suite

def return_room(available_economic, available_luxurious, available_suite):
    """Handles returning of room keys without using global variables."""
    while True:
        print("\nWhich type of room would you like to return?")
        print("1. Economic\n2. Luxurious\n3. Suite\n4. Cancel")
        choice = input("Enter your choice (1-4): ")

        if choice == "4":
            print("Return process canceled.")
            break

        room_type = ""
        booked_rooms = 0

        if choice == "1":
            room_type = "Economic"
            booked_rooms = 150 - available_economic
        elif choice == "2":
            room_type = "Luxurious"
            booked_rooms = 100 - available_luxurious
        elif choice == "3":
            room_type = "Suite"
            booked_rooms = 50 - available_suite
        else:
            print("Invalid choice! Please enter a valid option.")
            continue

        if booked_rooms == 0:
            print(f"No {room_type} rooms have been booked, so there's nothing to return.")
            continue

        while True:
            try:
                num_return = int(input(f"How many {room_type} rooms would you like to return? "))
                if num_return < 1:
                    print("You must return at least 1 room.")
                elif num_return > booked_rooms:
                    print(f"You only booked {booked_rooms} {room_type} rooms. Please enter a valid number.")
                else:
                    break
            except ValueError:
                print("Invalid input! Please enter a number.")

        if choice == "1":
            available_economic += num_return
        elif choice == "2":
            available_luxurious += num_return
        elif choice == "3":
            available_suite += num_return

        print(f"{num_return} {room_type} room(s) returned successfully!")
        break

    return available_economic, available_luxurious, available_suite

def main():
    """Main menu loop without using global variables."""
    available_economic = 150
    available_luxurious = 100
    available_suite = 50

    while True:
        print("\nHotel Menu System")
        print("1. Display Available Rooms and Prices")
        print("2. Book a Room")
        print("3. Return a Room Key")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_rooms(available_economic, available_luxurious, available_suite)
        elif choice == "2":
            available_economic, available_luxurious, available_suite = book_room(
                available_economic, available_luxurious, available_suite
            )
        elif choice == "3":
            available_economic, available_luxurious, available_suite = return_room(
                available_economic, available_luxurious, available_suite
            )
        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()