import employee_service as svc
from employee_service import Employee

employees = svc.load()

MENU = """
===== Employee Management =====
1. Add Employee
2. View All Employees
3. Search by ID
4. Update Employee
5. Delete Employee
6. Filter by Department
7. Exit
==============================="""


def prompt_employee(employee_id=None) -> Employee:
    eid = employee_id or input("Employee ID: ").strip()
    return Employee(
        employee_id=eid,
        name=input("Name: ").strip(),
        email=input("Email: ").strip(),
        department=input("Department: ").strip(),
        designation=input("Designation: ").strip(),
        joining_date=input("Joining Date (YYYY-MM-DD): ").strip(),
    )


def show(emp: Employee):
    print(f"  ID: {emp.employee_id} | Name: {emp.name} | Email: {emp.email} | "
          f"Dept: {emp.department} | Role: {emp.designation} | Joined: {emp.joining_date}")


def main():
    while True:
        print(MENU)
        choice = input("Choice: ").strip()

        if choice == "1":
            print(svc.add(employees, prompt_employee()))

        elif choice == "2":
            emps = sorted(employees, key=lambda e: e.name.lower())
            if emps:
                [show(e) for e in emps]
            else:
                print("No employees found.")

        elif choice == "3":
            emp = svc.find(employees, input("Employee ID: ").strip())
            show(emp) if emp else print("Not found.")

        elif choice == "4":
            eid = input("Employee ID to update: ").strip()
            if svc.find(employees, eid):
                print(svc.update(employees, eid, prompt_employee(employee_id=eid)))
            else:
                print("Not found.")

        elif choice == "5":
            print(svc.delete(employees, input("Employee ID to delete: ").strip()))

        elif choice == "6":
            result = svc.filter_dept(employees, input("Department: ").strip())
            if result:
                [show(e) for e in result]
            else:
                print("No employees in that department.")

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
