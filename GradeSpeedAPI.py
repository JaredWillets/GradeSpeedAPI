## This code is partially influenced by the work of hamptonmoore (https://github.com/hamptonmoore/gradespeed-api-dodea)

import requests as req
from bs4 import BeautifulSoup

requests = req.Session()

class Gradespeed:
    def __init__(self, username, password, schoolId):
        self.username = username
        self.password = password
        self.schoolId = schoolId
        self.grades = []
    def updateGrades(self):
        requests.post(
            "https://dodea.gradespeed.net/pc/StudentLogin.aspx",
            data = {
                "AuthType":"Student",
                "FormType": "Login",
                "DistrictID":"3000010",
                "SchoolID": self.schoolId,
                "Username": self.username,
                "Password": self.password,
                "cmdLogOn": "Sign+In"
            }
        )
        temp = []
        final = []
        request = requests.get("https://dodea.gradespeed.net/pc/ParentStudentGrades.aspx").content
        parse = BeautifulSoup(request, features="html.parser")
        normal = parse.findAll('tr',attrs = {"class":"DataRow"})
        alt = parse.findAll('tr',attrs = {"class":"DataRowAlt"})
        for x in range(len(normal)):
            try:
                temp.append(normal[x])
                temp.append(alt[x])
            except:
                continue
        gradeOrder = parse.find("tr", attrs = {"class":"TableHeader"})
        print(gradeOrder)
        gradeOrder = gradeOrder.findAll("th")
        tempOrder = gradeOrder
        gradeOrder = []
        for grade in tempOrder:
            grade = grade.contents[0]
            gradeOrder.append(grade)
        gradeOrder = gradeOrder[4:]
        for classEl in temp:
            grades = {}
            rawGrades = classEl.findChildren()
            print(rawGrades)
            for gradeNumber, grade in enumerate(gradeOrder):
                grades[grade] = rawGrades[gradeNumber + 3].contents[0]
            final.append({
                "teacher":classEl.find('a',attrs={"class":"EmailLink"}).contents[0],
                "grades":grades
                })
        # print(final)
    def getGrades(self):
        return self.grades
    def getClass(self, classID):
        temp = {}