# Imagine we have a washing machine which can wash the clothes, rinse the clothes and
# spin the clothes but all the tasks separately.
# We need a system that can automate the whole task without the disturbance or interference of us.
#
# To solve the above-described problem, we would like to hire the Facade Method.
# It will help us to hide or abstract the complexities of the subsystems as follows.
#
# Note: the methods wash(), rinse() and spin() provide the output of the appropriate operation.


class WashingMachine:

    def __init__(self):
        self._subsystem1 = Subsystem1()
        self._subsystem2 = Subsystem2()
        self._subsystem3 = Subsystem3()
        self.startWashing()

    def startWashing(self):
        results = []
        results.append(self._subsystem1.wash())
        results.append(self._subsystem2.rinse())
        results.append(self._subsystem3.spin())
        print("\n".join(results))


class Subsystem1:
    def wash(self):
        return "Washing..."


class Subsystem2:
    def rinse(self):
        return "Rinsing..."


class Subsystem3:
    def spin(self):
        return "Spinning..."


washingMachine = WashingMachine()
washingMachine.startWashing()
