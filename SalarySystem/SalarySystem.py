"""
SalarySystem -工资结算系统

Author: Sizhuo Li
Date: 2023/7/20
"""
from abc import abstractmethod


class Employee(object):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        pass


class Manager(Employee):
    def get_salary(self):
        return 15000


class Programmer(Employee):
    def __init__(self, name):
        super().__init__(name)
        self.working_hour = 0

    def get_salary(self):
        return 200 * self.working_hour


class Salesman(Employee):
    def __init__(self, name):
        super().__init__(name)
        self.sales = 0

    def get_salary(self):
        return 1800 + 0.05 * self.sales


def main():
    employees = [Manager('Tim Cook'), Programmer('Pony Ma'), Programmer('Steve Lebs'), Salesman('Jack Ma'),
                 Salesman('Richard Liu')]

    for emps in employees:
        if type(emps) == Programmer:
            emps.working_hour = int(input(f'请输入{emps.name}的本月工作时长:'))
        elif type(emps) == Salesman:
            emps.sales = float(input(f'请输入{emps.name}的本月销售额:'))
        print(f'员工{emps.name}的本月工资为{emps.get_salary()}')


if __name__ == '__main__':
    main()
