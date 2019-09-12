#
# this file holds the class and functions that will be testedself.
# created 09/11/2019


class Employee:
    def __init__(self, first, last, department, emp_time):
        self.first = first
        self.last = last
        self.department = department
        self.emp_time = emp_time

    def print_name(self):
        print("%s, %s" % (self.last, self.first))

    def length_of_employment(self):
        if self.emp_time == 1:
            print("%s %s has worked here for %d year!" % (self.first,
                                                          self.last,
                                                          self.emp_time))
        else:
            print("%s %s has worked here for %d years!" % (self.first,
                                                           self.last,
                                                           self.emp_time))

    def yearly_turnover(self):
        self.emp_time += 1

    def close(self):
        pass
