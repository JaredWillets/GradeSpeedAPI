# GradeSpeedAPI
 An API to access grades from DoDEA Gradespeed

To load the API code, use this command:

`import GradeSpeedAPI`

To create a client, use this command:

`client = GradeSpeedAPI.Gradespeed(username, password, schoolID)`

This schoolID can be gained by inspecting the list from the DoDEA GradeSpeed login page. More information about how to find these credentials can be found in hamptonmoore's older GradeSpeed API (https://github.com/hamptonmoore/gradespeed-api-dodea). You can gain the base grades by using the `getGrades()` command, which will automatically call the `updateGrades()` function. To get more detailed information about a single class, the `getClass()` function should be used.

An example of these functions would be:
`print(client.getGrades())`
Which would print:
`[{'name': 'AP Computer Sci A+', 'teacher': 'Doe, Jane', 'grades': {'Cycle 1': 'A+', 'Cycle 2': 'A+', 'Exam 1': 'A', 'Semester 1': 'A+', 'Cycle 3': 'A+', 'Cycle 4': '', 'Exam 2': '', 'Semester 2': 'A+'}, 'links': {'Cycle 1': '...', 'Cycle 2': '...', 'Exam 1': '', 'Semester 1': '', 'Cycle 3': '...', 'Cycle 4': '', 'Exam 2': '', 'Semester 2': ''}}, {'name': 'AP US History', 'teacher': 'Doe, John', 'grades': {'Cycle 1': 'A', 'Cycle 2': 'A-', 'Exam 1': 'A', 'Semester 1': 'A', 'Cycle 3': 'A', 'Cycle 4': '', 'Exam 2': '', 'Semester 2': 'A'}, 'links': {'Cycle 1': '...', 'Cycle 2': '...', 'Exam 1': '', 'Semester 1': '', 'Cycle 3': '...', 'Cycle 4': '', 'Exam 2': '', 'Semester 2': ''}}]`

The links in this output was changed to elipses to conserve space, but the links would look someting like this: `https://dodea.gradespeed.net/pc/ParentStudentGrades.aspx?data=M3w3NDMwNzU0NTY5fDAxMjEzMTN8U1NVNjExVXwwMDF8MzAwMDAxMHw2NjAyMg%3d%3d`

Getting class specific grades is simple with the use of this link. The following line is all that is needed:

`print(client.getClass(classURL))` 

This is where classURL is a url like the one shown above. This should generate an output like this:

`{'categories': [{'average': '97.94', 'category': 'Assignment', 'weight': '100%', 'grades': [{'Assignment': 'OT1. Exit Ticket/Google Chat Message', 'Assigned': 'Aug-23', 'Due': 'Aug-24', 'Points Earned': '4', 'Points Possible': '4', 'Note': '', '': ''}]}], 'className': 'AP Computer Sci A+', 'average': '98'}`

A sample assignment looks like this: 

`{'Assignment': 'OT1. Exit Ticket/Google Chat Message', 'Assigned': 'Aug-23', 'Due': 'Aug-24', 'Points Earned': '4', 'Points Possible': '4', 'Note': '', '': ''}`

These dictionary keys are given by the table headers for the grade table. The categories have the attributes: *category* (title), *average*, *weight*, and *grades*. The attributes of the class object include: categories, className, and average. The *categories* contains a list of the different categories, which has a list of the different assignments inside. The other two values seem self-explanatory.

More updates will be coming soon. Please email me any time at willetsjared@gmail.com with questions, suggestions, or concerns.

Features coming soon:

- Hypothetical Grade Calculator
- GUI
- Online API using Flask
- JavaScript Version
- Attendance and other GradeSpeed Features
