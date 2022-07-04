class data:
    def __init__(self,file_name,file_type,date,size):
        self.file_name=file_name
        self.file_type=file_type
        self.date=date
        self.size=size


    def file_open(self):
        file = open(self.file_name, 'w')
        file.write('this is the first line')
        file.write('\n')
        file.write('this is the second line')
        file.close()

    def file_read(self):
        file = open(self.file_name, 'r')
        print(file.read())

    def file_append(self):
        file = open(self.file_name, 'a')
        file.write('\n')
        file.write('this is appended text')
        file.close()

  


data_file = data('data.txt','txt',10/10/2020,10)
#data_file.file_open()
#data_file.file_read()
data_file.file_append()
data_file.file_read()
