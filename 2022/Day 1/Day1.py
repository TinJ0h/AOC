
class CalorieCounter:
    def __init__(self) -> None:
        pass

    def Sum(self, numbers):
    
        l = len(numbers)

        if l < 3:
            return numbers[0] + numbers[1]

        return numbers[0] + numbers[1] + numbers[2] 