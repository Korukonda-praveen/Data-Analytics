# Task 2 real time scenario for Multiple Inheritance
# Multiple Inheritance:one derived class with more than one base classes

class Engine:
    "base class 1"
    def start_engine(self):
        print("Engine Started")

class Musicsystem:
    "base class 2"
    def play_music(self):
        print("Music system is playing")

class Gps:
    "base class 3"
    def gps(self):
        print("GPS is active")

class Safety:
    "base  class 4"
    def airbags(self):
        print("Airbags are ready")

class Car(Engine,Musicsystem,Gps,Safety):
    "Derived class"
    def drive(self):
        print('Car is driving')

BMW=Car()
BMW.start_engine()
BMW.play_music()
BMW.gps()
BMW.airbags()
BMW.drive()