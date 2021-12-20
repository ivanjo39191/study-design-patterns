package com.sky.week2;

import java.time.LocalDate;

public class Index {
    public static void main(String[] args) {
        Schedule schedule = new CustomBuilder()
                .setSdate(LocalDate.now())
                .setEdate(LocalDate.now())
                .setDestination("墾丁")
                .setOrigin("台北")
                .setTransportation("高鐵")
                .build();
        schedule.printSchedule();
    }
}
