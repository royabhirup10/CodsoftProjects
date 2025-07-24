class Calculation:
    def __init__(self, value, history=None):
        self.value = value
        self.history = history or []

    def operate(self, operation, number):
        if operation == '+':
            result = self.value + number
        elif operation == '-':
            result = self.value - number
        elif operation == '*':
            result = self.value * number
        elif operation == '/':
            result = self.value / number if number != 0 else 'Error'
        else:
            raise ValueError("Unknown operation")
        new_history = self.history + [(self.value, operation, number, result)]
        return Calculation(result, new_history)