# Step 1: Foundation Setup
student_name = "Jelani Campbell"
current_gpa = 3.2
study_hours = 25
social_points = 50
stress_level = 50

print("Welcome to Assignment 3!")
print("Student Name:", student_name)
print("Current GPA:", current_gpa)
print("Study Hours:", study_hours)
print("Social Points:", social_points)
print("Stress level:", stress_level)

# Step 2: Course Planning Decision
print("Choose your course load:")
print("A) Light (12 credits)")
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")

choice = input("Your choice: ").strip().upper()

if choice == "A":
    if current_gpa >= 2.0:
        study_hours = study_hours + 2
        stress_level = stress_level - 5
    else:
        study_hours = study_hours + 3
        stress_level = stress_level + 5

elif choice == "B":
    study_hours = study_hours + 5
    stress_level = stress_level + 10
    
elif choice == "C":
    if current_gpa >= 3.5:
        study_hours = study_hours + 7
        stress_level = stress_level + 15
    else:
        study_hours = study_hours + 10
        stress_level = stress_level + 25
    
else:
    print("Invalid choice. No changes made.")

print("Updated Stats:")
print("Study Hours:", study_hours)
print("Stress Level:", stress_level)
 
 # Step 3: Study Strategy Decision
study_options = ["Programming", "Math", "English", "History"]

print("Study Options:")
print("Programming, Math, English, History")

study_choice = input("Choose a subject to focus on: ")

if study_choice not in study_options:
    print("Invalid study choice. No changes made to GPA/social points.")
else:
    print("You chose:", study_choice)
    if study_choice == "Programming" or study_hours == "Math":
        current_gpa = current_gpa + 0.20
        social_points = social_points - 5
    elif study_choice == "English" and current_gpa < 3.0:
        current_gpa = current_gpa + 0.10
        social_points = social_points + 2
    elif study_choice == "History" or (study_choice == "English" and current_gpa >= 3.0):
        current_gpa = current_gpa + 0.05
        social_points = social_points + 5
    if current_gpa > 4.0:
        current_gpa = 4.0
    if current_gpa < 0.0:
        current_gpa

print("Updated Stats after Study Choice:")
print("Current GPA:", current_gpa)
print("Social Points:", social_points)
print("Study Hours:", study_hours)
print("Stress Level:", stress_level)