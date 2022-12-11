from math import floor

class Monkey:
    monkeys = dict()
    mod = 1

    def __init__(self, name, items, operation, test):
        self.monkeys[name] = self
        self.name = name
        self.operation = operation
        self.test = test
        self.items = list()
        self.inspections = 0
        Monkey.mod *= self.test[0]
        for item in items:
            self.items.append(item)


    # def __repr__(self):
    #     return self.name


    @classmethod
    def rank_by_inspections(cls):
        return list(sorted(cls.monkeys.values(), key=lambda item: -item.inspections))


    @classmethod
    def get_monkey_business(cls):
        monkeys = cls.rank_by_inspections()
        print(monkeys[0].name, monkeys[0].inspections)
        print(monkeys[1].name, monkeys[1].inspections)
        return monkeys[0].inspections * monkeys[1].inspections


    def be_bored(self, item):
        pass # Part 2
        # item.worry = floor(item.worry / 3) # Part 1
        #print(f"{self} gets bored with item. Worry level changes to {item.worry}.")


    def do_round(self):
        items = [item for item in self.items]
        for item in items:
            self.inspections += 1
            self.perform_operation(item)
            self.be_bored(item)
            self.perform_test(item)


    def give(self, monkey, item):
        monkey.receive(item)
        self.items.pop(self.items.index(item))


    def receive(self, item):
        self.items.append(item)


    def perform_operation(self, item):
        old = item.worry
        item.worry = eval(self.operation) % self.mod
        #print(f"Worry level changes from {old} to {item.worry}.")


    def perform_test(self, item):
        if not item.worry % self.test[0]:
            self.give(self.monkeys[self.test[1]], item)
            #print(f"Test succeeds, item goes to {self.test[1]}.")
        else:
            self.give(self.monkeys[self.test[2]], item)
            #print(f"Test fails, item goes to {self.test[2]}.")