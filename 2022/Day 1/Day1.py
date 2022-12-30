
class CalorieCounter:
   
    data = [] 

    def __init__(self) -> None:
        pass

    def Sum(self, numbers):
    
        sum = 0 

        for x in numbers:
            sum = sum + x

        return sum

    def ReadData(self,filename):

        f = open(filename, "r")
        calories = []

        for x in f:
            if len(x.strip()) != 0:
                calories += [int(x)]
            else: 
                self.data += [self.Sum(calories)]
                calories = []

        self.data += [self.Sum(calories)]
        
    def GetMaxCalories(self):
        self.data.sort(reverse = True)
        return self.data[0]

    def GetTopThreeCalories(self):
       self.data.sort(reverse = True)
       return self.Sum(self.data[:3])
       
      


