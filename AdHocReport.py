import Program3
import BillingModule

RATE_MULTIPLIER = 1.05
NUMBER_OF_WEEKS = 4
REGULAR_HOURS_CAP = 160

def Report():
    completeTotal = 0
    employeeCount = 0
    completeInvoice = 0
    
    print("Employee\t" + "Rate\t" + "week1\t" + "week2\t" + "week3\t"\
          + "week4\t"+"Hours\t"+"Total")
    try:
        outFile = open("Billing.txt",'r')
        

        employee = outFile.readline().rstrip('\n')
        

        while employee != "":
            employeeCount += 1
            hourCount = employeeCount*4
            
            rate = outFile.readline().rstrip('\n')
            week1 = outFile.readline().rstrip('\n')
            week2 = outFile.readline().rstrip('\n')
            week3 = outFile.readline().rstrip('\n')
            week4 = outFile.readline().rstrip('\n')
            
            totalHours = round((float(week1) + float(week2) + float(week3)\
                          + float(week4)),2)
            overtimeHours = totalHours - REGULAR_HOURS_CAP
            overtimeRate = round(float(rate) * RATE_MULTIPLIER, 2)
            overtimeSalary = round(overtimeHours * overtimeRate, 2)
        
            completeTotal += round(totalHours, 2)
            

            if totalHours > REGULAR_HOURS_CAP:
                overtimeHours = totalHours - REGULAR_HOURS_CAP
                float(regularHours) == REGULAR_HOURS_CAP
            else:
                overtimeSalary = 0
                regularHours = totalHours

       
            regularSalary = regularHours * float(rate)
            invoiceAmount = regularSalary + overtimeSalary
            
            completeInvoice += invoiceAmount
            averageHours = round(completeTotal/hourCount, 2)
            

    
            
            print(employee+'\t'+rate+'\t'+week1+'\t'+week2+'\t'+\
                    week3+'\t'+week4+'\t'+format(totalHours,'.2f')+'\t'\
                    +'$'+format(invoiceAmount,'.2f'))
                                                       
            employee = outFile.readline().rstrip('\n')
            
        
        
        print('\nTotal Billable Due: $'+ format(completeInvoice,',.2f'))
        print('Total Billable Hours: '+ format(completeTotal,'.2f'))
        print('Average Billable Hours: '+ format(averageHours,'.2f'))
            
        outFile.close()
        
    except FileNotFoundError:
        print("No employees on file")




