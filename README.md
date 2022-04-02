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

This code creates a hypothetical class:

`hyp = GradeSpeedAPI.Hypothetical(client, classURL)`

This is assuming that classURL is a working URL to a GradeSpeed class such as the one seen above. This imports the grades and prepares the grade object. The following code shows how to add an assignment to the hypothetical class:

`hyp.addAssignment("[Insert Name here]",[Points Earned],[Points Possible])`

To get the new averages as well as set the class' grades object, user the `getAverage()` command, which is shown here:

`print(hyp.getAverage())`

This line prints the percentage value of the overall average of the class and sets the category averages. These category averages can be accesssed like this:

`print(hyp.getClass())`

This will return a class ouptut similar to the normal grades, but with the hypothetical assignments added in and averages adjusted.

Attendance is a newer feature that was recently added. To get attendance information, use the following lines of code:

`client.getAttendance()`

This line will return an output that looks similar to this:

`{'12/17/2021': [('HRM', 'E'), ('P2', 'Absent Excused')]}`