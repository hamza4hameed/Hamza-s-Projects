import tkinter
from tkinter import ttk
from tkinter import messagebox
import sqlite3

# def enter_data():
#     accepted = accept_var.get()
    
#     if accepted=="Accepted":
#         # User info
#         firstname = first_name_entry.get()
#         lastname = last_name_entry.get()
        
#         if firstname and lastname:
#             title = title_combobox.get()
#             age = age_spinbox.get()
#             nationality = nationality_combobox.get()
            
#             # Course info
#             registration_status = reg_status_var.get()
#             numcourses = numcourses_spinbox.get()
#             numsemesters = numsemesters_spinbox.get()
            
#             print("First name: ", firstname, "Last name: ", lastname)
#             print("Title: ", title, "Age: ", age, "Nationality: ", nationality)
#             print("# Courses: ", numcourses, "# Semesters: ", numsemesters)
#             print("Registration status", registration_status)
#             print("------------------------------------------")
            
#             # Create Table
#             conn = sqlite3.connect('data.db')
#             table_create_query = '''CREATE TABLE IF NOT EXISTS Student_Data 
#                     (firstname TEXT, lastname TEXT, title TEXT, age INT, nationality TEXT, 
#                     registration_status TEXT, num_courses INT, num_semesters INT)
#             '''
#             conn.execute(table_create_query)
            
#             # Insert Data
#             data_insert_query = '''INSERT INTO Student_Data (firstname, lastname, title, 
#             age, nationality, registration_status, num_courses, num_semesters) VALUES 
#             (?, ?, ?, ?, ?, ?, ?, ?)'''
#             data_insert_tuple = (firstname, lastname, title,
#                                   age, nationality, registration_status, numcourses, numsemesters)
#             cursor = conn.cursor()
#             cursor.execute(data_insert_query, data_insert_tuple)
#             conn.commit()
#             conn.close()

            
                
#         else:
#             tkinter.messagebox.showwarning(title="Error", message="First name and last name must be required.")
#     else:
#         tkinter.messagebox.showwarning(title= "Error", message="You have not accepted the terms")
def save():
    f = open("data_entry_form.txt", "a")
    f.write(f"Frist Name: {first_name_entry.get()}\n")
    f.write(f"Last Name: {last_name_entry.get()}\n")
    f.write(f"Title: {title_combobox.get()}\n")
    f.write(f"Age: {age_spinbox.get()}\n")
    f.write(f"Nationality: {nationality_combobox.get()}\n")    
    f.write(f"Courses: {numcourses_spinbox.get()}\n")
    f.write(f"Semester(s): {numsemesters_spinbox.get()}\n")
    f.write(f"registration status: {accept_var .get()}\n\n")
    f.write(f"-------------------------\n\n")
    f.close()
window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

first_name_entry = tkinter.StringVar()
last_name_entry = tkinter.StringVar()
title_combobox = tkinter.StringVar()
age_spinbox = tkinter.StringVar()
nationality_combobox = tkinter.StringVar()
numcourses = tkinter.StringVar()
numsemesters_spinbox = tkinter.StringVar()
accept_var = tkinter.IntVar()
# Saving User Info
user_info_frame =tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row= 0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms.", "Dr."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values=["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Saving Course Info
courses_frame = tkinter.LabelFrame(frame, text="Course Information")
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tkinter.Label(courses_frame, text="Registration Status")

registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered",onvalue="Registered",
                                        offvalue="Not registered")

registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tkinter.Label(courses_frame, text= "# Completed Courses")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tkinter.Label(courses_frame, text="# Semesters")
numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text= "I accept the terms and conditions.",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

# Button
button = tkinter.Button(frame, text="Enter data", command= save)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()