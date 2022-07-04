


class student:
    def __init__(self, name, rollno,joining_year,branch,current_topic):
        self.name=name
        self.rollno=rollno
        self.joining_year=joining_year
        self.branch=branch
        self.current_topic=current_topic

    def name_parsing(self):
        if type(self.name)==list:
            for i in self.name:
                print(i)
        else:
            print(self.name)
            
           

    def crt_topic(self):
        print('current topic is {}'.format(self.current_topic))

    def str_rollno(self):
        if type(self.rollno)==str:
            print('do you want to change your rollno to int? y/n')
            choice=input()
            if choice=='y':
                self.rollno = int(input('enter your new rollno:'))
                self.rollno=int(self.rollno)
                print('your rollno is now {}'.format(self.rollno))
            else:
                print('your rollno is {}'.format(self.rollno))
        else:
            print('your rollno is {}'.format(self.rollno))

    def __str__(self):
        return " student details: {} {} {} {} {}".format(self.name,self.rollno,self.joining_year,self.branch,self.current_topic)


#srini = student('srini', '1', '2020', 'cse', 'python')

#srini.str_rollno()

#print(srini)

strudents = student(['srini','sandeep','sachin'],['1','2','3'],['2020','2021','2022'],['cse','ece','mech'],['python','java','c++'])  

strudents.name_parsing()

sandeep = student('sandeep', '2', '2021', 'ece', 'java')
sandeep.name_parsing()