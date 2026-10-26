student_dictionary = {"st1": {"Name":"Mark","Year level":"Year 9","Subjects":"Math, HPE, English"},
                      "st2": {"Name":"Jessica","Year level":"Year 9","Subjects":"History, Science, Business"},
                      "st3": {"Name":"Abel","Year level":"Year 9","Subjects":"Geography, Math, Dance"},
                      "st4": {"Name":"Emma", "Year level":"Year 9","Subjects":"Art, Science, English"}}
print (student_dictionary)

print("Student data for st1 is:")
print(student_dictionary.get("st1", "Not found"))
print("Student data for st5 is:")
print (student_dictionary.get("st5", "Not found"))

student_dictionary["st5"] = {"Name":"Logan", "Year level":"Year 9", "Subjects":"HPE, Art, Business"}
student_dictionary["st2"]["Subjects"] = {"Dance", "Geography", "Science"}

cleaned_data = {}
seen_records = []

for student_op, details in student_dictionary.items():
    special_key = (details["Name"], details["Year level"], details["Subjects"])
    if special_key not in seen_records:
        seen_records.append(special_key)
        cleaned_data[student_op] = details

student_op = cleaned_data

print("")
print("After removing all the duplicate data, here's the unique ones:")
print(student_op)

new_student_dictionary = student_dictionary.pop("st4","Not found")

print("Here's the removed student:",new_student_dictionary)

print("====HERE ARE THE FINAL STUDENT SUBJECT RECORDS IN DICTIONARY!====")

for student_op, details in student_dictionary.items():
    print(student_op, ":", details)

print("===THANK YOU===")

