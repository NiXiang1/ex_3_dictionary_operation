student = {
    "name": "Alice Wong",
    "student_id": "ST1024",
    "age": 21,
    "program": "Software Engineering",
    "city": "Nanjing",
    "gpa": 3.6
}


# First, display the complete record using for loop, printing and some string formatting only



# Check if there's a key called 'email'. If not, ask the user to enter an email



# Ask the user to enter a new city, and update the existing city with this new one
# Make sure the new city is not an empty string



# Check if there's 'phone' key in the dictionary. If not, print a message saying "Phone number not found."
# Use the get() method



# Add a new key called 'contact' to the dictionary, which is itself a dictionary containing two keys: 'phone' and 'email'.




# Add another key called 'courses' to the dictionary, which is itself a dictionary containing three keys: 'Python', 'Databases', and 'Software Engineering', with 88, 91, and 84 as their corresponding scores



# Calculate the average score for the student without built-in functions like sum(). Use a for loop instead. 



# Add a new key called 'academic_status' to the dictionary
# It should be a string that indicates the student's academic status based on the average score. 
# If the score is >= 90, the status should be "Excellent".
# If the score is >= 75, the status should be "Good".
# If the score is >= 60, the status should be "Pass".
# If the score is < 60, the status should be "At Risk".




# Add the logic to search for a course. 
# If the course is found, print the course name and score. If not, print "Course not found".




# Add the logic to update a course score. 
# Ask the user to enter the course name and the new score. 
# If the course is found, then update the score and print a message indicating the change.
# While adding the new course, make sure the new score is a number between 0 and 100




# Recaclculate the average score and update the academic status after the course score has been updated.




# Display the final formatted student record with all the updated information, including the average score and academic status.
# It should look like the following: 
""" 
=====================================
        STUDENT RECORD
=====================================

Name: Alice Wong
Student ID: ST1024
Age: 21
Program: Software Engineering
City: Shanghai
GPA: 3.6

CONTACT
Phone: 13800001111
Email: alice.wong@university.edu

COURSE RESULTS
Python: 88
Databases: 91
Software Engineering: 84

Average Score: 87.7
Academic Status: Good

===================================== """

