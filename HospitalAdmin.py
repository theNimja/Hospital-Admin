import sys, time, random,pyaudio,wave


def GetName():
	firstName=firstNames[random.randint(0,len(firstNames)-1)]
	lastName=familyNames[random.randint(0,len(familyNames)-1)]
	name = firstName+" " +lastName
	return name

def GetPatient():
        name=GetName()
        temp=random.randint(tempLowerLimit,tempUpperLimit)+(random.randint(0,9)/10)
        symptom=symptoms[random.randint(0,len(symptoms)-1)]
        poorly=""
        if IsIll({"name":name,"temperature":temp,"symptom":symptom,}):
                if random.randint(0,3):
                        poorly=poorlyWords[random.randint(0,len(poorlyWords)-1)]

        else:
                if not random.randint(0,3):
                        poorly=poorlyWords[random.randint(0,len(poorlyWords)-1)]
        return {"name":name,"temperature":temp,"symptom":symptom,"poorly?":poorly}
	
def IsIll(patient):
        ill = False
        if (patient["temperature"]>tempHealthyUpperLimit or patient["temperature"]<tempHealthyLowerLimit):
                ill = True
        if (patient["symptom"]):
                ill=True
        return ill
def PlaySound(sound):
        CHUNK = 1024

        #       if len(sys.argv) < 2:
        #         sys.exit(-1)

        wf = wave.open(sound, 'rb')

        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        data = wf.readframes(CHUNK)

        while data != '':
            stream.write(data)
            data = wf.readframes(CHUNK)

        stream.stop_stream()
        stream.close()

        p.terminate()  
        
firstNames ="Joshua Laurie Brodie Sara Jeevan Patrick James Nimrod Carlin Morgan Brandon Sarah Ryan Rishi Shaun Jamie".split()
familyNames="Craig Cunninghamn Duff Duthie Francis Kane Lawson Libman Mackenzie McPherson Mills Mir Morrice Purkayastha Wilson McDonald".split()
symptoms=["","","","","","","","","","","coughing","coughing up blood","vomiting","wheezing","vainy-eyed","not breathing","bleeding"]
tempUpperLimit=40.0
tempLowerLimit=34.0
tempHealthyUpperLimit=38
tempHealthyLowerLimit=36
poorlyWords="poorly bad sick ill delusional".split()

playAgain="y"

while playAgain=="y":
        PlaySound("beepbeep.wav")
        print("You are Hospital-Admin, the revolutionary new software from Simpson Enterprises for hospital administration.")
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
                PlaySound("sick.wav")
                print("Incoming Patient\n+---------------------------------------------------------+")
                print("Name:" +newPatient["name"])
                print("Temperature: "+str(newPatient["temperature"]))
                if (newPatient["symptom"]):
                        print("The patient is "+newPatient["symptom"]+".")
                if (newPatient["poorly?"]):
                        print("The patient looks "+newPatient["poorly?"]+".")
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
                PlaySound("sick2.wav")
                print("Outgoing Patient\n+---------------------------------------------------------+")
                print("Name:" +newPatient["name"])
                print("Temperature: "+str(newPatient["temperature"]))
                if (newPatient["symptom"]):
                        print("The patient is "+newPatient["symptom"]+".")
                if (newPatient["poorly?"]):
                        print("The patient looks "+newPatient["poorly?"]+".")
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
                        correct=True
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
        print("                  GAME OVER                      ")
        PlaySound("flat.wav")
      
        print("Do you want to play again?(y to play again):")
        playAgain=input()
        
print("Goodbye.")
time.sleep(2)
sys.exit()
