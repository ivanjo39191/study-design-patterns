# 例子：辦旅遊
# Product
class Trip:    
    def __init__(self):
        self.price = None
        self.duration = None
        self.destination = None

    def __str__(self):
        return f"旅遊地點{self.destination} 期間{self.duration} 價格{self.price}"


# Abstract Builder
class TripBuilder:
    def __init__(self):
        self.trip = None
    
    def new_trip(self):
        self.trip = Trip()


# Concrete Builder 1 
class SpringTripBuilder(TripBuilder):
    def build_duration(self):
        self.trip.duration = '春天'

    def build_price(self, price):
        self.trip.price = price

    def build_destination(self, destination):
        self.trip.destination = destination


# Concrete Builder 2
class SummerTripBuilder(TripBuilder):
    def build_duration(self):
        self.trip.duration = '夏天'

    def build_price(self, price):
        self.trip.price = price

    def build_destination(self, destination):
        self.trip.destination = destination


# Director
class Director(object):
    def __init__(self):
        self.trip_builder = None

    def construct_trip(self, price=None, destination=None):
        self.trip_builder.new_trip()
        self.trip_builder.build_duration()
        self.trip_builder.build_price(price)
        self.trip_builder.build_destination(destination)

    def get_trip(self):
        return self.trip_builder.trip


if __name__ == "__main__":
    director = Director()
    # 建造春天之旅
    director.trip_builder = SpringTripBuilder()
    director.construct_trip(destination="新竹", price="一萬元")
    print(director.get_trip())
    # 建造夏天之旅
    director.trip_builder = SummerTripBuilder()
    director.construct_trip(destination="台南", price="五千元")
    print(director.get_trip())

    # 結果：
    # 旅遊地點新竹 期間春天 價格一萬元
    # 旅遊地點台南 期間夏天 價格五千元

# ==================================
# 例子：蓋房子
# Product
class Building(object):
    def __init__(self):
        self.floor = None
        self.size = None

    def __repr__(self):
        return 'Floor: %s | Size: %s' % (self.floor, self.size)


# Abstract Builder
class Builder(object):
    def __init__(self):
        self.building = None

    def new_building(self):
        self.building = Building()


# Concrete Builder
class BuilderHouse(Builder):
    def build_floor(self):
        self.building.floor = 'One'

    def build_size(self):
        self.building.size = 'Big'


# Director
class Director(object):
    def __init__(self):
        self.builder = None

    def construct_building(self):
        self.builder.new_building()
        self.builder.build_floor()
        self.builder.build_size()

    def get_building(self):
        return self.builder.building