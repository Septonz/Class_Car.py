class Car(object):
    """
    blue print for car.
    """
    def __init__(self,model,brand,color,type,speedLimit):
        self.model=model
        self.brand=brand
        self.color=color
        self.type=type
        self.speedLimit=speedLimit

    def start(self):
        print("started")

    def stop(self):
        print("stoped")

    def accelerate(self):
        print("accelerating")
        "accelerater functionality here"

    def change_gear(self, gearType):
        print("gear changed")

Toyota=Car("suzuki","Toyota", "grey", "automatic",250)
print(Toyota.color)