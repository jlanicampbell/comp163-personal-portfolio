# 1. Personal Information Storage (use the exact string values)
full_name = "Jelani Campbell"
student_email = "jlcampbell1@ncat.edu"
hometown = "Greensboro, NC"
graduation_semester = "Spring 2027"
major = "Computer Science"

# 2. Academic Data Organization (use the exact list values)
current_courses = ["COMP 163", "MATH 131", "BUAN 132", "HIS 103"]
completed_courses = ["Music Theory", "Intro to Media", "Statistics", "German I", "Humanities"]
credit_hours = [3, 3, 3, 3]
gpa_history = [3.8, 3.2, 2.4, 2.1]

# 3. Contact Inforamtion Storage (use the exact tuple values)
emergency_contact = ("Mom", "Celeste Williams", "565-6565-5566")
home_address = ("456 Oak Street", "Charlotte, NC", "28202")
instagram_info = ("Instagram", "@jordan_codes", "312")
twitter_info = ("Twitter", "@jordandev", "127")
birthday = ("Birthday", "5, 22", "2006")

# 4. Interest Tracking (use the exact set values)
current_skills = {
    "Photo Shop",
    "Adobe Premiere Pro",
    "After Effects",
    "Videography",
    "Editorial Freelancing"
}
skills_to_learn = {
    "Networking",
    "Building Apps",
    "Visual Code",
    "API Coding",
    "Debugging"
}
career_interests = {
    "Cyber Security",
    "Programmer",
    "Online Tech Brand",
    "Tech Professor"
}
hobbies = {
    "Dancing",
    "Piano",
    "Gym",
    "Tennis",
    "YouTube"
}
entertainment_backlog = {
    "One Piece",
    "Barry",
    "Life",
    "Incantation",
    "Memento"
}
# 5. Organizational Mapping (use the exact dictionary key-values)
course_credits = {
    "COMP 163": 3,
    "MATH 131": 3,
    "BUAN 132": 3,
    "HIS 103": 3
}
course_professors = {
    "COMP 163": "Prof. Rhodes",
    "MATH 131": "Dr. Gernald",
    "BUAN 132": "Dr. Marry",
    "HIS 103": "Dr. Green"
}
course_rooms = {
    "COMP 163": "M-Eric 330",
    "MATH 131": "Marteena 213",
    "BUAN 132": "Crosby 126",
    "HIS 103": "Crosby 219"
}
monthly_budget = {
    "Food": 400,
    "Entertainment": 150,
    "Books": 75,
    "Transportation": 50
}
study_hours = {
    "Programming": 8,
    "Math": 6,
    "Info Systems": 2,
    "History": 1
}
contact_directory = {
    "Mom": "704-555-0199",
    "Roommate": "336-555-7821",
    "Academic Advisor": "336-334-5000"
}

# Required Calculations
total_current_credits = sum(credit_hours)

total_gpa = sum(gpa_history)
number_of_gpas = len(gpa_history)
cumulative_gpa = round(total_gpa / number_of_gpas, 2)

completed_courses_count = len(completed_courses)

total_study_hours = study_hours["Programming"] + study_hours["Math"] + study_hours["Info Systems"] + study_hours["History"]

academic_load = total_current_credits + total_study_hours

monthly_food = monthly_budget["Food"]
monthly_entertainment = monthly_budget["Entertainment"]
monthly_books = monthly_budget["Books"]
monthly_transportation = monthly_budget["Transportation"]
monthly_budget_total = monthly_food + monthly_entertainment + monthly_books + monthly_transportation

daily_food_budget = round(monthly_food / 30,2)

annual_budget_projection = monthly_budget_total * 12

study_cost_per_hour = round(monthly_books / total_study_hours, 2)

# Analytics Calculations
instagram_followers = int(instagram_info[2])
twitter_followers = int(twitter_info[2])
total_followers = instagram_followers + twitter_followers

current_skills_count = len(current_skills)
skills_to_learn_count = len(skills_to_learn)

contact_count = len(contact_directory)

entertainment_count = len(entertainment_backlog)

total_credits = sum(credit_hours)
total_hours = study_hours["Programming"] + study_hours["Math"] + study_hours["History"]
academic_workload = total_credits + total_hours

# Final Output Display
print("=" * 64)
print("              PERSONAL ACADEMIC & LIFE PORTFOLIO")
print("=" * 64)

# Personal Info
print(f"Student: {full_name} | Email: {student_email}")
print(f"From: {hometown} | Graduating: {graduation_semester}")
print(f"Major: {major}")
print()

# Academic Profile
print("=== ACADEMIC PROFILE ===")
print(f"Current Semester: {total_current_credits} credits across {len(current_courses)} courses")
print(f"Cumulative GPA: {cumulative_gpa}")
print(f"Weekly Study Time: {total_study_hours} hours")
print(f"Academic Investment: ${study_cost_per_hour} per study hour")
print()

# Current courses
print("Current Courses:")
print(f"{current_courses[0]} - {course_credits['COMP 163']} credits - {course_professors['COMP 163']} - {course_rooms['COMP 163']}")
print(f"{current_courses[1]} - {course_credits['MATH 131']} credits - {course_professors['MATH 131']} - {course_rooms['MATH 131']}")
print(f"{current_courses[2]} - {course_credits['BUAN 132']} credits - {course_professors['BUAN 132']} - {course_rooms['BUAN 132']}")
print(f"{current_courses[3]} - {course_credits['HIS 103']} credits - {course_professors['HIS 103']} - {course_rooms['HIS 103']}")
print()

# Personal Development
print("=== PERSONAL DEVELOPMENT ===")
print(f"Current Skills: {current_skills}")
print(f"Learning Goals: {skills_to_learn}")
print(f"Career Interests: {career_interests}")
print(f"Skills Currently Have: {current_skills_count}")
print(f"Skills Want to Learn: {skills_to_learn_count}")
print()

# Financial Overview
print("=== FINANCIAL OVERVIEW ===")
print(f"Monthly Budget: ${monthly_budget_total}")
print(f"Food: ${monthly_food} (${daily_food_budget}/day)")
print(f"Entertainment: ${monthly_entertainment}")
print(f"Books: ${monthly_books}")
print(f"Transportation: ${monthly_transportation}")
print(f"Annual Projection: ${annual_budget_projection}")
print()

# Connections & Contacts
print("=== CONNECTIONS & CONTACTS ===")
print(f"Emergency Contact: {emergency_contact[1]} ({emergency_contact[0]}) - {emergency_contact[2]}")
print(f"Home Address: {home_address[0]}, {home_address[1]} {home_address[2]}")
print(f"Social Media Presence: {total_followers} followers across 2 platforms")
print(f"Key Contacts: {contact_count} people in directory")
print()

# Life Stats
print("=== LIFE STATISTICS ===")
print(f"Total Courses Completed: {completed_courses_count}")
print(f"Current Academic Load: {academic_load} weekly commitments")
print(f"Entertainment Backlog: {entertainment_count} items")
print(f"Current Hobbies: {len(hobbies)} activities")
print("=" * 64)
