
import csv
from student import Student


class FetchStudentDetails:
    student_list = None
    headers = None

    def __init__(self):
        self.headers = []
        self.student_list = []

    @staticmethod
    def clean_input(row):
        """
        Clean and sanitize the input so that it does not contain leading and trailing spaces
        """
        return [r.strip() for r in row]

    @staticmethod
    def map_csv_to_class(row):
        """
        Convert the input row into a Student class
        """
        return Student(*row)
    
    @staticmethod
    def convert_to_int(row):
        """
        Convert the input to integer
        """
        return [row[0], int(row[1]), int(row[2]), row[3], row[4], float(row[5])]


    def get_data(self, file_name="./student_details.csv"):
        """
        Fetch the data from the given csv file and construct the list of Student objects
        """
        with open(file_name, newline="") as _file:
            reader = csv.reader(
                _file,
                delimiter=",",
                quotechar='"',
                quoting=csv.QUOTE_ALL,
                skipinitialspace=True,
            )
            self.headers = next(reader)

            # set here self.headers (first row)
            self.student_list = [self.map_csv_to_class(self.convert_to_int(self.clean_input(row))) for row in reader]
            _file.close()
            # set here self.student_list consider using clean_input() and map_csv_to_class()
        return self.student_list

    def get_super_student(self):
            """
            Get super student
            """
            self.super_student = "yohan doe"
            return self.super_student

fetch_student = FetchStudentDetails()
fetch_student.get_data()
super_student = fetch_student.get_super_student()

print(super_student)