from random import randint

class Train:
    def __int__(self, trainno):
        self.trainno = trainno

    def book(self,fro,to):
        print(f"Ticket is booked in train no:{self.trainno} from {fro} to {to}")
    def getstatus(self):
        print(f"Train {self.trainno} is running")
    def getfare(self,fro,to):
        print(f"Fare from {fro} to {to} is ₹{randint(222,500)}")


t = Train(8942)

t.book("Rampur","Delhi")
t.getstatus()
t.getfare("Rampur","Delhi")