class Member:
    def __init__(self, name='', age='', gender='', contact_no='', email='', bmi='', duration=''):
            self.name = name
            self.age = age
            self.gender = gender
            self.contact_no = contact_no
            self.email = email
            self.bmi = bmi
            self.duration = duration

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age

    def setGender(self, gender):
        self.gender = gender

    def getGender(self):
        return self.gender

    def setContact(self, contact_no):
        self.contact_no = contact_no

    def getContact(self):
        return self.contact_no

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email

    def setBMI(self, bmi):
        self.bmi = bmi

    def getBMI(self):
        return self.bmi

    def setDuration(self, duration):
        self.duration = duration

    def getDuration(self):
        return self.duration



obj= Member('name', 'age', 'gender', 'contact_no', 'email', 'bmi', 'duration')
















