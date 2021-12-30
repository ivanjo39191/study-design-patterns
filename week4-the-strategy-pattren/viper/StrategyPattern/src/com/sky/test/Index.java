package com.sky.test;

public class Index {
    public static void main(String[] args) {
        Monster monster1 = new Monster("史萊姆",new Slime());
        Monster monster2 = new Monster("史萊姆王",new SlimeKing());
        Monster monster3 = new Monster("殭屍史萊姆",new ZombieSlime());

        monster1.strategy();
        monster2.strategy();
        monster3.strategy();
    }
}
