# random generators for project
#    doctors(employee_id*, first_name, last_name)
#    patients(patient_id*, first_name, last_name, phone, address, city, notes)
#    vitals(foregin(appointment_id), foregien(patient_id), weight, bp_sys, bp_dia, height, pulse)
#    illnesses(unique_id*?, name, treatment, symptoms)
#    check-up(appointment_number, date-time, patient_id, doctor_id)
#    specialty(doctor_id, illness_id*?)
#    infected/infects(patient_id, illness_id*?)

## Creates data for what became database_2.  Vitals table is combined with check-up
## table in database_1 now. 


import math, random, time
def create_doctors():
    first_names = ['Jeff', 'Sam','Travis','John', 'Michael','Fred',
                   'Horris', 'Borris', 'Ryan', 'Stuart', 'Matt', 'Cory',
                   'David', 'Henry','Hank', 'Clive', 'Brad', 'Chris', 'Larry',
                   'Englebert', 'Sammie', 'Owen', 'Tim', 'Eddie', 'Francis',
                   'Finkle', 'Clarice', 'Erica', 'Broomhilda', 'Casey', 'Samantha',
                   'Julia', 'Michelle', 'Andrea', 'Laura']
    last_names = ['Hill', 'Smith', 'Schlafly', 'Busch', 'Doctor', 'Anderson',
                  'Miller', 'Stephenson', 'Platt', 'Sunnen', 'Pain', 'Robotnik',
                  'Frederickson', 'Chowder', 'Pratt', 'Frizzielanki', 'Thibadaux',
                  'Humperdink', 'Damon', 'Owens', 'Gerkin', 'McLovin',
                  'Izzard', 'Moriarty', 'Finklemeister', 'Three-Toes', 'Forester',
                  'Trump', 'Clinton', 'Davis Jr.', 'Terrlumpkin', 'Gordronovits',
                  'Rumperstein', 'Goldberger', 'Black', 'Brown', 'Laridopolis',
                  'Renault', 'Redinbacher', 'Carmike','BARNETT','GRAVES','JIMENEZ',
                  'HORTON','SHELTON','BARRETT','OBRIEN','CASTRO','SUTTON','GREGORY',
                  'MCKINNEY','LUCAS','MILES','CRAIG','RODRIQUEZ','CHAMBERS','HOLT',
                  'LAMBERT','FLETCHER','WATTS','BATES','HALE','RHODES','PENA','BECK',
                  'NEWMAN','HAYNES','MCDANIEL','MENDEZ','BUSH','VAUGHN','PARKS',
                  'DAWSON','SANTIAGO','NORRIS','HARDY','LOVE','STEELE','CURRY',
                  'POWERS','SCHULTZ','BARKER','GUZMAN','PAGE','MUNOZ','BALL','KELLER',
                  'CHANDLER','WEBER','LEONARD','WALSH','LYONS','RAMSEY','WOLFE',
                  'SCHNEIDER','MULLINS','BENSON','SHARP','BOWEN','DANIEL','BARBER',
                  'CUMMINGS','HINES','BALDWIN','GRIFFITH','VALDEZ','HUBBARD','SALAZAR',
                  'REEVES','WARNER','STEVENSON','BURGESS','SANTOS','TATE','CROSS',
                  'GARNER','MANN','MACK','MOSS','THORNTON','DENNIS','MCGEE','FARMER',
                  'DELGADO','AGUILAR','VEGA','GLOVER','MANNING','COHEN','HARMON',
                  'RODGERS','ROBBINS','NEWTON','TODD','BLAIR','HIGGINS''INGRAM',
                  'REESE','CANNON','STRICKLAND','TOWNSEND','POTTER','GOODWIN',
                  'WALTON','ROWE','HAMPTON','ORTEGA','PATTON']
    numDocs = 100
    i = 0
    while (i<numDocs):
        randFirstName = first_names[random.randint(0,len(first_names))-1]
        randLastName = last_names[random.randint(0,len(last_names))-1]
        string_record = "INSERT INTO doctors VALUES(" + str(i+1)+",'" + randFirstName.upper() + "','"+randLastName.upper()+ "');"
        print(string_record)
        i+=1

def create_patients():
    first_names = ['Jeff', 'Sam','Travis','John', 'Michael','Fred',
                   'Horris', 'Borris', 'Ryan', 'Stuart', 'Matt', 'Cory',
                   'David', 'Henry','Hank', 'Clive', 'Brad', 'Chris', 'Larry',
                   'Englebert', 'Sammie', 'Owen', 'Tim', 'Eddie', 'Francis',
                   'Finkle', 'Clarice', 'Erica', 'Broomhilda', 'Casey', 'Samantha',
                   'Julia', 'Michelle', 'Andrea', 'Laura']
    last_names = ['Hill', 'Smith', 'Schlafly', 'Busch', 'Doctor', 'Anderson',
                  'Miller', 'Stephenson', 'Platt', 'Sunnen', 'Pain', 'Robotnik',
                  'Frederickson', 'Chowder', 'Pratt', 'Frizzielanki', 'Thibadaux',
                  'Humperdink', 'Damon', 'Owens', 'Gerkin', 'McLovin',
                  'Izzard', 'Moriarty', 'Finklemeister', 'Three-Toes', 'Forester',
                  'Trump', 'Clinton', 'Davis Jr.', 'Terrlumpkin', 'Gordronovits',
                  'Rumperstein', 'Goldberger', 'Black', 'Brown', 'Laridopolis',
                  'Renault', 'Redinbacher', 'Carmike','BARNETT','GRAVES','JIMENEZ',
                  'HORTON','SHELTON','BARRETT','OBRIEN','CASTRO','SUTTON','GREGORY',
                  'MCKINNEY','LUCAS','MILES','CRAIG','RODRIQUEZ','CHAMBERS','HOLT',
                  'LAMBERT','FLETCHER','WATTS','BATES','HALE','RHODES','PENA','BECK',
                  'NEWMAN','HAYNES','MCDANIEL','MENDEZ','BUSH','VAUGHN','PARKS',
                  'DAWSON','SANTIAGO','NORRIS','HARDY','LOVE','STEELE','CURRY',
                  'POWERS','SCHULTZ','BARKER','GUZMAN','PAGE','MUNOZ','BALL','KELLER',
                  'CHANDLER','WEBER','LEONARD','WALSH','LYONS','RAMSEY','WOLFE',
                  'SCHNEIDER','MULLINS','BENSON','SHARP','BOWEN','DANIEL','BARBER',
                  'CUMMINGS','HINES','BALDWIN','GRIFFITH','VALDEZ','HUBBARD','SALAZAR',
                  'REEVES','WARNER','STEVENSON','BURGESS','SANTOS','TATE','CROSS',
                  'GARNER','MANN','MACK','MOSS','THORNTON','DENNIS','MCGEE','FARMER',
                  'DELGADO','AGUILAR','VEGA','GLOVER','MANNING','COHEN','HARMON',
                  'RODGERS','ROBBINS','NEWTON','TODD','BLAIR','HIGGINS''INGRAM',
                  'REESE','CANNON','STRICKLAND','TOWNSEND','POTTER','GOODWIN',
                  'WALTON','ROWE','HAMPTON','ORTEGA','PATTON']
    address = ['Main St.', 'Oak St.', 'Pine Rd.', 'Cedar St.', 'Mapl Blvd.', 'Elm St.',
               'View Rd.', 'Washington Ave.', 'Beach Rd.', 'Tropics St.', 'Far Ln.', 'Easterly Wind Ln.',
               'Hill St.', 'First St.', 'Second St.', 'Third St.', 'Fourth St.', 'Fifth St.', 'Sixth St.', 'Seventh St.']
    city = ['Orlando', 'Melbourne', 'Indialantic', 'Satellite Beach', 'Palm Bay', 'Malabar', 'Grant']
    numPats = 100
    i=0
    while (i<numPats):
        randFirstName = first_names[random.randint(0,len(first_names))-1]
        randLastName = last_names[random.randint(0,len(last_names))-1]
        randAddress = address[random.randint(0,len(address))-1]
        randAddress = str(random.randint(0,1000))+' ' +randAddress
        randCity = city[random.randint(0,len(city))-1]
        phone_number = random.randint(1111111,10000000)
        phone_number = phone_number + 3210000000

        string_record = "INSERT INTO patients VALUES(" + str(i+1)+",'" + randFirstName.upper() + "','"+randLastName.upper()+"',"+str(phone_number)+ ",'"+randAddress.upper()+ "','"+randCity.upper()+ "','');"
        print(string_record)
        i+=1

def create_vitals():
    numVitals = 100
    i = 0
    listNum = []
    for j in range(100):
        thing = j+1
        listNum.append(thing)
    while (i<numVitals):
        randI = random.randint(0,len(listNum)-1)
        randApp = listNum[randI]
        listNum.remove(randApp)
        randWeight = random.randint(120,300)
        randBPSys = random.randint(50,160)
        randBPDias = randBPSys-30
        randHeight = random.randint(59,80)
        randPulse = random.randint(60,130)
        string_record = "INSERT INTO vitals VALUES(" + str(i+1)+"," + str(randApp) +","+ str(randWeight)+ ","+str(randBPSys)+ ","+str(randBPDias)+ ","+str(randHeight)+","+str(randPulse)+");"
        print(string_record)
        i+=1

def create_infected():
    i=0
    listNum = []
    for j in range(100):
        thing = j+1
        listNum.append(thing)
    while (len(listNum)>0):
        randI = random.randint(0,len(listNum)-1)
        randPat = listNum[randI]
        listNum.remove(randPat)
        randIll = random.randint(0,101)
        string_record = "INSERT INTO infected VALUES(" + str(i+1)+"," + str(randPat) + ","+str(randIll)+ ");"
        print(string_record)
        i+=1

def create_specialty():
    i=0
    listNum = []
    for j in range(100):
        thing = j+1
        listNum.append(thing)
    while (len(listNum)>0):
        randI = random.randint(0,len(listNum)-1)
        randDoc = listNum[randI]
        listNum.remove(randDoc)
        randIll = random.randint(0,101)
        string_record = "INSERT INTO specialty VALUES(" + str(i+1)+"," + str(randDoc) + ","+str(randIll)+ ");"
        print(string_record)
        i+=1

def create_checkup():
    i = 0
    listNumDocs = []
    listNumPats = []
    for j in range(100):
        thing = j+1
        listNumDocs.append(thing)
    for h in range(100):
        this = h+1
        listNumPats.append(this)
    while (len(listNumDocs)>0):
        date = randomDate("1/1/2008 1 PM", "1/1/2009 4 AM", random.random())
        randI = random.randint(0,len(listNumDocs)-1)
        randDoc = listNumDocs[randI]
        listNumDocs.remove(randDoc)
        randJ = random.randint(0,len(listNumPats)-1)
        randPat = listNumPats[randJ]
        listNumPats.remove(randPat)
        string_record = "INSERT INTO check_up VALUES(" + str(i+1)+",'" + date + "',"+str(randDoc)+","+str(randPat)+ ");"
        print(string_record)
        i+=1

def create_illness():
    ##This creates the template, needs to be manually edited
    i = 0
    numIll = 100
    while (i<numIll):
        illness = "Alopecia"
        symptoms = "Bald"
        treatment = "Apply lotion"
        string_record = "INSERT INTO illnesses VALUES(" + str(i+1)+",'" + illness.upper() + "','"+treatment.upper()+ "','" + symptoms.upper()+ "');"
        print(string_record)
        i+=1
        



def strTimeProp(start, end, format, prop):
##    Get a time at a proportion of a range of two formatted times.
##
##    start and end should be strings specifying times formated in the
##    given format (strftime-style), giving an interval [start, end].
##    prop specifies how a proportion of the interval to be taken after
##    start.  The returned time will be in the specified format.


    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%m/%d/%Y %I %p', prop)
