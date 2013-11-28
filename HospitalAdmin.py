import sys, time, random


def GetName():
	firstName=firstNames[random.randint(0,len(firstNames)-1)]
	lastName=familyNames[random.randint(0,len(familyNames)-1)]
	name = firstName+" " +lastName
	return name

def GetPatient():
	name=GetName()
	temp=random.randint(tempLowerLimit,tempUpperLimit)+(random.randint(0,9)/10)
	symptom=symptoms[random.randint(0,len(symptoms)-1)]
	return {"name":name,"temperature":temp,"symptom":symptom}
	
def IsIll(patient):
        ill = False
        if (patient["temperature"]>tempHealthyUpperLimit or patient["temperature"]<tempHealthyLowerLimit):
                ill = True
        if (patient["symptom"]):
                ill=True
        return ill

        
firstNames ="Joshua Laurie Brodie Sara Jeevan Patrick James Nimrod Carlin Morgan Brandon Sarah Ryan Rishi Shaun Jamie".split()
familyNames="Craig Cunninghamn Duff Duthie Francis Kane Lawson Libman Mackenzie McPherson Mills Mir Morrice Purkayastha Wilson McDonald".split()
symptoms=["","","","","","","","","","","coughing","coughing up blood","vomiting","wheezing","vainy-eyed","not breathing","bleeding"]
tempUpperLimit=40.0
tempLowerLimit=34.0
tempHealthyUpperLimit=38
tempHealthyLowerLimit=36

playAgain="y"

while playAgain=="y":
        print("You are Hospital-Admin3.6.1.exe, the revolutionary new software from Simpson Enterprises for hospital administration.")
        time.sleep(0.5)
        print("You have been licenced to the local hospital to help out the hospital with admissions and discharges.")
        time.sleep(0.5)
        print("However "+GetName()+",the hospital manager, is not convinced of your helpfulness. Doctors are checking all your decisions,")
        time.sleep(0.5)
        print("and making too many mistakes will result in your deletion. Survive!")
        time.sleep(2.5)
        mistakes=0
        hours = 0
        
        while mistakes <3:
                #incoming patient
                print("\n\n")
                newPatient=GetPatient()
                print("Incoming Patient\n+---------------------------------------------------------+")
                print("Name:" +newPatient["name"])
                print("Temperature: "+str(newPatient["temperature"]))
                if (newPatient["symptom"]):
                        print("The patient is "+newPatient["symptom"])
                print("+--------------------------------------------------------+")

                responce="m"
                while responce !="y" and responce !="n":
                        print("admit(y/n): ", end ="")
                        responce= input()

                time.sleep(1)
                ill= IsIll(newPatient)
                correct=False
                if (ill and responce=="y"):
                        print("After human examination, "+newPatient["name"]+" was found to be ill.")
                        correct=True
                elif (not ill and responce == "n"):
                        print("After human examination,"+newPatient["name"]+" was sent home.")
                        correct=True
                elif (ill and responce =="n"):
                        print("After human examination, "+newPatient["name"]+" was found out to be ill.")

                elif(not ill and responce =="y"):
                        print("After human examination,"+newPatient["name"]+" was sent back.")
                print("The hospital is" ,end ="")
                if ( not correct):
                       print(" not", end ="")
                       mistakes +=1
                print(" pleased.")
                time.sleep(1)
                hours+=1
                if (not mistakes<3 ):
                        break

                print("\n\n")
        #outgoing patient
                newPatient=GetPatient()
                print("Outgoing Patient\n+---------------------------------------------------------+")
                print("Name:" +newPatient["name"])
                print("Temperature: "+str(newPatient["temperature"]))
                if (newPatient["symptom"]):
                        print("The patient is "+newPatient["symptom"])
                print("+--------------------------------------------------------+")

                responce="m"
                while responce !="y" and responce !="n":
                        print("discharge?(y/n): ", end ="")
                        responce= input()
        
                time.sleep(1)
                ill= IsIll(newPatient)
                correct=False
                if (ill and responce=="n"):
                        print("After human examination, "+newPatient["name"]+" was kept in hospital.")
                        correct=True
                elif (not ill and responce == "y"):
                        print("After human examination,"+newPatient["name"]+" was discharged.")
                        correct=False
                elif (ill and responce=="y"):
                        print("After human examination, "+newPatient["name"]+" was found out to be ill.")
                elif (not ill and responce =="n"):
                       print("After human examination, "+newPatient["name"]+" was sent home.") 
                print("The hospital is" ,end ="")
                if ( not correct):
                       print(" not", end ="")
                       mistakes +=1
                print(" pleased.")
                time.sleep(1)
                hours+=1
        print("you made too many mistakes, and the hospital could not afford to keep you. You were deleted.You worked for "+str(hours)+" hours.")
        print("+--------------------------------------------------------+")
        print("         SYSTEM SHUTDOWN")
        for t in range(10):
                time.sleep(1)
                print("|")

        print("Do you want to play again?(y to play again):")
        playAgain=input()

print("Goodbye.")
time.sleep(2)
sys.exit()
