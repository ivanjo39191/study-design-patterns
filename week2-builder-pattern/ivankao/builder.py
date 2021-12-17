class Trip:

    def __init__(self, builder):
        self.place = builder.place
        self.tourist_guide = builder.tourist_guide
        self.consumption_amount = builder.consumption_amount
        self.stay_time = builder.stay_time

    def __str__(self):
        tourist_guide = '是' if self.tourist_guide else '否'
        return f"地點:{self.place}\n是否需要導遊:{tourist_guide}\n預計消費金額:{self.consumption_amount} 元\n預計停留時間:{self.stay_time} 小時"

    class TripBuilder:
    
        def __init__(self):
            self.place ='None'
            self.tourist_guide =False
            self.consumption_amount = 1000
            self.stay_time = 60

        def add_place(self, name):
            self.place = name
            return self
    
        def add_tourist_guide(self):
            self.tourist_guide = True
            return self
      
        def add_consumption_amount(self, amount):
            self.consumption_amount = amount
            return self

        def add_stay_time(self, time):
            self.stay_time = time
            return self

        def build(self):
            return Trip(self)

      
if __name__ == '__main__':
    trip = Trip.TripBuilder().add_place('阿里山').add_tourist_guide().add_consumption_amount(10000).add_stay_time(8).build()
    print(trip)
    trip = Trip.TripBuilder().add_place('麗寶樂園').add_consumption_amount(3000).add_stay_time(3).build()
    print(trip)