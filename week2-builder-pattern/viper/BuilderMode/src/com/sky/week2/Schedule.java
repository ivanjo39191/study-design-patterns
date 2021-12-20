package com.sky.week2;

import java.time.LocalDate;

public class Schedule {
    //出發日
    private LocalDate sdate;
    //回程日
    private LocalDate edate;
    //起點
    private String origin;
    //目的地
    private String destination;
    //交通工具
    private String transportation;

    public Schedule(CustomBuilder builder) {
        this.sdate = builder.getSdate();
        this.edate = builder.getEdate();
        this.origin = builder.getOrigin();
        this.destination = builder.getDestination();
        this.transportation = builder.getTransportation();
    }

    public void printSchedule() {
        System.out.println("出發日:" + this.sdate);
        System.out.println("回程日:" + this.edate);
        System.out.println("起點:" + this.origin);
        System.out.println("目的地:" + this.destination);
        System.out.println("交通工具:" + this.transportation);
    }
}
