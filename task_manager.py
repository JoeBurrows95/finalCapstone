# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], 
                                           DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], 
                                                DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)

#========= functions ===========

# Register a new user with password
def reg_user(user_dictionary, text_file):
    
    '''Add a new user to the text_file'''
    # Request input of a new username
    new_username = input("New Username: ")

    # Handle existing username and allow user to start again
    if new_username in user_dictionary:
        print("This username already exists. Please use another")
        return reg_user(user_dictionary, text_file)
        
    # Request input of a new password
    new_password = input("New Password: ")

    # Request input of password confirmation.
    confirm_password = input("Confirm Password: ")

    # Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # If they are the same, add them to the text_file,
        user_dictionary[new_username] = new_password
        
        with open(text_file, "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))
        
        print("New user added")
        return user_dictionary

    # Otherwise you present a relevant message.
    else:
        print("Passwords do not match")
        return user_dictionary


# Add a new task to a given list of tasks and text_file
def add_task(user_dictionary, list_of_tasks, text_file):
    
    '''Allow a user to add a new task to text_file
    Prompt a user for the following: 
        - A username of the person whom the task is assigned to,
        - A title of a task,
        - A description of the task 
        - The due date of the task.'''
    
    # Check that the username exists, if not return to main menu
    task_username = input("Name of person assigned to task: ")
    if task_username not in user_dictionary.keys():
        print("User does not exist. Please enter a valid username")
        return list_of_tasks
    
    # Take task title and task description from user
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    
    # Take due date and check that it's been entered in a valid datetime format
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break
        # If invalid format, handle the error and allow user to try again
        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    
    # Create a new task with the captured details
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    # Append the new task to the list_of_tasks
    list_of_tasks.append(new_task)
    
    # Write the updated list_of_tasks to the text_file
    with open(text_file, "w") as task_file:
        task_list_to_write = []
        for t in list_of_tasks:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")
    return list_of_tasks


# View all tasks
def view_all(list_of_tasks):
   
    '''Reads the task from list_of_tasks and prints to the console (includes 
    spacing and labelling) 
    '''
    
    disp_str = ""

    # Add each task to a display string in desired format, which can be printed
    for t in list_of_tasks:
        disp_str += f"\nTask: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t \
{t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t \
{t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        
    return disp_str


# View the tasks of the logged in user only
def view_mine(list_of_tasks):
    
    '''Reads the task from list_of_tasks and prints to the console (includes 
    spacing and labelling) 
    '''
    
    disp_str = ""
    task_number = 1
    numbered_task_list = {}

    # Loop through list_of_tasks and add the current user's to a display string
    for i, t in enumerate(list_of_tasks):
        if t['username'] == curr_user:
            disp_str += f"\nTask {task_number}: \t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t \
{t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t \
{t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"

            numbered_task_list[task_number] = i

            task_number += 1
    
    if disp_str == "":
        disp_str = None
    
    return disp_str, numbered_task_list
        
# Enable user to select a task to edit, or return to the main menu
def select_task(task_list_with_numbers):
    
    # Take user input and cast to integer - handle error if not numeric
    while True:
        try:
            task_selection = input("If you'd like to mark a task complete or \
edit it, enter the task number. Otherwise, please enter '-1' to return to \
the main menu:\n")
            task_selection = int(task_selection)
            break
            
        except ValueError:
            print("Please enter a number only")
    
    # Return user to main menu
    if task_selection == -1:
        print("You have chosen to return to the main menu.")
        return task_selection
    
    # Return selected task for next steps
    elif 0 < task_selection <= len(task_list_with_numbers):
        return task_selection
    
    # If the number given isn't a valid task number, user can try again
    else:
        print("Please select a valid task number.\n")
        return select_task(task_list_with_numbers)


# Having selected a task to edit, this function allows the user to confirm
# what kind of change they want to make
def edit_choice(number_of_task, task_number_dictionary, master_task_list):
    
    # Take user input and cast to integer - handle error if not numeric
    while True:
        try:
            option_selection = input('''Select one of the following options below:
1 - Mark the task complete
2 - Edit the task\n''')
            option_selection = int(option_selection)
            break
        except ValueError:
            print("Please enter a number only\n")

    # Ensure user input is a valid option - if not, enable them to try again
    if 1 <= option_selection <= 2:
        task = master_task_list[task_number_dictionary[number_of_task]]
        return option_selection, task, master_task_list
    else:
        print("Please select a valid option.")
        return None, edit_task(number_of_task, task_number_dictionary, 
                                master_task_list), master_task_list

        
# If the user has opted to mark a task complete, this function achieves that                  
def mark_complete(task, master_task_list, task_number_dictionary, 
                  number_of_task, text_file):
    
    if task['completed'] == True:
        print("This task is already marked as complete.")
    else:
    
        # Marks the task as complete and updates the task list accordingly
        task['completed'] = True
        master_task_list[task_number_dictionary[number_of_task]] = task

        # Writes the updated task list to the text file to keep up to date
        with open(text_file, "w") as task_file:
            task_list_to_write = []
            for t in master_task_list:
                str_attrs = [
                    t['username'],
                    t['title'],
                    t['description'],
                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                    "Yes" if t['completed'] else "No"
                ]
                task_list_to_write.append(";".join(str_attrs))
            task_file.write("\n".join(task_list_to_write))
        print(f"Task {number_of_task} has been marked as complete.")
    return master_task_list

# User has chosen to edit details, and can now change the assigned user or due date
def edit_task(task, master_task_list, task_number_dictionary, number_of_task, 
              text_file, user_dictionary):
    
    # Take user input and cast to integer - handle error if not numeric
    while True:
        try:
            edit_selection = input('''What would you like to edit?
1 - Assigned user
2 - Due date\n''')
            edit_selection = int(edit_selection)
            break
        except ValueError:
            print("Please enter a number only")

    while True:

        # Updates the username for the task
        if edit_selection == 1:
            updated_user = input("Please enter the username you wish to assign\
 this task to:\n")
            if updated_user in user_dictionary:
                task['username'] = updated_user
                print(f"You have chosen to assign Task {number_of_task} to \
{updated_user}")
                break
            else:
                print("This user does not exist.")

        # Updates the due date for the task
        elif edit_selection == 2:
            # Take due date and check that it's been entered in a valid datetime format
            while True:
                try:
                    task_due_date = input("Due date of task (YYYY-MM-DD): ")
                    due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                    break
                # If invalid format, handle the error and allow user to try again
                except ValueError:
                    print("Invalid datetime format. Please use the format specified")

            task['due_date'] = due_date_time
            print(f"You have chosen to update the due date of this task to \
{task_due_date}")
            break
        else:
            print("Please select a valid option.")

    # Whatever the change, the below updates the task list and writes the updated
    # task list to the text file
    master_task_list[task_number_dictionary[number_of_task]] = task

    with open(text_file, "w") as task_file:
        task_list_to_write = []
        for t in master_task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))

    print("The task has been updated.")
    return master_task_list

# Updates "task_overview.txt", and creates the file if it doesn't exist
def task_report(list_of_tasks, text_file):

    # Gathering the data items required to generate the report
    total_tasks = len(list_of_tasks)
    
    completed_tasks = 0
    for task in list_of_tasks:
        if task['completed']:
            completed_tasks += 1
    
    uncompleted_tasks = total_tasks - completed_tasks

    overdue_tasks = 0
    for task in list_of_tasks:
        if not task['completed'] and task['due_date'] > datetime.now():
            overdue_tasks += 1

    percentage_incomplete = (uncompleted_tasks / total_tasks) * 100

    percentage_overdue = (overdue_tasks / total_tasks) * 100

    # Generates the report in a user-friendly format
    with open(text_file, "w") as task_overview:
        report_data = f"Total tasks\t\t\t\t: \t\t {total_tasks}\n"
        report_data += f"Completed tasks\t\t\t: \t\t {completed_tasks}\n"
        report_data += f"Incomplete tasks\t\t: \t\t {uncompleted_tasks}\n"
        report_data += f"Overdue tasks\t\t\t: \t\t {overdue_tasks}\n"
        report_data += f"% of tasks incomplete\t: \t\t {percentage_incomplete:.1f}%\n"
        report_data += f"% of tasks overdue\t\t: \t\t {percentage_overdue:.1f}%\n"
        task_overview.write(report_data)
    
    # Provides a printable version - not currently in use but can be if required
    with open(text_file, "r") as task_overview_two:
        printable_version = task_overview_two.read()
        return printable_version
        
    # Updates "user_overview.txt", and creates the file if it doesn't exist
def user_report(list_of_users, list_of_tasks, text_file):
    
    # Gathering the data items required to generate the report
    total_users = len(list_of_users)
    total_tasks = len(list_of_tasks)
    user_tasks = {}
    users = list_of_users.keys()

    # For every user, if they are the assigned user for any task, various
    # counts are updated for that user
    for user in users:
        user_stats = {}
        task_count = 0
        completed_task_count = 0
        incomplete_task_count = 0
        overdue_task_count = 0

        for task in list_of_tasks:
            if user == task['username']:
                task_count += 1
                if task['completed']:
                    completed_task_count += 1
                else:
                    incomplete_task_count += 1
                    if task['due_date'] > datetime.now():
                        overdue_task_count += 1

        user_stats['user_tasks'] = task_count
        # Calculations of the data points to be included in the report
        if task_count != 0:
            user_stats['percent_of_total'] = \
                (task_count / total_tasks) * 100
            user_stats['percent_complete'] = \
                (completed_task_count / task_count) * 100
            user_stats['percent_incomplete'] = \
                (incomplete_task_count / task_count) * 100
            user_stats['percent_overdue'] = \
                (overdue_task_count / incomplete_task_count) * 100
        
        # Handles for if a user has no tasks assigned to them
        else:
            user_stats['percent_of_total'] = 0
            user_stats['percent_complete'] = 0
            user_stats['percent_incomplete'] = 0
            user_stats['percent_overdue'] = 0

        # Adds a dictionary item in the format {user : user_stats}
        user_tasks[user] = user_stats

    # Generates the report in a user-friendly format
    with open(text_file, "w") as user_overview:
        report_data = f"Total users\t\t\t\t\t\t\t: \t\t {total_users}\n"
        report_data += f"Total tasks\t\t\t\t\t\t\t: \t\t {total_tasks}\n"
        report_data += f"\nUser Specific Data\n\n"

        for user in user_tasks:
            report_data += f"User: {user}\n"
            report_data += f"Total user tasks\t\t\t\t\t: \t\t \
{user_tasks[user]['user_tasks']}\n"
            report_data += f"% of total tasks assigned to user\t: \t\t \
{user_tasks[user]['percent_of_total']:.1f}%\n"
            report_data += f"% of user's tasks completed\t\t\t: \t\t \
{user_tasks[user]['percent_complete']:.1f}%\n"
            report_data += f"% of user's tasks incomplete\t\t: \t\t \
{user_tasks[user]['percent_incomplete']:.1f}%\n"
            report_data += f"% of user's tasks overdue\t\t\t: \t\t \
{user_tasks[user]['percent_overdue']:.1f}%\n\n"

        user_overview.write(report_data)
    
    # Provides a printable version - not currently in use but can be if required
    with open(text_file, "r") as user_overview_two:
        printable_version = user_overview_two.read()
        return printable_version

# Created to provide total users or total tasks for displaying statistics
def total_from_overview(overview_file, summary_string):
    
    '''User provides the text file they want to read from, and the string they
    want to put in front of the output. The function then reads the first line
    from the overview_file as both "user_overview.txt" and "task_overview.txt"
    have their totals on the first line
    '''
    with open(overview_file, "r") as text_file:
        first_line = text_file.readline()
    
    # This code extracts the number from the first line, to allow a formatted
    # string with the desired summary to be returned
    number = ""

    for character in first_line:
        if character.isnumeric():
            number += character

    number = int(number)
    return f"{summary_string}: \t\t {number}"


#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True

#====Menu Options====
'''This section of code allows the user to select menu options and subsequently
complete actions such as registering a user, task management, and generating
reports. Only the admin user can display statistics
'''
while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my tasks
gr - generate reports
ds - Display statistics
e - Exit
: ''').lower()

    # Calls the function to register a new user in username_password and "user.txt"
    if menu == 'r':
        username_password = reg_user(username_password, "user.txt")

    # Calls the function to add a task to task_list and update "tasks.txt"
    elif menu == 'a':
        task_list = add_task(username_password, task_list, "tasks.txt")

    # Calls the function to view all tasks in a user-friendly way  
    elif menu == 'va':
        print(view_all(task_list))

    # Calls the function to view the current user's tasks in a user-friendly way
    elif menu == 'vm':
        view_my_tasks, tasks_number_index = view_mine(task_list)     
        
        if view_my_tasks == None:
            print("You have no tasks to display.")
        else:
            print(view_my_tasks)

            # After viewing their tasks, user can choose to edit one
            task_number = select_task(tasks_number_index)
            if task_number == -1:
                continue
            
            # User decides to either mark as complete or edit details
            option, task_to_update, task_list = edit_choice(
                task_number, tasks_number_index, task_list)
            
            # Task is marked as complete
            if option == 1:
                task_list = mark_complete(task_to_update, task_list, 
                                        tasks_number_index, task_number, "tasks.txt")
            
            # User edits either the assigned user or due date
            elif option == 2:
                task_list = edit_task(task_to_update, task_list, tasks_number_index, 
                                    task_number, "tasks.txt", username_password)

    # Generates "task_overview.txt" and "user_overview.txt", informs the user
    elif menu == 'gr':
        overview_of_tasks = task_report(task_list, "task_overview.txt")
        overview_of_users = user_report(username_password, task_list, 
                                        "user_overview.txt")

        print("The task overview report has been generated as \
'task_overview.txt'.")
        print("The user overview report has also been generated as \
'user_overview.txt'.")

    # Displays statistics for admin user - pulls stats from "task_overview.txt"
    # and "user_overview.txt"
    elif menu == 'ds' and curr_user == 'admin': 
        '''If the user is an admin they can display statistics about number of
            users and tasks.'''
        overview_of_tasks = task_report(task_list, "task_overview.txt")
        overview_of_users = user_report(username_password, task_list, 
                                        "user_overview.txt")
        
        print("-----------------------------------")
        print(total_from_overview("user_overview.txt", "Number of users"))
        print(total_from_overview("task_overview.txt", "Number of tasks"))
        print("-----------------------------------")

    # User opts to exit the programme
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    # Invalid choice entered
    else:
        print("You have made a wrong choice, Please try again")