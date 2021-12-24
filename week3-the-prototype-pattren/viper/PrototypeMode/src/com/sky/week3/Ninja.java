package com.sky.week3;

public class Ninja implements Cloneable {
    private String skill;
    private String name;

    public Ninja(String skill, String name){
        this.skill = skill;
        this.name = name;
    }

    @Override
    protected Object clone() throws CloneNotSupportedException {
        return super.clone();
    }

    public String getSkill() {
        return skill;
    }

    public void setSkill(String skill) {
        this.skill = skill;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
