# Employee Management Console Application

## How to Run

```bash
python main.py
```

> Requires Python 3.10+

## Features Implemented

- Add employee with validation (ID, name, email)
- View all employees (sorted by name)
- Search employee by ID
- Update employee details
- Delete employee
- Filter employees by department
- Prevent duplicate employee IDs
- Persist data to `employees.json`

## Project Structure

```
├── employee.py          # Employee data model
├── employee_service.py  # Business logic & validation
├── main.py              # Console UI / entry point
├── employees.json       # Auto-generated data file
└── README.md
```

## Best Practices Followed

- Meaningful names for variables, functions, and classes
- Single-responsibility methods
- Input validation (empty ID/name, email format)
- No duplicate code — shared `prompt_employee_details` and `display_employee`
- Data persistence via JSON file
- Graceful error messages instead of crashes
- Logic separated across model, service, and UI layers
