package com.sky.week2;

import java.time.LocalDate;

public interface Builder {
    Builder setSdate(LocalDate sdate);

    Builder setEdate(LocalDate edate);

    Builder setOrigin(String origin);

    Builder setDestination(String destination);

    Builder setTransportation(String transportation);

    Schedule build();
}
