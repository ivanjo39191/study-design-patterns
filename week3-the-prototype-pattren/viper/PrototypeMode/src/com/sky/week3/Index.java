package com.sky.week3;

public class Index {
    public static void main(String[] args) throws CloneNotSupportedException {
        Ninja ninja = new Ninja("螺旋丸", "鳴人");
        Ninja ninjaClone = (Ninja) ninja.clone();
        ninjaClone.setName("分身");
        System.err.println(ninja.getName() + "招式>>>" + ninja.getSkill());
        System.err.println(ninjaClone.getName() + "招式>>>" + ninja.getSkill());
        ninja.setSkill("大玉螺旋丸");
        System.err.println(ninja.getName() + "招式>>>" + ninja.getSkill());
        System.err.println(ninjaClone.getName() + "招式>>>" + ninjaClone.getSkill());
    }
}
