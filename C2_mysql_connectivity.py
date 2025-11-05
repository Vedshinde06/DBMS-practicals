import mysql.connector

# ------------------------
# 1️⃣ Connect to MySQL
# ------------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",        # your MySQL username
    password="root",    # your MySQL password
    database="student_db"
)

cursor = conn.cursor()
print(" Connected to MySQL Database successfully!\n")

# ------------------------
# 2️⃣ Functions for Operations
# ------------------------

# Add new record
def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course = input("Enter course name: ")

    query = "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)"
    values = (name, age, course)
    cursor.execute(query, values)
    conn.commit()
    print(" Record added successfully!\n")


# View all records
def show_students():
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()
    print("\n Student Records:")
    print("----------------------------")
    for row in result:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Course: {row[3]}")
    print("----------------------------\n")


# Edit record (update)
def edit_student():
    student_id = int(input("Enter ID to edit: "))
    new_age = int(input("Enter new age: "))
    new_course = input("Enter new course: ")

    query = "UPDATE students SET age=%s, course=%s WHERE id=%s"
    values = (new_age, new_course, student_id)
    cursor.execute(query, values)
    conn.commit()
    print(" Record updated successfully!\n")


# Delete record
def delete_student():
    student_id = int(input("Enter ID to delete: "))
    query = "DELETE FROM students WHERE id=%s"
    cursor.execute(query, (student_id,))
    conn.commit()
    print(" Record deleted successfully!\n")


# ------------------------
# 3️⃣ Menu-driven Navigation
# ------------------------
while True:
    print("===== STUDENT DATABASE MENU =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Edit Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        show_students()
    elif choice == '3':
        edit_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        print(" Exiting Program...")
        break
    else:
        print(" Invalid choice, try again!")

# ------------------------
# 4️⃣ Close Connection
# ------------------------
cursor.close()
conn.close()
