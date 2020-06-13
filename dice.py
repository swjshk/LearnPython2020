import random

class Die:
    def __init__(self):
        self.__value = self.roll()

    @property
    def value(self):
        return self.__value
                
    @value.setter
    def value(self, value):
        if value <1:
            raise ValueError("Die can't be less than 1.")
        if value > 6:
            raise ValueError("Die can't be greater than 6.")
        else:
            self.__value = value
            
    @property
    def image(self):
        if self.__value == 1:
                   image= " _____ \n" + \
                          "|     |\n" + \
                          "|  o  |\n" + \
                          "|_____|"
                   return image 
        elif self.__value ==2:
                   image= " _____ \n" + \
                          "|o    |\n" + \
                          "|     |\n" + \
                          "|____o|"
                   return image
        elif self.__value ==3:
                   image= " _____ \n" + \
                          "|o    |\n" + \
                          "|  o  |\n" + \
                          "|____o|"
                   return image 

        elif self.__value ==4:
            self.__image= " _____ \n" + \
                          "|o   o|\n" + \
                          "|     |\n" + \
                          "|o___o|"

        elif self.__value ==5:
                   image= " _____ \n" + \
                          "|o   o|\n" + \
                          "|  o  |\n" + \
                          "|o___o|"
                   return image 
                
        elif self.__value ==6:
                   image= " _____ \n" + \
                          "|o   o|\n" + \
                          "|o   o|\n" + \
                          "|o___o|"

                   return image

                
    def roll(self):
        self.__value = random.randrange(1, 7)
        return self.__value
    
                
class Dice:

    def __init__(self):
        self.__list = []
        self.total_value = 0
        self.count = 0

    def addDie(self, die):
        self.__list.append(die)

    @property
    def list(self):
        dice_tuple = tuple(self.__list)
        return dice_tuple
                
    def rollAll(self):
        for die in self.__list:
            die.roll()

    def getTotal(self):
        #total_value =0 
        for die in self.__list:
            self.total_value += die.value
            self.count += 1
        return self.total_value

    def getAvg(self):
        average_value = self.total_value / self.count
        return average_value 
