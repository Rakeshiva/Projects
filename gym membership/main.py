from Member import Member


class Manager:
    regimen = dict()
    members = dict()

    @classmethod
    def add_member(cls, member):
        Manager.members[member.getContact()] = member


obj = Manager()


class Superuser:
    def __init__(self):
        while True:
            print("=" * 60)
            print("1.Create Member",
                  "\n2.View Member",
                  "\n3.Delete Member",
                  "\n4.Update Member",
                  "\n5.Create Regimen",
                  "\n6.View Regimen",
                  "\n7.Delete Regimen",
                  "\n8.Update Regimen",
                  "\n0.Exit")
            print("=" * 60)
            ur_choice = input()
            if ur_choice == '1':
                self.create_member()
            elif ur_choice == '2':
                self.view_member()
            elif ur_choice == '3':
                self.delete_member()
            elif ur_choice == '4':
                self.update_member()
            elif ur_choice == '5':
                self.create_regimen()
            elif ur_choice == '6':
                self.view_regimen()
            elif ur_choice == '7':
                self.delete_regimen()
            elif ur_choice == '8':
                self.update_regimen()
            elif ur_choice == '0':
                break
            else:
                print("enter correct value")

    def create_member(self):
        print("=====Enter details of Member=====")
        name = str(input("Name:"))
        age = str(input("Age:"))
        while age.isdigit() == False or len(age) > 2:
            print('give valid input')
            print()
            age = str(input('Enter Age:'))
            continue
        print("=====**Note:Enter 'M/m' for 'Male'or 'F/f' for 'Female' or 'O/o' for 'Other'=========")
        print()
        Gender = input("Select ur Gender:")
        while Gender not in ('mMfFoO'):
            print("give valid input as per Note")
            print()
            Gender = input("Enter ur Gender:")
            continue
        if (Gender.upper() == "M"):
            gender = "Male"
        if (Gender.upper() == "F"):
            gender = "Female"
        if (Gender.upper() == "O"):
            gender = "Other"
        contact_no = str(input("Phone No.:"))
        email = str(input("email:"))
        BMI = input("BMI:")
        while BMI.isdigit() == False:
            print('Enter Correct BMI value:')
            print()
            BMI = input("BMI:")
            continue
        while int(BMI) not in range(9, 66):
            print("===============BMI ranges from 9-66======================================")
            print("============Please Enter the Correct value as per Note:=================")
            BMI = input('Enter Correct BMI value:')
            continue
        bmi = int(BMI)
        if bmi < 18.5:
            R = {'Mon': 'Chest', 'Tue': 'Biceps', 'Wed': 'Rest', 'Thu': 'Back', 'Fri': 'Triceps', 'Sat': 'Rest',
                 'Sun': 'Rest'}
        elif bmi < 25:
            R = {'Mon': 'Chest', 'Tue': 'Biceps', 'Wed': 'Cardio/Abs', 'Thu': 'Back', 'Fri': 'Triceps',
                 'Sat': 'Legs', 'Sun': 'Rest'}
        elif bmi < 30:
            R = {'Mon': 'Chest', 'Tue': 'Biceps', 'Wed': 'Abs/Cardio', 'Thu': 'Back', 'Fri': 'Triceps',
                 'Sat': 'Legs', 'Sun': 'Cardio'}
        elif bmi > 30:
            R = {'Mon': 'Chest', 'Tue': 'Biceps', 'Wed': 'Cardio', 'Thu': 'Back', 'Fri': 'Triceps', 'Sat': 'Cardio',
                 'Sun': 'Cardio'}
        Manager.regimen[contact_no] = R
        duration = int(input("Enter Membership duration in months(1,3,6,12): "))
        while duration not in (1, 3, 6, 12):
            print("============Please Enter the Correct value as per Note:=================")
            print()
            duration = int(input("Enter Membership duration in months(1,3,6,12): "))
            continue
        member = Member(name, age, gender, contact_no, email, bmi, duration)
        Manager.add_member(member)

    def view_member(self):
        id = input("Enter Phone number of member: ")
        if id in Manager.members:
            member = Manager.members[id]
            print("=" * 60)
            print("Name:","     ",member.getName())
            print("Age:","      ",member.getAge(),"years")
            print("Gender:","   ",member.getGender())
            print("Mobile No:","",member.getContact())
            print("Email:","    ",member.getEmail())
            print("bmi:","      ",member.getBMI())
            print("duration:"," ",member.getDuration(),"months")
        else:
            print("===enter valid phone number===")

    def delete_member(self):
        id = input("Enter Phone number of member: ")
        if id in Manager.members:
            del Manager.members[id]
            print("=" * 60)
            print("=====Member Deleted========")
        else:
            print("===enter valid phone number===")

    def update_member(self):
        print("Select from the following",
              "\n1.Extend",
              "\n2.Revoke")
        choose = int(input())
        if choose == 1:
            id = input("Enter Phone number of member to extend membership: ")
            if id in Manager.members:
                member = Manager.members[id]
                d = member.getDuration()
                dur = input("Enter Membership duration in months(1,3,6,12): ")
                while dur.isdigit() == False:
                    print('Enter Correct BMI value:')
                    print()
                    dur = input("Enter Membership duration in months(1,3,6,12): ")
                    continue
                while int(dur) not in (1, 3, 6, 12):
                    print("============Please Enter the Correct value as per Note:=================")
                    print()
                    dur = int(input("Enter Membership duration in months(1,3,6,12): "))
                    continue
                s = int(d) + int(dur)
                member.setDuration(str(s))
                print("Extended Sucessfully")
            else:
                print("Member donot exist", "Knidly check the number")

        elif choose == 2:
            id = input("Enter Phone number of member to revoke the membership: ")
            if id in Manager.members:
                member = Manager.members[id]
                member.setDuration("0")
                print("Membership Revoked")
            else:
                print("Member donot exist", "Knidly check the number")

    def create_regimen(self):
        regimenn = {'Mon': " ", 'Tue': " ", 'Wed': " ", 'Thu': " ", 'Fri': " ", 'Sat': " ", 'Sun': " "}
        i = input("To create Regimen enter the phone number of member: ")
        if i in Manager.members:
            if i not in Manager.regimen:
                Manager.regimen[i] = regimenn
                for j in Manager.regimen[i]:
                    print("Enter workout for {}(day)!".format(j))
                    Manager.regimen[i][j] = input()
            else:
                print("===Regimen exist for this number,delete the existing regimen to proceed for new regimen creation====")
        else:
            print("===enter valid phone number===")

    def view_regimen(self):
        i = input("To view Regimen enter the phone number of member: ")
        if i in Manager.regimen:
            print("=" * 60)
            for key, values in Manager.regimen[i].items():
                print(key, ":", values)

        else:
            print("=======enter valid phone number========")

    def delete_regimen(self):
        id = input("Enter Phone number of member: ")
        if id in Manager.regimen:
            del Manager.regimen[id]
            print("=" * 60)
            print("======Regimen Deleted======")
        else:
            print("===enter valid phone number===")

    def update_regimen(self):
        i = input("Enter the phone number of member you want to update regimen of: ")
        if i in Manager.regimen:
            print("Enter the day which u want to update mon,tue,wed,thu,fri,sat,sun :  ")
            DAY=input()
            day = DAY.capitalize()
            for j in Manager.regimen[i]:
                if j == day:
                    Manager.regimen[i][j] = input("Enter the workout: ")
                    print("Updated Sucessfully")
        else:
            print("===enter valid phone number===")


class memberr:
    def __init__(self):
        while True:
            print("\n*******Member Portal*********\n")
            print("\n1.My Regimen")
            print("\n2.My Profile")
            print("\n0.Exit")
            print("\nEnter your choice:")
            choice = input()
            if choice == '1':
                id = input("To view Regimen enter ur phone member: ")
                if id in Manager.regimen:
                    print()
                    print("====Regimen based on your BMI=====")
                    print("="*45)
                    for key, values in Manager.regimen[id].items():
                        print(key, ":", values)
                else:
                    print("Valid Phone number")
                print("\n")


            elif choice =='2':
                id = input("To view Profile enter ur phone member: ")
                if id in Manager.members:
                    member = Manager.members[id]
                    print("=" * 60)
                    print("Name:","     ",member.getName())
                    print("Age:","      ",member.getAge(),"years")
                    print("Gender:", "  ",member.getGender())
                    print("Mobile No:","",member.getContact())
                    print("Email:","    ",member.getEmail())
                    print("bmi:","      ",member.getBMI())
                    print("duration:"," ",member.getDuration(),"months")
                else:
                    print("Valid Phone number")

            elif choice =='0':
                break

            else:
                print("======Enter valid number========")


def mainn():
    while True:
        print("=" * 60)
        print("             WELCOME TO GYM CENTER           ")
        print("*"*60)
        print("       Fall in love with taking care of your Body         ")
        print("*" * 60)
        print("Select from the following options:""\n1.SuperUser", "\n2.Member", "\n0.Exit")
        choice = input()
        if choice == '0':
            break
        if choice == '1':
            obj = Superuser()
        elif choice == '2':
            obj = memberr()
        else:
            print("======Enter valid number===========")


mainn()


