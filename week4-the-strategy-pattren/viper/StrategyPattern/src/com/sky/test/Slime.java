package com.sky.test;

public class Slime implements AttackStrategy {
    @Override
    public void attack(String name) {
        System.err.println(name+":隨便砍");
    }
}
