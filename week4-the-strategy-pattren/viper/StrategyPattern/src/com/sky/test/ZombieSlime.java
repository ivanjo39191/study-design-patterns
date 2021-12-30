package com.sky.test;

public class ZombieSlime implements AttackStrategy {
    @Override
    public void attack(String name) {
        System.err.println(name + ":用火燒");
    }
}
