# OOP(Object Oriented Programming)
# It always has classes and objects/instance
# A class always has properties /attributes.
# Objects come from a class
# An object takes on the properties of a class.
# Class name starts with a capital letter and always in singular 
# Syntax of oop
#1. Creating classes
# Cohort class


class cohort:
    def __init__(self,name,description,start_date,end_date):
        self.name = name 
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
cohort1=cohort("Keine","Software enginner","19/6/2024","20/7/2024") 
print(cohort1.name) 
print(cohort1.start_date)
print(cohort1.end_date) 

#
class cohort:
    def __init__(self,cohort_name,total_number_of_students): 
        self.cohort_name=cohort_name
        self.total_number_of_students=total_number_of_students
    def myfunc(self):
        print("The cohort name is " + self.cohort_name + "and the total number of students is" + str(self.total_number_of_students)) 
    cohort1=cohort ("cohort 4",60)  
    cohort1.myfunc() 


class cohort:
    def __init__(self,name,description,start_date,end_date):
        self.name = name
        self.description = description 
        self.start_date = start_date 
        self.end_date = end_date 
cohortthree=cohort("Ayebare","Computer scientist","20/8/2026","17/4/2028") 
print(cohortthree.name)
print(cohortthree.description)
print(cohortthree.start_date)
print(cohortthree.end_date)         


           



