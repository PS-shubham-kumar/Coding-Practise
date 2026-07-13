from employee import Employee
import employee_service as service

employees = service._load_from_file()

MENU = """
========= Employee Management =========
1. Add Employee
2. View All Employees
3. Search Employee by ID
4. Update Employee
5. Delete Employee
6. Filter by Department
7. Exit
=======================================
"""


def prompt_employee_details(employee_id=None) -> Employee:
    eid = employee_id or input("Employee ID: ").strip()
    return Employee(
        employee_id=eid,
        name=input("Name: ").strip(),
        email=input("Email: ").strip(),
        department=input("Department: ").strip(),
        designation=input("Designation: ").strip(),
        joining_date=input("Joining Date (YYYY-MM-DD): ").strip(),
    )


def display_employee(emp: Employee):
    print(f"""
  ID         : {emp.employee_id}
  Name       : {emp.name}
  Email      : {emp.email}
  Department : {emp.department}
  Designation: {emp.designation}
  Joined     : {emp.joining_date}""")


def handle_add():
    emp = prompt_employee_details()
    print(service.add_employee(employees, emp))


def handle_view():
    all_emps = service.get_all_employees(employees, sort_by_name=True)
    if not all_emps:
        print("No employees found.")
        return
    for emp in all_emps:
        display_employee(emp)


def handle_search():
    eid = input("Enter Employee ID: ").strip()
    emp = service.search_by_id(employees, eid)
    display_employee(emp) if emp else print("Employee not found.")


def handle_update():
    eid = input("Enter Employee ID to update: ").strip()
    if not service.search_by_id(employees, eid):
        print("Employee not found.")
        return
    print("Enter new details:")
    updated = prompt_employee_details(employee_id=eid)
    print(service.update_employee(employees, eid, updated))


def handle_delete():
    eid = input("Enter Employee ID to delete: ").strip()
    print(service.delete_employee(employees, eid))


def handle_filter():
    dept = input("Enter Department name: ").strip()
    result = service.filter_by_department(employees, dept)
    if not result:
        print("No employees found in this department.")
        return
    for emp in result:
        display_employee(emp)


ACTIONS = {
    "1": handle_add,
    "2": handle_view,
    "3": handle_search,
    "4": handle_update,
    "5": handle_delete,
    "6": handle_filter,
}


def main():
    while True:
        print(MENU)
        choice = input("Enter your choice: ").strip()
        if choice == "7":
            print("Goodbye!")
            break
        action = ACTIONS.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
