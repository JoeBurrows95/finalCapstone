# Task Manager Capstone Project
## Project Description
This project enables users to manage and edit tasks, as well as creating new users and generating reports on both tasks and users. Once logged in, a user is able to:
- Register a user
- Add a task
- View all tasks
- View their own tasks, with the ability to mark complete and edit assignee or due date
- Generate reports on tasks and users
- Display statistics on total tasks and users (admin user only)

An example use case for this tool might be a project team working towards a deadline - the Task Manager would serve as a central point for team members to add, update, and track tasks. The reports provide insights on complete, incomplete, and overdue tasks, overall and also by user.

## Installation
You need an IDE to run the code on - I use VS Code. Also ensure both text files - 'tasks.txt' and 'user.txt' - exist in the same folder as the Python file ('task_manager.py).

## Usage
In order to use the Task Manager, you need log-in credentials. These can be found in the 'user.txt' file - recommend using the 'admin' in the first instance as this user has access to all functionality. You can also register new users once you're logged in.

In the below example usage I'll show, with accompanying screenshots, the how-to and results of performing each available action.
### 1. Register a user

Having successfully logged in, the user is presented with the following in the terminal:

![Screenshot 2024-03-04 at 14 30 15](https://github.com/JoeBurrows95/finalCapstone/assets/153125852/790e724e-9df1-4779-a197-ae6e0c388dfa)

To register a user, we enter 'r', and are then asked to enter the new username and confirm their password. Provided this user doesn't already exist, and the passwords match, the new user will be added to 'user.txt' as shown below:

_Text file before new user added_

![Screenshot 2024-03-04 at 14 33 26](https://github.com/JoeBurrows95/finalCapstone/assets/153125852/b526a4e3-c261-4268-a753-b4457c1b0af9)

_Adding new user details_

![Screenshot 2024-03-04 at 14 37 53](https://github.com/JoeBurrows95/finalCapstone/assets/153125852/31c76ebe-2918-4a80-8e65-3133a5030fcd)

_Text file after new user added_

![Screenshot 2024-03-04 at 14 39 06](https://github.com/JoeBurrows95/finalCapstone/assets/153125852/9de4b3fd-4357-454e-ada1-affdb3d65011)

### 2. Add a task

The logged in user can add a brand new task by entering 'a', which will be added to 'tasks.txt' and viewable via "View all tasks". They're asked to provide:
- Username of the assignee
- Title of the task
- Description of the task
- Due date

![Screenshot 2024-03-04 at 15 15 45](https://github.com/JoeBurrows95/finalCapstone/assets/153125852/c6bf6723-8b9b-478f-93dd-8b4fcc006cb1)

As well as the above, the programme also passes through creation date and completion status, which defaults to 'No', to 'tasks.txt'

![Screenshot 2024-03-04 at 15 18 03](https://github.com/JoeBurrows95/finalCapstone/assets/153125852/84181b02-6293-4b9c-b873-85b437d3262d)


### 3. View all tasks

By entering 'va', the user can view all tasks. This calls a function which prints the task list in a user-friendly format. The task list derives from 'tasks.txt' and is kept up to date as the text file is updated. Here's a snippet of the output:

![Screenshot 2024-03-04 at 15 21 58](https://github.com/JoeBurrows95/finalCapstone/assets/153125852/02079fdf-aa60-4815-9278-cd4d70c77802)


### 4. View my tasks

This, initiated by entering 'vm', behaves similarly to "View all tasks" but with a couple of differences - of course, it only displays the tasks assigned to the logged in user. But it also numbers the tasks to allow the user to select one if they would like to edit it. If they do so, they can either mark the task as complete or edit details, in this case the assignee or due date. Here's an example of a user viewing their tasks and changing the assignee, with the resulting change in 'tasks.txt' below it.

_Viewing my tasks and changing assignee_

![Screenshot 2024-03-04 at 15 28 52](https://github.com/JoeBurrows95/finalCapstone/assets/153125852/794a3234-37ef-4b13-8023-2a9092c5bd0d)

_Updated text file_

![Screenshot 2024-03-04 at 15 30 38](https://github.com/JoeBurrows95/finalCapstone/assets/153125852/5a4a4970-dc7e-4230-babb-065a00166a66)

If the user chooses to mark the task as complete, the value 'No' in 'tasks.txt' changes to Yes.

### 5. Generate reports

When 'gr' is entered, two reports are generated in the form of new text files. The first is "user_overview.txt" and the second is "task_overview.txt". If the files don't already exist, they'll be created when the function to generate them is called. If they already exist, they'll be updated with the latest information. Here's a snippet of what they both look like:

_User Overview_

![Screenshot 2024-03-04 at 15 34 19](https://github.com/JoeBurrows95/finalCapstone/assets/153125852/80937ba8-5337-4292-91ad-2ee0f326dde5)

_Task Overview_

![Screenshot 2024-03-04 at 15 34 38](https://github.com/JoeBurrows95/finalCapstone/assets/153125852/1762523f-fb07-4f55-9f7e-840d4a337453)


### 6. Display statistics

Available only to the admin user, this simply displays the total number of users and total number of tasks in the terminal. The programme pulls this information from 'user_overview.txt' and 'task_overview.txt', so the functions to generate these are called when 'ds' is entered by the admin user to ensure the most up to date information is being used.

![Screenshot 2024-03-04 at 15 36 37](https://github.com/JoeBurrows95/finalCapstone/assets/153125852/a3d5eee5-791e-4e1c-9451-fd3ea5b5cd36)

### When you're finished

When the user is done, they can simply enter 'e' from the main menu to exit the programme.

## Credits
Thanks to the HyperionDev team for countless guided learning hours and materials, and guidance on this Capstone Project.
