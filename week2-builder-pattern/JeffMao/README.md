# 例子：辦旅遊

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

