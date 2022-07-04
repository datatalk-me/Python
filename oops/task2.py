import logging

class data:
    def __init__(self,file_name,file_type,date,size):
        self.file_name=file_name
        self.file_type=file_type
        self.date=date
        self.size=size

    logging.basicConfig(filename='logs.log', level=logging.INFO)

    def file_open(self):
        try:
            file = open(self.file_name, 'w')
            logging.info('file opened')
            file.write('this is the first line')
            logging.info('first line written')
            file.write('\n')
            file.write('this is the second line')
            logging.info('second line written')
            file.close()
            logging.info('file closed')
        except Exception as e:
            print(e)
            logging.error(e)


    def file_read(self):
        try:
            file = open(self.file_name, 'r')
            print(file.read())
            logging.info('file read')
        except Exception as e:
            print(e)
            logging.error(e)

    def file_append(self):
        try:
            file = open(self.file_name, 'a')
            file.write('\n')
            file.write('this is appended text')
            logging.info('file appended')
            file.close()

        except Exception as e:
            print(e)
            logging.error(e)

    def logging_error(self):
        logging.basicConfig(filename='logs.log', level=logging.INFO)
        logging.error('error')

data_file = data('datawithlog.txt','txt',10/10/2020,10)
data_file.file_open()
data_file.file_read()
data_file.file_append()

        