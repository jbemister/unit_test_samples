from emp_functions import Employee
import pytest

@pytest.mark.parametrize('emp, output',[(Employee('Jason', 'Smith', 'Sales', 5), "Smith, Jason"),
                                        (Employee('Jane', 'Doe', 'Marketing', 3), "Doe, Jane"),
                                        (Employee('Alex', 'Hopkins', 'Research', 1), "Hopkins, Alex")])
def test_print_name(emp, output):
    assert emp.print_name() == output

@pytest.mark.parametrize('emp, output', [(Employee('Jason', 'Smith', 'Sales', 5), "Jason Smith has worked here for 5 years!"),
                                        (Employee('Jane', 'Doe', 'Marketing', 3), "Jane Doe has worked here for 3 years!"),
                                        (Employee('Alex', 'Hopkins', 'Research', 1), "Alex Hopkins has worked here for 1 year!")])
def test_length_of_employment(emp, output):
    assert emp.length_of_employment() == output

@pytest.mark.parametrize('emp, output', [(Employee('Jason', 'Smith', 'Sales', 5), "Jason Smith has worked here for 5 years!"),
                                        (Employee('Jane', 'Doe', 'Marketing', 3), "Jane Doe has worked here for 3 years!"),
                                        (Employee('Alex', 'Hopkins', 'Research', 1), "Alex Hopkins has worked here for 1 year!")])
    

# def inst_creation():
#     emp1 = Employee('Jason', 'Smith', 'Sales', 5)
#     emp2 = Employee('Jane', 'Doe', 'Marketing', 3)
#     emp3 = Employee('Alex', 'Hopkins', 'Research', 0)
#     emps = (emp1, emp2, emp3)
#     yield emps
#     # the close function merely prints a closing statement
#     emp1.close()
#     emp2.close()
#     emp3.close()
