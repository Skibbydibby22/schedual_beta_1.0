import datetime, os

thing = ["First Day Of School!!", "No School", "No School", "No School", "End of Quarter 1", "Start Of Quarter 2", "Early Dismissal & Parent Teacher Conferences", "No School & Parent Teacher Conferences", "Early Release", "No School", "No School", "No School", "Early Release", "No School/Winter Break", "No School/Winter Break", "No School/Winter Break", "No School/Winter Break", "No School/Winter Break", "No School/Winter Break", "No School/Winter Break", "No School/Winter Break", "No School/Winter Break", "No School/Winter Break", "No School/Winter Break", "No School", "End of Quarter 2", "Start Of Quarter 3", "No School", "Early Release/End Of Quarter 3", "Spring Break", "Spring Break", "Spring Break", "Spring Break", "Spring Break", "Start Of Quarter 4", "No School", "No School", "Last Day Of Schol!!"]
date = ["8/25/22", "9/5/22", "10/7/22", "10/10/22", "10/28/22", "10/31/22", "11/3/22", "11/4/22", "11/22", "11/23/22", "11/24/22", "11/25/22", "12/22/22", "12/23/22", "12/26/22", "12/27/22", "12/28/22", "12/29/22", "12/30/22", "1/2/23", "1/3/23", "1/4/23", "1/5/23", "1/6/23", "1/16/23", "1/20/23", "1/23/23", "2/20/23", "3/24/23", "3/27/23", "3/28/23", "3/29/23", "3/30/23", "3/31/23", "4/3/23", "4/7/23", "5/29/23", "6/7/23"]

x = datetime.datetime.now()
day = x.strftime("%A")
today = str(x.month) + "/" + str(x.day) + "/" + str(x.year)[2: ]
prevday = str(x.month) + "/" + str(x.day) + "/" + str(x.year)[2: ]

while True:
  x = datetime.datetime.now()
  today = str(x.month) + "/" + str(x.day) + "/" + str(x.year)[2: ]
  if today != prevday:
    prevday = str(x.month) + "/" + str(x.day) + "/" + str(x.year)[2: ]
    x = datetime.datetime.now()
    day = x.strftime("%A")
    if os.path.isfile('temp/tempo.txt'):
        os.remove('temp/tempo.txt')
    with open('temp/tempo.txt', 'w') as t:
        t.close()
    os.system('cls')
    
    print("The date today is:", day, today)

    if day == "Saturday" or day == "Sunday":
        t = open('temp/tempo.txt', 'a')
        t.write("Today is an: Weeknd babby!!!!!!")
        print("Today is an: Weeknd babby!!!!!!")
        t.close()
    elif today not in date:
        t = open('temp/tempo.txt', 'a')
        t.write("Nothing Special Today!")
        print("Nothing Special Today!")
        t.close()
    else:
        t = open('temp/tempo.txt', 'a')
        t.write("Today is an:", thing[date.index(today)] + " day")
        print("Today is an:", thing[date.index(today)] + " day")
        t.close()

    t = open('temp/tempo.txt', 'a')
    t.write("Class,                          Period, Teacher,               Room#")
    print("Class,                          Period, Teacher,               Room#")
    t.close()

    if today == 'Saturday' or today == 'Sunday':
        if "8/25/22" <= today <= "10/28/22":
            print("Quarter 1")
            f = open('schedualo\q1.txt', 'r')
            t = open('temp/tempo.txt', 'a')
            t.write(f.read)
            print(f.read())
            t.close()
            f.close()
        elif "10/31/22" <= today <= "1/20/23":
            print("Quarter 2")
            f = open('schedualo\q2.txt', 'r')
            t = open('temp/tempo.txt', 'a')
            t.write(f.read())
            print(f.read())
            t.close()
            f.close()
        elif "1/23/23" <= today <= "3/24/23":
            print("Quarter 3")
            f = open('schedualo\q3.txt', 'r')
            t = open('temp/tempo.txt', 'a')
            t.write(f.read())
            print(f.read())
            f.close()
        elif "4/3/23" <= today <= "6/7/23":
            print("Quarter 4")
            f = open('schedualo\q4.txt', 'r')
            t = open('temp/tempo.txt', 'a')
            t.write(f.read())
            print(f.read())
            f.close()
        else:
            t = open('temp/tempo.txt', 'a')
            t.write("No School Yet")
            print("No School Yet")
            t.close()