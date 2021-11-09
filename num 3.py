class Worker:
    def __init__(self, name, surname, position, profit):
        self.name = name
        self.surname = surname
        self.position = position
        self._profit_wage = profit['wage']
        self._profit_bonus = profit['bonus']


class Position(Worker):

    def full_name(self):
        return (f'{self.name} {self.surname} {self.position}')

    def total_profit(self):
        return self._profit_wage + self._profit_bonus


pos = Position('Александр', 'Зырянов', 'малой', {"wage": 10000, "bonus": 20000})


print(pos.full_name())
print(pos.total_profit())
