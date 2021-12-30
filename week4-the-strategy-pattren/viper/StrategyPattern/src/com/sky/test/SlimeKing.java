package com.sky.test;

public class SlimeKing implements AttackStrategy {
    @Override
    public void attack(String name) {
        System.err.println(name+":認真砍");
    }
}
