package com.sky.test;

public class DrinkFactory {
    public static Drinks produce(String type) {
        switch (type) {
            case "cola":
                return new Cola();
            case "tea":
                return new Tea();
            case "juice":
                return new Juice();
        }
        return null;
    }
}
