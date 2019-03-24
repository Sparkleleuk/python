employee_ID = ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7']
employee_name = ['Luther', 'Diego', 'Alison', 'Klaus', 'Five', 'Ben', 'Vanya']
position = ['Manager', 'Lead', 'Manager2', 'Junior', 'Advisor', 'Specialist', 'Specialist2']
department = ['Executive_Team', 'Security', 'Marketing', 'Marketing', 'Strategy', 'Planning', 'Research']
salary = [140000, 120000, 100000, 50000, 130000, 110000, 115000]

def build_employees_dict():
    employees = {}
    for i in range(len(employee_ID)):
        employee = {'id':employee_ID[i],
                   'name':employee_name[i],
                   'pos':position[i],
                   'dept':department[i],
                   'salary':salary[i]
                   }
        employees[employee_ID[i]]=employee
   #  print(employees)
    return employees

employees = build_employees_dict()
print(employees)

def getEmpSalary(employees, employee_ID):
    return(employees[employee_ID]['salary'])

getEmpSalary(employees, 'E2')

def getEmpPosition(employees, employee_ID):
    return(employees[employee_ID]['pos'])

getEmpPosition(employees, 'E3')

def getEmpDept(employees, employee_ID):
    return(employees[employee_ID]['dept'])

getEmpDept(employees, 'E6')

def addNewEmployee(employees, employee_ID, employee_name, position, department, salary):
    employee = {'id':employee_ID,
                   'name':employee_name,
                   'pos':position,
                   'dept':department,
                   'salary':salary
                   }
    employees[employee_ID] = employee

addNewEmployee(employees, 'E8', 'Pogo', 'Legal Counsel', 'Legal', 135000)
addNewEmployee(employees, 'E9', 'Grace', 'Manager', 'Human Resources', 100000)
print(employees)

addNewEmployee(employees, 'E10', 'Eudora', 'Investigator', 'Security', 90000)
print(employees)

def removeEmployees(employees, employee_ID):
    employees.pop('E10')

removeEmployees(employees, 'E10')
print(employees)

def updateSalary(employees, employee_ID, salary):
    print('salary = ' + str(salary))
    employee = employees[employee_ID]
    print('employee = ' + str(employee))
    employee['salary'] = salary

updateSalary(employees, 'E2', 130000)
print(employees)

def updatePosition(employees, employee_id, position):
    employees[employee_id]['pos'] = position

updatePosition(employees, 'E4', 'Senior')
print(employees['E4'])

updateSalary(employees, 'E4', 80000)
print(employees['E4'])

def inc_salary_new(employees, employee_ID, salary):
    if employees[employee_ID]['salary'] <= 100000:
        return (employees[employee_ID]['salary']+employees[employee_ID]['salary']*0.2)
        print(employees, employee_ID, salary)
    else:
        return (employees[employee_ID]['salary']+employees[employee_ID]['salary']*0.1)

inc_salary_new(employees, 'E3', 'salary')

addNewEmployee(employees, 'E11', 'Hazel', 'Security Specialist', 'Security', 70000)
print(employees['E11'])

def create_report(employees):
    for employee in employees.values():
        print(employee['name'],employee['pos'],employee['salary'])

create_report(employees)

def find_employee(employees):
    for employee in employees.values():
        print(employee['id'], employee['name'])

find_employee(employees)

addNewEmployee(employees, 'E12', 'Cha-Cha', 'Security Specialist', 'Security', 70000)
print(employees['E12'])

create_report(employees)

def findEmpName(employees, name):
    for employee in employees.values():
        if employee['name'] == name:
            return employee

findEmpName(employees, 'Cha-Cha')

def findEmpPos(employees, position):
    for employee in employees.values():
        if position in employee['pos']:
        #if employee['pos'] == position:
            return employee['name']

findEmpPos(employees, 'Specialist')

def findEmpDept(employees, department):
    for employee in employees.values():
        if employee['dept'] == department:
            print(employee['name'], employee['pos'], employee['salary'])

findEmpDept(employees, 'Marketing')

def findEmpSalary(employees, salary):
    for employee in employees.values():
        if int(employee['salary']) < (int(salary)):
            print(employee['name'], employee['pos'], employee['dept'], employee['salary'])

findEmpSalary(employees, 100000)

def inc_salary_new(employees):
    for employee in employees.values():
        if employee['salary'] < 100000:
            employee['salary'] = (employee['salary'] + employee['salary']*0.2)
        else:
            employee['salary'] = (employee['salary'] + employee['salary']*0.1)

employees = build_employees_dict()
addNewEmployee(employees, 'E8', 'Pogo', 'Legal Counsel', 'Legal', 135000)
addNewEmployee(employees, 'E9', 'Grace', 'Manager', 'Human Resources', 100000)
addNewEmployee(employees, 'E11', 'Hazel', 'Security Specialist', 'Security', 70000)
addNewEmployee(employees, 'E12', 'Cha-Cha', 'Security Specialist', 'Security', 70000)
updatePosition(employees, 'E4', 'Senior')
create_report(employees)
inc_salary_new(employees)
create_report(employees)
