#----------------------
#Authors: Andrew Tippett, Drew Difilipo, Rubin Smith, Pablo Mendana
#Program: BillingModule
#
#Description:
#Program seperate from our initial Billing Program that gathers the input data
#from the user
#---------------------

def readEmployeeName(eprompt):

    employee = str(input(eprompt))
    while employee == '' :
        print("Employee name must be entered.")
        employee = str(input("\nEmployee Name: "))
        
    return employee

def readHourlyRate(rprompt):
    MINIMUM_RATE = 20.00
    loop = True
    while loop == True:
        try:
            rate = float(input(rprompt))
            while rate < MINIMUM_RATE:
                print("\nInvalid Hourly Rate, Must be at least $20.00/hour")
                try:
                    rate = float(input("Hourly Rate: "))
                except ValueError:
                    print("Please enter a valid rate")
                
        except ValueError:
            print("Please enter a valid rate")
        else:
            loop = False
    return rate

def readWeeklyHours(hprompt):
    NUMBER_OF_WEEKS = 4
    MINIMUM_HOURS = 35
    MAXIMUM_HOURS = 80
    loop2 = True
    while loop2 == True:
        try:
            weekOutput = float(input(hprompt))
            while weekOutput < 35 or weekOutput > 80:
                print("Invalid number of hours, must be between 35 and 80.")
                try:
                    weekOutput = float(input('\n'+hprompt))
                except ValueError:
                    print("Enter a valid number")

        except ValueError:
            print("Enter a valid number")
        else:
            loop2 = False

    return weekOutput

def resetBillingFile():
    open("Billing.txt",'w').close()



def writeBillingRecord(employee,rate,week1,week2,week3,week4):

    outFile = open("Billing.txt",'a')
    outFile.write(employee+'\n'+str(rate)+'\n'+str(week1)+'\n'+str(week2)\
                  +'\n'+str(week3)+'\n'+str(week4)+'\n')         
    outFile.close

