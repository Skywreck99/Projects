
public class Sequence extends Star {

    public Sequence(String name, double mass, double size) {
        super(name,mass,size);
    }


    public boolean isSun() {
        if( getMass() == 2 && getSize() == 430) {
            return true;
        }
        else {
            return false;
        }
    }

    public boolean isBlackHole() {
        if(getMass() > 1000 && getSize() < 50) {
            return true;
        }
        else {
            return false;
        }
    }

    public String toString() {
        return "<" + getName() + ">:" + "A Sequence Star with mass = <" + getMass() + "> KG; and " + "Size = <" + getSize() + "> miles";

    }

}