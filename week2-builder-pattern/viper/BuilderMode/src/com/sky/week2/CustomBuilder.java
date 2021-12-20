package com.sky.week2;

import java.time.LocalDate;

public class CustomBuilder implements Builder {
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


    @Override
    public Builder setSdate(LocalDate sdate) {
        this.sdate = sdate;
        return this;
    }

    @Override
    public Builder setEdate(LocalDate edate) {
        this.edate = edate;
        return this;
    }

    @Override
    public Builder setOrigin(String origin) {
        this.origin = origin;
        return this;
    }

    @Override
    public Builder setDestination(String destination) {
        this.destination = destination;
        return this;
    }

    @Override
    public Builder setTransportation(String transportation) {
        this.transportation = transportation;
        return this;
    }

    public LocalDate getSdate() {
        return sdate;
    }

    public LocalDate getEdate() {
        return edate;
    }

    public String getOrigin() {
        return origin;
    }

    public String getDestination() {
        return destination;
    }

    public String getTransportation() {
        return transportation;
    }

    @Override
    public Schedule build() {
        return new Schedule(this);
    }
}
