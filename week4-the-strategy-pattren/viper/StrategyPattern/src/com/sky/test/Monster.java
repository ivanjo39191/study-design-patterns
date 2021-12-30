package com.sky.test;

public class Monster {
    private String name;
    private AttackStrategy attackStrategy;

    public Monster(String name, AttackStrategy attackStrategy) {
        this.name = name;
        this.attackStrategy = attackStrategy;
    }

    public void strategy() {
        this.attackStrategy.attack(this.name);
    }
}

