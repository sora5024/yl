class Student:

    school = 'Blue Lock'

    def __init__(self, first_name, last_name, phone):
        self.first_name = first_name
        self.last_name = last_name
        self._phone = phone

    def add_reason_for_absence(self, reason):
        self.reason = reason
        print(f'{self.first_name} {self.last_name} Reason for absence: {self.reason}')
        student_two.add_reason_for_absence('Undefined.')

    def get_phone(self):
        return self._phone
    
    def set_phone(self, phone):
        self._phone = phone

class AdultStudent(Student):
    def __init__(self, first_name, last_name, occupation):
            super().__init__('first_name', 'last_name', 'occupation')
            self.occupation = occupation

student_one = Student('Michael','Kaiser', '5884 6797')
student_two = Student('Alexis','Ness', '7789 9877')
AdultStudent = Student('Ego','Jinpachi', '9999 9999')

print(f'Student 1: {student_one.first_name} {student_one.last_name} - {student_one.school}')
print(f'Student 2: {student_two.first_name} {student_two.last_name} - {student_two.school}')
print(f'Adult student 1: {AdultStudent.first_name} {AdultStudent.last_name}')

print('Student 1 phone number:', student_one.get_phone())
(student_one.set_phone('UNKNOWN CELLAR'))
print('Student 1 phone number:', student_one.get_phone())

if student_one == student_two:
    print('Student 1 is the same as student 2.')
else:
    print('Student 1 is not equivalent to student 2.')

print(f'1. opilane: {student_one.first_name} {student_one.last_name} - {student_one.school}')
print(f'2. opilane: {student_two.first_name} {student_two.last_name} - {student_two.school}')
print(f'3. opilane: {adult_student.first_name} {adult_student.last_name} - {adult_student.school}')
student_two.add_reason_for_absence('Medical reasons')

#print(student_one._phone)

print(student_one.get_phone())
student_one.set_phone('52123456')
print(student_one.get_phone())

print(f'{adult_student.first_name} Telephone is {adult_student.get_phone()}')
adult_student.print_occupation()