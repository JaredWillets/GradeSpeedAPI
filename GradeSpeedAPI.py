## This code is partially influenced by the work of hamptonmoore (https://github.com/hamptonmoore/gradespeed-api-dodea)

import requests as req
from bs4 import BeautifulSoup

def getTable(table):
    finalTable = []
    for rowNumber, row in enumerate(table.findAll("tr")[:-1]):
        tempRow = []
        for colNumber, col in enumerate(row.findAll(['td','th'])):
            try: tempRow.append(col.contents[0])
            except: tempRow.append("")
        finalTable.append(tempRow)
    return finalTable
class Gradespeed:
    def __init__(self, username, password, schoolId):
        self.requests = req.Session()
        self.username = username
        self.password = password
        self.schoolId = schoolId
        self.grades = []
        response = self.requests.post(
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
        if response == 200:
            raise Exception("Incorrect Credentials")
    def updateGrades(self):
        temp = []
        final = []
        request = self.requests.get("https://dodea.gradespeed.net/pc/ParentStudentGrades.aspx").content
        parse = BeautifulSoup(request, features="html.parser")
        temp = parse.findAll('tr',attrs = {"class":["DataRow", "DataRowAlt"]})
        gradeOrder = parse.find("tr", attrs = {"class":"TableHeader"})
        schoolCount = len(parse.findAll("table", attrs = {"class":"DataTable"}))
        gradeOrder = gradeOrder.findAll("th")
        tempOrder = gradeOrder
        gradeOrder = []
        for grade in tempOrder:
            grade = grade.contents[0]
            gradeOrder.append(grade)
        gradeOrder = gradeOrder[4:]
        for classNumber, classEl in enumerate(temp):
            grades = {}
            ids = {}
            rawGrades = classEl.findChildren(recursive = False)
            for gradeNumber, grade in enumerate(gradeOrder):
                try:
                    grades[grade] = rawGrades[4 + gradeNumber].contents[0].contents[0]
                    try:
                        ids[grade] = "https://dodea.gradespeed.net/pc/ParentStudentGrades.aspx"+rawGrades[4 + gradeNumber].contents[0]['href']
                    except:
                        ids[grade] = ""
                except: 
                    grades[grade]= ""
                    ids[grade] = ""
            final.append({
                "name":classEl.find_all('td')[1].contents[0],
                "teacher":classEl.find('a',attrs={"class":"EmailLink"}).contents[0],
                "grades":grades,
                "links":ids
                })
        self.grades = final
        self.schoolCount = schoolCount
    def getGrades(self):
        self.updateGrades()
        return self.grades
    def getClass(self, classURL):
        self.updateGrades()
        temp = []
        gradePage = BeautifulSoup(self.requests.get(classURL).content, features="html.parser")
        grades = gradePage.findAll("table", attrs = {"class":"DataTable"})
        grades = grades[self.schoolCount:]
        for categoryNumber, category in enumerate(grades):
            average = category.findAll('tr')[-1].findChildren()[3].contents[0]
            categoryName = gradePage.findAll("span", attrs = {"class":"CategoryName"})[categoryNumber].contents[0].split(' - ')[0]
            weight = gradePage.findAll("span", attrs = {"class":"CategoryName"})[categoryNumber].contents[0].split(' - ')[1]
            gradesList = []
            for assignment in getTable(category)[1:]:
                tempDict = {}
                for columnNumber in range(len(assignment)):
                    tempDict[getTable(category)[0][columnNumber].replace("\xa0","")] = assignment[columnNumber].replace("\xa0","")
                gradesList.append(tempDict)
            # print(average)
            # print(weight)
            # print(categoryName)
            temp.append({
                "average":average,
                "category":categoryName,
                "weight":weight,
                "grades":gradesList
            })
        final = {
            "categories":temp,
            "className":gradePage.find("h3", attrs={"class":"ClassName"}).contents[0].split(" (")[0],
            "average":gradePage.find("p",attrs={"class":"CurrentAverage"}).contents[0].split(": ")[1]
        }
        return final