import GradeSpeedAPI

client = GradeSpeedAPI.Gradespeed("jwil4569@student.dodea.edu", "2023.EDhs.7430!!","66022")

grades = client.getGrades()

hyp = GradeSpeedAPI.Hypothetical(client, grades[0]['links']['Cycle 1'])

print(hyp.getAverage())