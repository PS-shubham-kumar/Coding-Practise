import re
import json
import os
from employee import Employee

DATA_FILE = "employees.json"


def _load_from_file() -> list[Employee]:
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return [Employee(**e) for e in json.load(f)]


def _save_to_file(employees: list[Employee]):
    with open(DATA_FILE, "w") as f:
        json.dump([e.__dict__ for e in employees], f, indent=2)


def _is_valid_email(email: str) -> bool:
    return bool(re.match(r"^[\w.-]+@[\w.-]+\.\w{2,}$", email))


def _validate(emp: Employee) -> str | None:
    if not emp.employee_id.strip():
        return "Employee ID cannot be empty."
    if not emp.name.strip():
        return "Name cannot be empty."
    if not _is_valid_email(emp.email):
        return "Invalid email address."
    return None


def add_employee(employees: list[Employee], emp: Employee) -> str:
    error = _validate(emp)
    if error:
        return error
    if any(e.employee_id == emp.employee_id for e in employees):
        return f"Employee ID '{emp.employee_id}' already exists."
    employees.append(emp)
    _save_to_file(employees)
    return "Employee added successfully."


def get_all_employees(employees: list[Employee], sort_by_name=False) -> list[Employee]:
    return sorted(employees, key=lambda e: e.name.lower()) if sort_by_name else employees


def search_by_id(employees: list[Employee], employee_id: str) -> Employee | None:
    return next((e for e in employees if e.employee_id == employee_id), None)


def update_employee(employees: list[Employee], employee_id: str, updated: Employee) -> str:
    error = _validate(updated)
    if error:
        return error
    for i, e in enumerate(employees):
        if e.employee_id == employee_id:
            employees[i] = updated
            _save_to_file(employees)
            return "Employee updated successfully."
    return "Employee not found."


def delete_employee(employees: list[Employee], employee_id: str) -> str:
    for i, e in enumerate(employees):
        if e.employee_id == employee_id:
            employees.pop(i)
            _save_to_file(employees)
            return "Employee deleted successfully."
    return "Employee not found."


def filter_by_department(employees: list[Employee], department: str) -> list[Employee]:
    return [e for e in employees if e.department.lower() == department.lower()]
