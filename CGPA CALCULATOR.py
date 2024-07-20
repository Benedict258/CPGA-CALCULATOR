print("Enter the names of your courses (up to 10):")
course_names = []
course_ccus = []
course_ts = []
course_es = []
for i in range(1, 11):
    course_name = input(f"Enter Course{i} name: ")
    if course_name:
        course_names.append(course_name)
        course_ccu = int(input(f"Enter Course{i} credit unit: "))
        course_ccus.append(course_ccu)
        course_ts.append(int(input(f"Enter Course{i} test score: ")))
        course_es.append(int(input(f"Enter Course{i} exam score: ")))
    else:
        break

# Calculate total course credit units
total_ccu = sum(course_ccus)

# Calculate course grades and grade points
course_tscs = [x + y for x, y in zip(course_es, course_ts)]
course_grades = []
course_gps = []
grade_points = {"A": 5, "B": 4, "C": 3, "D": 2, "F": 0}
grade_bounds = [(70, "A"), (60, "B"), (50, "C"), (45, "D"), (0, "F")]
for ctu, tsc, name in zip(course_ccus, course_tscs, course_names):
    for bound, grade in grade_bounds:
        if tsc >= bound:
            break
    gp = grade_points[grade]
    course_grades.append(grade)
    course_gps.append(ctu * gp)

# Calculate total grade points and CGPA
total_gps = sum(course_gps)
cgpa = total_gps / total_ccu

# Print course grades and CGPA
for name, grade, gp in zip(course_names, course_grades, course_gps):
    print(f"{name} grade is {grade} with {gp} points")
print(f"Your CGPA is {cgpa:.2f}")