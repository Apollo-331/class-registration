from course import Course
from student import Student

math = Course("Algebra I")
language = Course("Spanish I")
science = Course("Earth Science")
history = Course("U.S. History I")
phys_ed = Course("Physical Education I")
CSE = Course("Computer Science Essentials")
IED = Course("Intro to Engineering Design")

test_student = Student("Jill", "Sample")
test_student.add_course(math)
test_student.add_course(language)
test_student.add_course(science)
test_student.add_course(history)

test_student2 = Student("Bill", "Sample")
test_student2.add_course(math)
test_student2.add_course(phys_ed)
test_student2.add_course(science)
test_student2.add_course(history)

test_student3 = Student("Will", "Sample")
test_student3.add_course(language)
test_student3.add_course(history)
test_student3.add_course(IED)
test_student3.add_course(CSE)

student_list = [test_student, test_student2, test_student3]

print("student_list:", student_list)

for student in student_list:
    # Each iteration should:
    # print the student
    print(f"Student: {student}")

    # print their course schedule (assumes `student.courses` exists as a list)
    course_list = getattr(student, "courses", None)
    if course_list is None:
        course_list = getattr(student, "schedule", None)

    if isinstance(course_list, list):
        course_names = ", ".join(str(c) for c in course_list)
        print(f"  Courses: {course_names}")
    else:
        print(f"  Courses: {course_list}")

    print()
"""
 for this part you may need to review the other skeleton code to:
    - see how to get items from a list
    - see if there is code (like a function) in that file you can call in this file
    - verify that running this file gets you the correct output with information from that file
  Also, review syntax of pulling items from a list from other activities 
"""