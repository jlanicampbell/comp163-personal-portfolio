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
# player chooses a subject to focus on.
# demonstrate membership operators ("in", "not in") by checking if the input is valid.
# use if/elif/else branching and logical operators ("and", "or") to adjust GPA and social points.
study_options = ["Programming", "Math", "English", "History"]

print("Study Options:")
print("Programming, Math, English, History")

study_choice = input("Choose a subject to focus on: ")

# check if the choice is valid
if study_choice not in study_options:
    print("Invalid study choice. No changes made to GPA/social points.")
else:
    print("You chose:", study_choice)
# branching logic with OR operator 
    if study_choice == "Programming" or study_hours == "Math":
        current_gpa = current_gpa + 0.20
        social_points = social_points - 5
    elif study_choice == "English" and current_gpa < 3.0:
        current_gpa = current_gpa + 0.10
        social_points = social_points + 2
# nested condition
    elif study_choice == "History" or (study_choice == "English" and current_gpa >= 3.0):
        current_gpa = current_gpa + 0.05
        social_points = social_points + 5
# gpa clamped so it never goes above 4.0 or below 0.0
    if current_gpa > 4.0:
        current_gpa = 4.0
    if current_gpa < 0.0:
        current_gpa

print("Updated Stats after Study Choice:")
print("Current GPA:", current_gpa)
print("Social Points:", social_points)
print("Study Hours:", study_hours)
print("Stress Level:", stress_level)

# Step 4: Final Semester Assessment 
# bring everything together and uses identity operators, membership operators, and nested if statements to decide the player's outcome.
major = "CS"

# check if the study_choice is stored as a string.
if type(study_choice) is str:
    print("Identity Check: study_choice is stored as a string.")
# check that study_choice is not an integer.
if type(study_choice) is not int:
    print("Indentity Check: study_choice is not an integer.")
# Membership operator: check if the major is in STEM fields and if the study choice is Programming or Math.
if major in ["CS", "Math", "Engineering", "Physics"] and study_choice in ["Programming", "Math"]:
    current_gpa = current_gpa + 0.05
    if current_gpa > 4.0:
        current_gpa = 4.0
# nested if statements are used below to decide the final ending.
if current_gpa >= 3.5:
    if stress_level < 40:
        ending = "Dean's List"
    else:
        ending = "High GPA but too much stress"
elif current_gpa >= 2.5:
    if social_points >= 10:
        ending = "Solid Semester"
    else:
        ending = "Could improve networking"
else:
    if stress_level > 70:
        ending = "On Probabtion"
    else:
        ending = "Needs Academic Recovery"

# display the final semester report with all updated statistics.
print("===== FINAL SEMESTER REPORT =====")
print("Major:", major)
print("GPA:", current_gpa)
print("Study Hours:", study_hours)
print("Social Points:", social_points)
print("Stress Level:", stress_level)
print("Result:", ending)
print("=================================")

# AI (ChatGPT) was used to explain branching concepts such as the use of `is`, `is not`, and nested if statements. It also suggested structure for this section to ensure that required operators and branching examples were included. 
# Rest of Logic developed independently with notes and python website (pythons website helped with functions like .strip())
