package com.sky.week1;

public class Index {
    public static void main(String[] args) {
        Drinks product = DrinkFactory.produce("cola");
        product.drink();
    }
}
