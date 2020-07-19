import sys
import csv

class CsvToJsonConvert:
    def __init__(self,path=None, delimiter=None,encoding =None):
        if path is None:
            if len(sys.argv)>1:
                self.path = sys.argv[1]
                self.newFile = sys.argv[2]
            else:
                raise Exception("You miss the filepath or the name of the file \N{grinning face}")
        else:
            self.path = path
            if len(sys.argv) > 2:
                self.newFile = sys.argv[2]
            else:
                self.newFile = "convert.json"
        self.delimiter= ',' if delimiter is None else delimiter
        self.subset = dict()
        self.dataset = list()
        self.set_header()
        self.encoding = encoding if encoding is not None else 'utf-8-sig'

    def set_header(self):
        """

        set the header of the file and create the header according the rule where the first line represent the header and the next lines represent
        data set.
        soon I will create the exceptions where user does not have any header.

        """
        fopen = open (self.path, 'r',encoding='utf-8-sig')
        self.header = csv.reader(fopen.readlines(1)) #return class of reader of object
        fopen.close()


    def get_header(self):
        return self.header

    def extract_headers(self):
        for data in self.get_header():
            return data

    def __create_json_file(self):
        with open(self.newFile,'w') as jt:
            jt.write(str(self.dataset))

    def convert (self):
        #with open(self.path,'r',encoding='utf-8-sig') as sfopen:

        """
        this method convert the data according the data set sended from user and generate the value
        """

        with open(self.path,'r',encoding=self.encoding) as fopen:
            header = self.extract_headers()
            reader = csv.reader(fopen)
            for data in reader:
                for key,rows in enumerate(data):
                    self.subset.update({header[key]: rows})
                self.dataset.append(self.subset)
        self.__create_json_file()

    def get_values_from_args(self):
        return sys.argv

if __name__=='__main__':
    try:
        convertor = CsvToJsonConvert(path=None,delimiter=',')
        convertor.convert()
    except Exception as fnf:
        print(fnf)
