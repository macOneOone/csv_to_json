import csv
import sys

class CsvToJsonConvert:

    def __init__(self,path=None, delimiter=None,encoding =None):


        if path is None and len(sys.argv) == 1:
            raise Exception("You miss the filepath \N{grinning face}")

        self.path = sys.argv[1] if path is None else path
        self.delimiter= ',' if delimiter is None else delimiter
        self.subset = dict()
        self.dataset = list()
        self.newFile = 'converted.json' if sys.argv[2] is None else sys.argv[2]
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
    def create_json_file(self):
        with open(self.newFile,'w') as jt:
            jt.write(str(self.dataset))

    def convert (self):
        #with open(self.path,'r',encoding='utf-8-sig') as sfopen:
        """
        this method convert the data according the data set sended from user and generate the value
        """
        with open(self.path,'r',encoding=self.encoding) as fopen:
            next(fopen)
            header = self.extract_headers()
            reader = csv.reader(fopen)
            for data in reader:
                for key,rows in enumerate(data):
                    self.subset.update({header[key]: rows})
                self.dataset.append(self.subset)
        self.create_json_file()

    def get_values_from_args(self):
        return sys.argv

try:
    convertor = CsvToJsonConvert(path=None,delimiter=',')
    convertor.convert()
except Exception as fnf:
    print(fnf)
