from abc import ABC, abstractmethod
# from torch import torch


"""2. Một Ward (phường) gồm có name (string) và danh sách của mọi người trong Ward.
Một người person có thể là student, doctor, hoặc teacher. Một student gồm có name,
yob (int) (năm sinh), và grade (string). Một teacher gồm có name, yob, và subject
(string). Một doctor gồm có name, yob, và specialist (string). Lưu ý cần sử dụng a
list để chứa danh sách của mọi người trong Ward."""
class Ward():
    listPeople = []
    def __init__(self, name):
        self.name = name
        self.listPeople = []

    def describe(self):
        print(f"Ward name: {self.name}")
        for ele in self.listPeople:
            ele.describe()

    def add_person(self, ele):
        self.listPeople.append(ele)

    def count_doctor(self):
        cnt_dt = 0
        for ele in self.listPeople:
            if "Doctor" in str(type(ele)):
                cnt_dt += 1
        return cnt_dt
    
    def sort_age(self):
        self.listPeople.sort(key = lambda x: x._yob, reverse = True)

    def compute_average(self):
        total = 0
        cnt = 0
        for ele in self.listPeople:
            if "Teacher" in str(type(ele)):
                total += ele._yob
                cnt += 1
        return total / cnt


class Person(ABC):
    def __init__(self, name: str , yob: int):
        self._name = name
        self._yob = yob
    def get_yob(self):
        return self._yob
    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name, yob, grade: str):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        print(f"Student name: {self._name} - Student yob: {self._yob} - Student grade: {self.grade}")


class Teacher(Person):
    def __init__(self, name, yob, subject: str):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        print(f"Teacher name: {self._name} - Teacher yob: {self._yob} - Teacher subject: {self.subject}")

class Doctor(Person):
    def __init__(self, name, yob, specialist: str):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        print(f"Doctor name: {self._name} - Doctor yob: {self._yob} - Doctor specialist: {self.specialist}")


"""3. Thực hiện xây dựng class Stack với các phương thức (method) sau đây"""
class Stack():
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
    
    def is_full(self):
        if len(self.stack) >= self.capacity:
            return True
        else:
            return False
        
    def pop(self):
        result = self.stack[-1]
        self.stack.pop(-1)
        return result

    def push(self, ele):
        self.stack.append(ele)

    def top(self):
        return self.stack[-1]
    

"""4. Thực hiện xây dựng class Queue với các chức năng (method) sau đây"""
class Queue():
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False
    
    def is_full(self):
        if len(self.queue) >= self.capacity:
            return True
        else:
            return False
        
    def dequeue(self):
        result = self.queue[0]
        self.queue.pop(0)
        return result

    def enqueue(self, ele):
        self.queue.append(ele)

    def front(self):
        return self.queue[0]


if __name__ == "__main__":
    # 2.(a)
    student1 = Student(name = "studentA", yob = 2010, grade = "7")
    student1.describe()
    teacher1 = Teacher(name = "teacherA", yob = 1969, subject = "Math")
    teacher1.describe()
    doctor1 = Doctor(name = "doctorA", yob = 1945, specialist = "Endocrinologists")
    doctor1.describe ()

    # 2.(b)
    print()
    teacher2 = Teacher(name = "teacherB", yob = 1995, subject = "History")
    doctor2 = Doctor(name = "doctorB", yob = 1975, specialist = "Cardiologists")
    ward1 = Ward(name = "Ward1")
    ward1.add_person(student1)
    ward1.add_person(teacher1)
    ward1.add_person(teacher2)
    ward1.add_person(doctor1)
    ward1.add_person(doctor2)
    ward1.describe()

    # 2.(c)
    print(f"\nNumber of doctors : {ward1.count_doctor()}")

    # 2.(d)
    print("\nAfter sorting Age of Ward1 people ")
    ward1.sort_age()
    ward1.describe()

    # 2(e)
    print(f"\nAverage year of birth (teachers): {ward1.compute_average()}")

    # 3.
    stack1 = Stack(capacity = 5)
    stack1.push(1)
    stack1.push(2)
    print(stack1.is_full())
    print(stack1.top())
    print(stack1.pop())
    print(stack1.top())
    print(stack1.pop())
    print(stack1.is_empty())

    # 4.
    queue1 = Queue(capacity = 5)
    queue1.enqueue(1)
    queue1.enqueue(2)
    print(queue1.is_full())
    print(queue1.front())
    print(queue1.dequeue())
    print(queue1.front())
    print(queue1.dequeue())
    print(queue1.is_empty())