public class RedGiant extends Star{

    public RedGiant(String name, double mass, double size) {
        super(name,mass,size);

    }


    public boolean isSuperGiant() {
        if(getMass() > 100 && getSize() > 100) {
            return true;
        } else {
            return false;
        }
    }

    public boolean isBlackHole() {
        return isSuperGiant();
    }

    public String toString() {
        if(isSuperGiant()) {
            return "<" + getName() + ">:" + "A SuperGiant with mass = <" + getMass() + "> KG; and " + "Size = <" + getSize() + "> miles";
        }
        else {
            return "<" + getName() + ">:" + "A RedGiant with mass = <" + getMass() + "> KG; and " + "Size = <" + getSize() + "> miles";
        }
    }
}