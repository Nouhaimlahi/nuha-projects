# ============================
# Airline Booking System
# ============================

# --- Top Level Function ---
def main():
    flights = read_flight_data("flights.txt")
    
    while True:
        email = get_valid_email()
        user_reservations = []

        while True:
            choice = show_menu()
            if choice == '1':
                show_flights(flights)
            elif choice == '2':
                search_itinerary(flights)
            elif choice == '3':
                reserve_flight(flights, user_reservations)
            elif choice == '4':
                compute_total(user_reservations)
            elif choice == '5':
                save_reservations(email, user_reservations)
            elif choice == '6':
                print("Logging out...\n")
                break
            else:
                print("Invalid choice, try again.")

# --- Read Flight Data ---
def read_flight_data(filename):
    flights = []
    with open(filename, 'a') as file:
        next(file)  # skip header
        for line in file:
            parts = line.strip().split(',')
            flight = {
                'airline': parts[0],
                'flight_no': parts[1],
                'from': parts[2],
                'departure': parts[3],
                'to': parts[4],
                'arrival': parts[5],
                'price': int(parts[6]),
                'seats': int(parts[7])
            }
            flights.append(flight)
    return flights

# --- Get Valid Email ---
def get_valid_email():
    while True:
        email = input("Enter your email: ").lower()
        if validate_email(email):
            print("Email accepted.\n")
            return email
        else:
            print("Invalid email, try again.")

def validate_email(email):
    if '@' not in email or email.startswith('@') or email.endswith('@'):
        return False
    if '.' not in email.split('@')[1]:
        return False
    before_at = email.split('@')[0]
    middle = email.split('@')[1].split('.')[0]
    after_dot = email.split('@')[1].split('.')[-1]
    if not any(c.isalpha() for c in before_at):
        return False
    if not any(c.isalpha() for c in middle):
        return False
    if not any(c.isalpha() for c in after_dot):
        return False
    return True

# --- Show Menu ---
def show_menu():
    print("Menu:")
    print("1. View all flights")
    print("2. Find an itinerary")
    print("3. Reserve a flight")
    print("4. Compute my bill")
    print("5. Save my reservation")
    print("6. Exit to login screen")
    return input("Choose an option (1-6): ")

# --- Show Flights ---
def show_flights(flights):
    print("\nAvailable Flights:")
    for f in flights:
        print(f"{f['airline']} {f['flight_no']} | {f['from']} -> {f['to']} | Dep: {f['departure']} Arr: {f['arrival']} | {f['price']} dhs | Seats: {f['seats']}")
    print()

# --- Search Itinerary ---
def search_itinerary(flights):
    dep = input("From: ").upper()
    arr = input("To: ").upper()
    found = False

    # Direct flights
    for f in flights:
        if f['from'] == dep and f['to'] == arr:
            print(f"Direct: {f['airline']} {f['flight_no']} | {f['departure']}->{f['arrival']} | {f['price']} dhs")
            found = True

    # Indirect flights (2 legs) 
    for f1 in flights:
        for f2 in flights:
            if f1['from'] == dep and f1['to'] == f2['from'] and f2['to'] == arr:
                print(f"Connection: {f1['from']}->{f1['to']}->{f2['to']} : {f1['airline']} {f1['flight_no']} + {f2['airline']} {f2['flight_no']}")
                found = True

    if not found:
        print("No itinerary found.\n")

# --- Reserve Flight ---
def reserve_flight(flights, user_reservations):
    show_flights(flights)
    flight_no = input("Enter flight number to reserve: ")

    for f in flights:
        if f['flight_no'] == flight_no:
            if f['seats'] > 0:
                f['seats'] -= 1
                user_reservations.append(f)
                print(f"Flight {flight_no} reserved successfully!\n")
            else:
                print("No seats available.\n")
            return

    print("Flight not found.\n")

# --- Compute Total ---
def compute_total(user_reservations):
    total = sum(f['price'] for f in user_reservations)
    print(f"Your total bill is: {total} dhs\n")


# --- Save Reservations ---
def save_reservations(email, user_reservations):
    filename = f"{email}_reservations.txt"
    total = sum(f['price'] for f in user_reservations)

    with open(filename, 'w') as file:
        for f in user_reservations:
            file.write(f"{f['airline']} {f['flight_no']} | {f['from']} -> {f['to']} | {f['price']} dhs\n")
        file.write(f"Total Price: {total} dhs\n")

    print(f"Reservations saved to {filename}\n")

# --- Run the Program ---
main()
