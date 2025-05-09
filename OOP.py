
class person:
    def __init__(self,name,money,mood,healthrate):
        self.name=name
        self.money=money
        self.mood=mood
        self.healthrate=healthrate
    def sleep(self,hours):
        if hours==7:
            self.mood="happy"
        elif hours<7:
            self.mood="tired"
        else:
            self.mood="lazy"
    def eat(self,meals):
        if meals==3:
            self.healthrate=100
        elif meals==2:
            self.healthrate=75
        elif meals==1:
            self.healthrate=50
    def buy(self,items):
        self.money -=items*10
         
class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = min(max(fuelRate, 0), 100)
        self.velocity = min(max(velocity, 0), 200)  

    def run(self, distance, velocity):
        self.velocity = min(max(velocity, 0), 200)
        fuel_needed = (distance // 10) * 10 
        self.fuelRate -= fuel_needed

        if self.fuelRate <= 0:
            self.fuelRate = 0
            remain_distance = distance - (fuel_needed * 0.1)
            self.stop(remain_distance)
        else:
            self.stop(0)

    def stop(self, remain_distance):
        self.velocity = 0
        if remain_distance > 0:
            print(f"Car stopped early. {remain_distance} km left.")
        else:
            print("Arrived at destination.")


class Office:
    employeesNum = 0

    def __init__(self, name):
        self.name = name
        self.employees = []

    def get_all_employees(self):
        return self.employees

    def get_employee(self, empId):
        for emp in self.employees:
            if emp.id == empId:
                return emp
        return None

    def hire(self, employee):
        self.employees.append(employee)
        Office.employeesNum += 1

    def fire(self, empId):
        self.employees = [emp for emp in self.employees if emp.id != empId]
        Office.employeesNum -= 1

    def deduct(self, empId, deduction):
        emp = self.get_employee(empId)
        if emp:
            emp.salary -= deduction

    def reward(self, empId, reward):
        emp = self.get_employee(empId)
        if emp:
            emp.salary += reward

    def check_lateness(self, empId, moveHour):
        emp = self.get_employee(empId)
        if emp:
            is_late = self.calculate_lateness(9, moveHour, emp.distanceToWork, emp.car.velocity)
            if is_late:
                self.deduct(empId, 10)
            else:
                self.reward(empId, 10)

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        time_needed = distance / velocity
        arrival_time = moveHour + time_needed
        return arrival_time > targetHour

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num

class Employee(person):
    def __init__(self, name, money, mood, healthRate, emp_id, car, email, salary, distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.id = emp_id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours > 8:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def drive(self, distance):
        self.car.run(distance, self.car.velocity)

    def refuel(self, gasAmount=100):
        self.car.fuelRate = min(100, self.car.fuelRate + gasAmount)

    def send_mail(self, to, subject, body, receiver_name):
        print(f"Sending mail to {receiver_name} ({to}): {subject}\n{body}")