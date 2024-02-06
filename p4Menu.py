import Program3
import BillingModule
import AdHocReport


def menuProgram():

    LoopControl = True
    while LoopControl == True:
        print('\nMenu:\n')
        print('\t0 - end')
        print('\t1 - Enter billing data')
        print('\t2 - Display adhoc billing report')
        
        try:
            option = int(input('\nOption ==> '))
            
            if option == 0:
                LoopControl = False
                BillingModule.resetBillingFile()
            elif option == 1:
                Program3.main()
            elif option == 2:
                AdHocReport.Report()
            else:
                print('Please enter an available option.\n')

        except ValueError:
            print("Value entered is not an integer.")
            

menuProgram()
