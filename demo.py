class Fan:
    def __init__(self):
         self.brand = "Bajaj"
         self.color = "White"
         self.cost = "3k"
    def on(self):
         print("Fan is on")
    def rotate(self):
         print("Fan is rotating")
f1 = Fan()
print(f1.brand)
print(f1.color)
print(f1.cost)
f1.on()
f1.rotate()