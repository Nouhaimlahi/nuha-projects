# Function to load students from the file into parallel lists
def load_students_from_file():
    student_names = []
    student_gpas = []
    
    try:
        # Try to open the file in read mode
        with open("students.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    name, gpa = line.rsplit(" ", 1)  # Split by the last space
                    student_names.append(name)
                    student_gpas.append(float(gpa))
    except FileNotFoundError:
        # If the file doesn't exist, create an empty file
        print("File not found, creating a new one...")
        with open("students.txt", "w") as file:
            pass  # Create the file if it doesn't exist
    
    return student_names, student_gpas

# Function to display the students and their GPAs
def display_students(student_names, student_gpas):
    if len(student_names) == 0:
        print("There are currently no students in the class.")
    else:
        # Sort students by GPA in descending order, keeping the parallel list intact
        sorted_students = sorted(zip(student_gpas, student_names), reverse=True)
        for gpa, name in sorted_students:
            print(f"{gpa:.2f} | {name}")

# Function to show performance statistics
def performance_statistics(student_names, student_gpas):
    probation_list = []
    passing_list = []
    president_list = []
    
    # Categorize students based on GPA
    for name, gpa in zip(student_names, student_gpas):
        if gpa == 4.00:
            president_list.append((gpa, name))
        elif gpa <= 2.50:
            probation_list.append((gpa, name))
        else:
            passing_list.append((gpa, name))
    
    # Sort the lists by GPA
    probation_list.sort(reverse=True)
    passing_list.sort(reverse=True)
    president_list.sort(reverse=True)
    
    # Print the statistics
    print(f"Number of students on probation (GPA ≤ 2.50): {len(probation_list)} students")
    print(f"Number of students with a passing GPA (GPA > 2.50): {len(passing_list)} students")
    print(f"Number of students on the President's List (GPA = 4.00): {len(president_list)} students")
    
    # Display the lists
    print("\nPresident's List:")
    for gpa, name in president_list:
        print(f"{gpa:.2f} | {name}")
    
    print("\nProbation List:")
    for gpa, name in probation_list:
        print(f"{gpa:.2f} | {name}")
    
    print("\nPassing List:")
    for gpa, name in passing_list:
        print(f"{gpa:.2f} | {name}")

# Function to add a new student
def add_student(student_names, student_gpas):
    name = input("Enter student's name: ").strip().title()  # Capitalize the name
    gpa = float(input("Enter student's GPA: ").strip())  # Convert GPA to float
    student_names.append(name)
    student_gpas.append(round(gpa, 2))  # Round GPA to 2 decimal places
    
    # Update the file
    with open("students.txt", "a") as file:
        file.write(f"{name} {gpa:.2f}\n")  # Correct format: no comma at the end

# Function to update a student's GPA
def update_student_gpa(student_names, student_gpas):
    name = input("Enter the student's name to update GPA: ").strip().title()
    
    if name in student_names:
        index = student_names.index(name)
        new_gpa = float(input(f"Enter new GPA for {name}: ").strip())
        student_gpas[index] = round(new_gpa, 2)
        
        # Update the file with the new GPA
        with open("students.txt", "w") as file:
            for i in range(len(student_names)):
                file.write(f"{student_names[i]} {student_gpas[i]:.2f}\n")  # Correct format
    
    else:
        print(f"{name} not found in the student list.")

# Function to delete dropped-out students (GPA = 0.00)
def delete_dropped_out_students(student_names, student_gpas):
    to_delete = [i for i, gpa in enumerate(student_gpas) if gpa == 0.00]
    
    # Remove dropped-out students from the lists
    for i in reversed(to_delete):
        del student_names[i]
        del student_gpas[i]
    
    # Update the file after deletion
    with open("students.txt", "w") as file:
        for i in range(len(student_names)):
            file.write(f"{student_names[i]} {student_gpas[i]:.2f}\n")  # Correct format

# Main function
def main():
    # Load students from the file at the start
    student_names, student_gpas = load_students_from_file()
    
    # Menu loop
    attempts = 0
    while attempts < 3:
        print("\nMenu:")
        print("1. Add a new student")
        print("2. Display Students and their GPA")
        print("3. Performance Statistics")
        print("4. Update a Student's GPA")
        print("5. Delete Dropped-Out Students")
        print("6. Exit")
        
        try:
            choice = int(input("Enter your choice: ").strip())
            
            if choice == 1:
                add_student(student_names, student_gpas)
            elif choice == 2:
                display_students(student_names, student_gpas)
            elif choice == 3:
                performance_statistics(student_names, student_gpas)
            elif choice == 4:
                update_student_gpa(student_names, student_gpas)
            elif choice == 5:
                delete_dropped_out_students(student_names, student_gpas)
            elif choice == 6:
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Please try again.")
            
            attempts = 0  # Reset the attempts on valid input
        
        except ValueError:
            attempts += 1
            print(f"Invalid input. You have {3 - attempts} attempts left.")
            if attempts == 3:
                print("Exceeded maximum attempts. Exiting program...")
                break

# Run the program
if __name__ == "__main__":
    main()
