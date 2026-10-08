# Multiple Inheritance --> Whatsapp Scenario --> Send messages, Videocall
'''
class Messages:
    "base class-1"
    def send_message(self):
        print('User sending message')
class Voice:
    "base class-2"
    def voice(self):
        print('User making voice calls')
class Users(Messages,Voice):
    'derived class'
    # pass
    def video_call(self):
        print('user making vidoe calls')
u1=Users()
u1.voice()
u1.send_message()
u1.video_call()
'''
# Multilevel Inheritance --> level by level access
'''
class A:
    statement(s)....
    ......
class B:
    statement(s)....
    ......
class C(B):
    statement(s)....
    ......

# Whatsapp --> Users,Business Users,Premium Users

class Users:
    'Base class'
    def send_message(self):
        print('user can send messages')
class Bussiness_users(Users):
    'Business User features'
    def create_catalog(self):
        print('catalogue creation can be done')
class Premium_users(Bussiness_users):
    'premium user features'
    def avatars(self):
        print('user can create Avatars')

u1=Users()
u1.send_message()
print("-"*45)
u2=Bussiness_users()
u2.send_message()
u2.create_catalog()
print("-"*45)
u3=Premium_users()
u3.send_message()
u3.create_catalog()
u3.avatars()

# hybrid Inheritance--> IT is a combination of one or more types of Inheritance single with multiple inheritance so on..
class Person:
    def speak(self):
        print("I am a Person")

class Student(Person):
    def study(self):
        print("Studying subjects...")

class Employee(Person):
    def work(self):
        print("Working on tasks...")


class TeachingAssistant(Student, Employee):
    def assist(self):
        print("Assisting in lab...")



ta = TeachingAssistant()
ta.speak()   
ta.study()   
ta.work()    
ta.assist()  

# polymorphism--> poly-->many,morph-->forms
# method overloading,method overriding,operator overloading

# hotstar --> free User, Vip user,Premium user

class Hotstar:
    'method overloading'
    def watch(self):
        print('user has logged in')
    def watch(self,movie):
        self.movie=movie
        print(f'user starte watching {self.movie}')
tony=Hotstar()
tony.watch("Avengers Doom's day")

# In Above case same watch() method is overloaded so to make specific usage of we will make the usage of default arguments 

class Hotstar:
    'method overloading with default arguments'
    def watch(self,movie=None):
        self.movie=movie
        if self.movie==None:
            print('user logged in and in home page')
        else:
            print(f'user watching {self.movie}')
u1=Hotstar()
u1.watch()
u1.watch("Avengers Doom's day")

# method overloading wih variable length arguments

class Hotstar:
    'mol with *args usage'
    def add_to_list(self,*movies):
        print(movies)
        for movie in movies:
            print(f'user is watching {movie}')
u1=Hotstar()
u1.add_to_list("Avengers Doom's day","Avengers age of ultron","Avengers","Avengers End Game")

# method overloading with type of arguments usage

class Hotstar:
    'mol with type of args usage'
    def movieslist(self,content):
        self.content=content
        if isinstance(content,str):
            print(f'user is watching {self.content}')
        elif isinstance(content,list):
            print('movie added to watch list')
            for movie in content:
                print(f'User watches {movie}')
u1=Hotstar()
u1.movieslist('rrr')
fav_movies=['leo','vikram','Avengers']
u1.movieslist(fav_movies)

# In all above cases depending on user scenario we can prefer variable length or type of arguments usage

class Freeuser:
    'free user access'
    def freecontent(self):
        print(f'free user is watching movies with advertisements')
class Vip(Freeuser):
    "vip user access"
    def watch(self):
        print(f'vip user watching movie without advertisements')
class Premium(Vip):
    'Premium user access'
    def watch(self):
        print(f'Premium user watching live content')


# in above case usage of objects will vary,to make user of same method  prefer super()
'''
class Freeuser:
    'free user access'
    def watch(self): # Renamed from freecontent to watch
        print(f'free user is watching movies with advertisements')

class Vip(Freeuser):
    "vip user access"
    def watch(self):
        super().watch()
        print(f'vip user watching movie without advertisements')

class Premium(Vip):
    'Premium user access'
    def watch(self):
        super().watch()
        print(f'Premium user watching live content')

u1 = Premium()
u1.watch()
u2=Vip()
u2.watch()