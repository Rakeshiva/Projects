class Movie: 
    def __init__(self):
        print('=====================================Welcome to the CinemaWorld=============================================')
        print("**Note:PLease Enter the required values in numbers other than '0' to Continue.")
        print('============================================================================================================')
        print('***Kindly give the inputs which decides the size of hall''\n') 
        self.rows=input('Enter the number of rows:')
        while (self.rows=='0') or self.rows.isdigit()==False:               #this is for making our user to enter valid details
            print("=============Please Enter the Correct value as per Note:=================")
            self.rows=input('Enter the number of rows:')
            continue
        self.seats=input('Enter the number of seats in each row:')
        while (self.seats=='0')  or self.seats.isdigit()==False:
            print("=============Please Enter the Correct value as per Note:=================")
            self.seats=input('Enter the number of seats in each row:')
            continue
        self.rows=int(self.rows)                    #  {   define the 
        self.seats=int(self.seats)                  #   size of the hall}.
        self.row=[]                                 #adding selected rows in this list when we book the ticket.
        self.column=[]                              #adding selected columns in this list when we book the ticket.
        self.Booked = 0                             #no.of tickets booked.
        self.Current_income =0                      #cummulative of current income.
        self.Booked_details = [[None for j in range(self.seats)] for i in range(self.rows)] #store details of user
        
    def Main_menu(self):
        while True:
            print('\n'"======Select from the following options:========="'\n'
                "1)Show the seats"'\n'
                "2)Buy a Ticket"'\n'                                    
                "3)Statistics"'\n'
                "4)Show Booked Ticket User Info"'\n'                              
                "0)Exit"'\n'
                "=======================================================")
            ur_choice=input('Please choose the required options to continue')
            while ur_choice.isdigit()==False:
                ur_choice=input('Please choose the required options to continue')
                continue
            ur_choice=int(ur_choice)
            if ur_choice==0:
                print('==============================="Your have exited" ===========================''\n'
                      "==========================' Have a Great Day '=================================")
                break
            if ur_choice==1:
                x.Show_the_seats()
            elif ur_choice==2:
                x.Buy_a_ticket()
            elif ur_choice==3:
                x.statistics()
            elif ur_choice==4:
                x.User_info()
            else:
                print('Not a valid option try again by entering the correct value')
    def Show_the_seats(self):
        print('\n''Cinema:')
        print('   '+'  '.join(map(str,list(range(1,self.seats+1)))))
        for i in range(0,self.rows):
            print(i+1,end='  ')
            for j in range(self.seats):
                if ((i+1,j+1) in list(zip(self.row,self.column))):
                    print('B',end='  ')
                else:
                    print('S',end='  ')
            print('\n',end='')

    def Buy_a_ticket(self):
        x.Show_the_seats()
        print("=======You can select the Vacant seats",'S:Vacant Seats','B:Reserved Seat==========')
        row = input('Enter the row number u want to choose:''\n')
        while (row=='0') or row.isdigit()==False or int(row) not in range(1, self.rows+1):
            print("=============Please Enter the Correct row value:=================") 
            row = input('Enter the row number u want to choose:''\n')
            continue
        column = input('Enter the column number u want to choose:\n')
        while (column=='0') or column.isdigit()==False or int(column) not in range(1, self.seats+1):
            print("=============Please Enter the Correct column value:=================") 
            column = input('Enter the column number u want to choose:''\n')
            continue 
        row=int(row)
        column=int(column)
        User_detail = {}                                                  #Here we can store the User details
        if (row,column) not in list(zip(self.row,self.column)):               #Check wheter seat is vacant or not
            if self.rows*self.seats <= 60:
                price_of_ticket = 10
            elif row <= int(self.rows//2):
                price_of_ticket = 10
            else:
                price_of_ticket = 8
            print('price_of_ticket: ', '$'+str(price_of_ticket))
            print('=====================================================================================================''\n'
                  'Press Y/y for YES to proceed your booking further or else the input other than Y will discard ur booking''\n'
                 '=======================================================================================================''\n')
            proceed = input('press Y/y')
            if (proceed.upper()=='Y'):
                self.row.append(row)
                self.column.append(column)
                User_detail['Name'] = input('Enter your Name:')
                while User_detail['Name'].isalpha()==False:
                    print("'Enter valid name', only aplhabets are allowed:")
                    User_detail['Name'] = input('Enter your Name: ')  
                    continue
                print("=====**Note:Enter 'M/m' for 'Male'or 'F/f' for 'Female' or 'O/o' for 'Other'=========")
                print()
                Gender = input("Enter ur Gender:")
                while Gender not in ('mMfFoO'):
                    print("give valid input as per Note")
                    Gender = input("Enter ur Gender:")
                    continue
                if(Gender.upper() == "M"):
                    self.gender = "Male"
                if(Gender.upper()=="F"):
                    self.gender ="Female"
                if(Gender.upper()=="O"):
                    self.gender="Other"
                User_detail['Gender'] = self.gender
                User_detail['Age'] = input('Enter your Age in number:')
                while User_detail['Age'].isdigit()==False or len(User_detail['Age'])>2:
                    print('give valid input')
                    User_detail['Age'] = input('Enter your Age in number:')
                    continue
                User_detail['Ticket_price'] = price_of_ticket
                User_detail['Phone_No'] = input('Enter Phone number: ')
                while User_detail['Phone_No'].isdigit()==False or len( User_detail['Phone_No'])!=10:
                        print('Enter valid Phone number')
                        User_detail['Phone_No'] = input('Enter Phone number: ')
                self.Booked += 1
                self.Current_income += price_of_ticket
                self.Booked_details[row-1][column-1] = User_detail
                print('\n''Your ticket has been Booked Successfully' '\n' 
                     " ================================='THANK YOU'======================================================="'\n')
            else:
                print('\n' "*****Your Booking cant be proceeded any more"'******' '\n')
        else:
            print('\n''==========This seat has been already booked please select from the Vacant seats=======================''\n')
    def statistics(self):
        print("==========================================")
        print("           Statistics:")
        print('===========================================')
        print('Number of purchased tickets:',self.Booked)
        self.percentage = (self.Booked/(self.rows*self.seats))*100
        print("Percentage:",str("{:.2f}".format(self.percentage))+'%')
        print('Current income:','$'+str(self.Current_income))
        self.Total_income=0                                               #Overall expected income.
        a=self.rows*self.seats
        [b,c]=[(a-(a//2)),(a//2)]
        if a<= 60:
            self.Total_income=(a*10)
        else:  
            self.Total_income=(c*10+b*8)    
        print('Total income:','$'+str(self.Total_income))
        print('=============================================')
    def User_info(self):
        booked_row = int(input('Enter Row number - \n'))
        booked_column= int(input('Enter Column number - \n'))
        if booked_row in range(1, self.rows+1) and booked_column in range(1, self.seats+1):
            if (booked_row,booked_column) in list(zip(self.row,self.column)):
                User = self.Booked_details[ booked_row  - 1][ booked_column - 1] 
                print("============================================")
                print("         User info:")  
                print('=============================================')
                print('Name:',User['Name'].capitalize())
                print('Gender:',User['Gender'])
                print('Age:',User['Age'])
                print('Ticket Price:','$'+str(User['Ticket_price']))
                print('Phone No:',User['Phone_No'])
                print('===============================================')
            else:
                print()
                print('The seat is not yet Booked','Kindly enter the details of Booked seat')

x=Movie()
x.Main_menu()