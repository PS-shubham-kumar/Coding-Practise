from dataclasses import dataclass


@dataclass
class Employee:
    employee_id: str
    name: str
    email: str
    department: str
    designation: str
    joining_date: str
