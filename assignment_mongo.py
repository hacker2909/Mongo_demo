import pymongo as mg


class MongoDBAssignment:

    def __init__(self):
        pass

    def DatabaseCreation(self):
        try:
            # Making Connection
            self.client = mg.MongoClient("mongodb://localhost:27017")

            # Creating or accessing existing dataBase
            self.mydb = self.client['University']
            print("MongoDB : Successfully Connected")

            self.CollectionCreation()

        except:
            print("MongoDB : Connection Failed")

    def CollectionCreation(self):
        try:
            # Creating or accessing existing collections
            self.students_info = self.mydb.students_information
            self.courses_info = self.mydb.courses_information
            print("MongoDB : Collections Successfully Created")
            self.DocumentInsertion()
        except:
            print("MongoDB : Collection Creation Failed")

    def DocumentInsertion(self):
        try:
            # inserting Multiple record in students collection
            self.students_info.insert_many([
                {"name": "Alice", "age": 20, "major": "Computer Science", "GPA": 3.8},
                {"name": "Bob", "age": 22, "major": "Engineering", "GPA": 3.5},
                {"name": "Charlie", "age": 21, "major": "Mathematics", "GPA": 3.9},
                {"name": "David", "age": 23, "major": "Physics", "GPA": 3.8},
                {"name": "Eve", "age": 19, "major": "Biology", "GPA": 4.0}
            ])
            # inserting Multiple record in courses collection
            self.courses_info.insert_many([
                {"name": "Python Programming", "instructor": "Dr. Smith", "credits": 4,
                 "schedule": "Mon/Wed/Fri 10:00AM"},
                {"name": "Database Management", "instructor": "Mr. Johson", "credits": 3,
                 "schedule": "Tue/Thu 1:00 PM"},
                {"name": "Linear Algebra", "instructor": "Prof. Brown", "credits": 3, "schedule": "Mon/Wed 2:00 PM"}
            ])
            print("MongoDB : Document Insertion Successfully Completed")
            self.QueryingData()
        except:
            print("MongoDB : Document Insertion Failed")

    def QueryingData(self):
        try:
            print("---------------------------")
            # printing all values existing in students collection
            print("Students Collection : ")
            for student in self.students_info.find({}):
                print(student)
            print("---------------------------")
            print("\nCourses by Instructor Dr. Smith : ")
            # printing a specific value existing in courses collection (from Dr. Smith)
            for documents in self.courses_info.find({"instructor": "Dr. Smith"}):
                print(documents)
            print("---------------------------")
            print("\nStudents with GPA greater than 3.5: ")
            # printing students information where GPA grater than 3.5
            for student in self.students_info.find({"GPA": {"$gt": 3.5}}):
                print(student)
            print("---------------------------")
            print("\nCourses with Credits less than or equal to 3: ")
            # printing courses with Credits less than or equal to 3
            for courses in self.courses_info.find({"credits": {"$lte": 3}}):
                print(courses)
            print("---------------------------")
            self.UpdatingData()

        except:
            print("MongoDB : Querying Data Failed")

    def UpdatingData(self):
        try:
            # Update the GPA for Alice to 4.0
            self.students_info.update_one({"name": "Alice"}, {"$set": {"GPA": 4.0}})

            # Add graduation_year as a new field in the students' collection.
            # Set new field values as '2024' for all the records
            self.students_info.update_many({}, {"$set": {"graduation_year": "2024"}})
            print("MongoDB : Update Data Successfully Completed")
            print("------ Student Collection After Update -----")
            for student in self.students_info.find({}):
                print(student)
        except:
            print("MongoDB : Update Data Failed")


mongo_assignment = MongoDBAssignment()
mongo_assignment.DatabaseCreation()