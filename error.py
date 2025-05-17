from enum import Enum

class Grades(Enum):
    A_PLUS=80
    A = 70
    A_MINUS = 60
    B_PLUS = 55
    
class UserType(Enum):
    REGULAR_USER = ['portal']
    ADMIN_USER = ["portal", 'payment']

marks = 79

if marks>Grades.A_PLUS.value:
    x = Grades.A_PLUS
    print(x)