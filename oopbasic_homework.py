# oopbasic_homework.py

class HotelRoom:
    def __init__(self,number,room_type,bed,floor):
        self.number = number
        self.room_type = room_type
        self.bed = bed
        self.floor = floor
    
    def preference(self):
        if self.floor <= 4:
            req_floor = 'Low floor'           
        else:
            req_floor = 'Hign floor'
        print(f'This room is a {req_floor}')

    def book(self):
        print('Book this room!!')

class HotelSuiteRoom(HotelRoom):
    def __init__(self,number,bed,floor,room_type,suite):
        super().__init__(number,bed,floor,room_type)
        self.suite = suite

    def suite_type(self):
        if self.suite_type != None:
            print('There is a living room included!!')
        else:
            print('This is not a suite room!!')

my_book = HotelRoom('4401','DLX','Double',4) 
my_suite_book = HotelSuiteRoom('3401','SUT','Double',3,'2 Bedroom Suite')

print('-----Booking informaiton-----')
print(f'Your booking room is :{my_book.number}, Type :{my_book.room_type}, bed :{my_book.bed}, floor :{my_book.floor}')
my_book.preference()

print('-----Booking informaiton-----')
print(f'Your booking room is :{my_suite_book.number}, Type :{my_suite_book.room_type}, Suite : {my_suite_book.suite}')
my_suite_book.suite_type()
