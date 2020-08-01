class Number:

    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        return (Number(self.data + other.data) if type(other) == Number else
                Number(self.data + other))

    def __sub__(self, other):
        return (Number(self.data - other.data) if type(other) == Number else
                Number(self.data - other))

    def __mul__(self, other):
        return (Number(self.data * other.data) if type(other) == Number else
                Number(self.data * other))

    def __truediv__(self, other):
        try:
            return (Number(self.data / other.data) if type(other) == Number else
                    Number(self.data / other))
        except ZeroDivisionError:
            return 'ZeroDivisionError'

    def __int__(self):
        return int(self.data)

    def __float__(self):
        return float(self.data)

    def __eq__(self, other):
        return self.data == other.data

    def __str__(self):
        return str(self.data)
