import re
import json
import os

DATA_FILE = "employees.json"


class Employee:
    def __init__(self, employee_id, name, email, department, designation, joining_date):
        self.employee_id = employee_id
        self.name = name
        self.email = email
        self.department = department
        self.designation = designation
        self.joining_date = joining_date


def load() -> list[Employee]:
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return [Employee(**e) for e in json.load(f)]


def save(employees: list[Employee]):
    with open(DATA_FILE, "w") as f:
        json.dump([e.__dict__ for e in employees], f, indent=2)


def _validate(emp: Employee) -> str | None:
    if not emp.employee_id.strip():
        return "Employee ID cannot be empty."
    if not emp.name.strip():
        return "Name cannot be empty."
    if not re.match(r"^[\w.-]+@[\w.-]+\.\w{2,}$", emp.email):
        return "Invalid email address."
    return None


def add(employees: list[Employee], emp: Employee) -> str:
    error = _validate(emp)
    if error:
        return error
    if any(e.employee_id == emp.employee_id for e in employees):
        return f"Employee ID '{emp.employee_id}' already exists."
    employees.append(emp)
    save(employees)
    return "Employee added successfully."


def find(employees: list[Employee], employee_id: str) -> Employee | None:
    return next((e for e in employees if e.employee_id == employee_id), None)


def update(employees: list[Employee], employee_id: str, updated: Employee) -> str:
    error = _validate(updated)
    if error:
        return error
    for i, e in enumerate(employees):
        if e.employee_id == employee_id:
            employees[i] = updated
            save(employees)
            return "Employee updated successfully."
    return "Employee not found."


def delete(employees: list[Employee], employee_id: str) -> str:
    for i, e in enumerate(employees):
        if e.employee_id == employee_id:
            employees.pop(i)
            save(employees)
            return "Employee deleted successfully."
    return "Employee not found."


def filter_dept(employees: list[Employee], department: str) -> list[Employee]:
    return [e for e in employees if e.department.lower() == department.lower()]
