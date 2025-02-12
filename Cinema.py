class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
            self.hall_list.append(hall)
     
class Hall(Star_Cinema):
    def __init__(self, row, col, hall_no):
             self._seats = {}
             self._show_list = []
             self.row = row
             self.col = col
             self.__hall_no = hall_no
             self.entry_hall(self)

    def entry_show (self, id, movie_name, time):
             self._show_list.append((id, movie_name, time))
             self._seats[id] = [[0 for _ in range(self.col)] for _ in range(self.row)]

    def book_seats (self, movie_id, seatDtls):
            if movie_id in self._seats:
                 row, col = seatDtls
                 if 0 <= row <= self.row and 0<= col <= self.col:
                      if self._seats[movie_id][row][col]== 0:
                             self._seats[movie_id][row][col]== 1
                             print(f"You've Successfully booked the seats [{row}][{col}]")
                      else:
                             print(f"Sorry! Seats are already booked")
                 else:
                        print(f"[{row}][{col}] are Invalid")
            else:
                   print(f"{movie_id} does not Exists!")

    def view_show_list(self):
        for show in self._show_list:
            (movieID, movieName, streamimgTime) = show 
            print(f"\n\tThe Movie : {movieName}\n\tShedule Time : {streamimgTime}\n\tMovie ID: {movieID}") 

    def view_available_seats(self, id):
        if id in self._seats:
              for row in range(self.row):
                    for col in range(self.col):
                          if self._seats[id][row][col] == 0:
                                print(f"Available Seats are [{row}][{col}]")
                          else:
                                print(f"Sorry ID:{id} is NOT FOUND!")   

new_hall = Hall(5, 6, 1)
new_hall = Hall(4, 6, 2)                                                                                
new_hall = Hall(6, 5, 3)   
new_hall = Hall(5, 5, 4)   
new_hall.entry_show(11, "'Inside Out'", "Friday 10:00 AM") 
new_hall.entry_show(12, "'Be With You'", "Saturday 6:00 PM")   
new_hall.entry_show(13, "'My Neighbor Totoro'", "Sunday 4:00 PM")    
new_hall.entry_show(14, "'20th Century Girl'", "Monday 12:00 AM") 
print(f"\tOption 1: VIEW SHOW LIST\n\tOption 2: AVAILABLE SEATS\n\tOption 3: BOOK A SEAT\n\tOption 4: EXIT")
print(f"Please Select an Option: ")  

while True:
      option = int(input())

      if option == 1:
            new_hall.view_show_list() 
            print(f"\nSelect another Option: ")  

      elif option == 2:
            print(f"\nPlease Select Movie Id For Available Seats") 
            movieID = int(input())
            new_hall.view_available_seats(movieID)  
            

      elif option == 3:
            print("Please Select 1. Movie ID 2. Row Seat 3. Column Seat")
            id = int(input())
            rowSeat = int(input())
            colSeat = int(input())
            new_hall.book_seats(id, (rowSeat, colSeat))
      elif option == 4:
            print("Thanks For Watching")
            break        