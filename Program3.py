
#----------------------
#Authors: Andrew Tippett, Drew Difilipo, Rubin Smith, Pablo Mendana
#Program: Program 1
#
#Description:
#Program prints invoice for a month of hours worked based on
#hourly rate. If the user has overtime, the program states how much overtime
#has been worked and will print an invoice based on overtime pay.
#If the user enters incorrect inputs, the program will ask them to
#enter the correct inputs.
#---------------------
import BillingModule

RATE_MULTIPLIER = 1.05
NUMBER_OF_WEEKS = 4
REGULAR_HOURS_CAP = 160

#---------------------
#input
#User inputs their name, hourly rate, and hours worked for 4 weeks.
#If the user inputs no name, they will be asked to enter a name.
#If the user enters a rate less than 20, they will be told to
#enter a rate more than 20.
#If the user inputs their weekly hours over 80 or less than 35,
#they will be told to enter a rate in between 35 and 80.
#---------------------
  
def main():
    newEmployee = 'y'

    while newEmployee == 'y':
        
        employee = BillingModule.readEmployeeName("Employee Name: ")
        rate = BillingModule.readHourlyRate("Hourly Rate: ")
        week1 = BillingModule.readWeeklyHours("Enter hours worked for week 1: ")
        week2 = BillingModule.readWeeklyHours("Enter hours worked for week 2: ")
        week3 = BillingModule.readWeeklyHours("Enter hours worked for week 3: ")
        week4 = BillingModule.readWeeklyHours("Enter hours worked for week 4: ")
            
        BillingModule.writeBillingRecord(employee,rate,week1,week2,week3,week4)

#---------------------
#processing
#Calculates the total and average hours, then the Salary for both regular
#and overtime salary.
#---------------------

        totalHours = week1 + week2 + week3 + week4
        averageHours = totalHours / NUMBER_OF_WEEKS
        overtimeHours = totalHours - REGULAR_HOURS_CAP
        overtimeRate = round(rate * RATE_MULTIPLIER, 2)
        overtimeSalary = round(overtimeHours * overtimeRate, 2)

#-------------------
#The if statement creats 2 new variables.
#otMsg prints the message that the inputed employee works a certain amount of
#overtime hours.
#otInvoice prints the overtime invoice in the event that the employee worked
#overtime.
#The if statement also limits regular hours to 160 in the event there is
#overtime hours if not total hours is equal to regular hours.
#-------------------

        if totalHours > REGULAR_HOURS_CAP:
            overtimeHours = totalHours - REGULAR_HOURS_CAP
            regularHours = REGULAR_HOURS_CAP
            otMsg ='\n' + employee + ' worked ' + str(overtimeHours) + \
                    ' hours of overtime'
            otInvoice ='Overtime Hours: ' + format(overtimeHours,'.2f') + ' @ ' + \
                format(overtimeRate,'.2f') + ' = ' + '$' + \
                  format(overtimeSalary,'.2f')
        else:
            otMsg =('\n' + employee + ' worked no overtime.')
            otInvoice = ('')
            overtimeSalary = 0
            regularHours = totalHours

   
        regularSalary = regularHours * rate
        invoiceAmount = regularSalary + overtimeSalary

#--------------
#output
#Prints the mesage that the employee worked x amount of overtime hours
#and prints the invoice.
#At the end of the invoice, the user will be asked if they want to
#enter another employee, entering y for yes.
#--------------

        print(otMsg)
    
        print('\nInvoice')
        print('Resource: ',employee,'\tAverage weekly hours: ',\
              format(averageHours,'.2f'))

        print('\nTotal billable hours: ',\
              format(totalHours, '.2f'),'\trate: $',\
              format(rate, '.2f'),sep='')

        print(otInvoice)
   
        print('Regular Hours: ',format(regularHours,'.2f'), ' @ ',\
              format(rate,'.2f'), ' = ', '$',format(regularSalary,',.2f'),sep='')              

        print('Amount Due: $',format(invoiceAmount,',.2f'),sep='')

        newEmployee=str(input('\nEnter another employee? ("y"=yes): '))



