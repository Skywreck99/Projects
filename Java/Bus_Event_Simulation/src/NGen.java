
// NGen.java
// A *simplified* generic node class for use with the Stack1Gen class 
// and other data structures as desired; uses generics for the data

//Credited by: "CSci 1933 Lecture Examples."

public class NGen <T> {

    private T data;
    private NGen <T> next;

    // constructors
    public NGen () {}

    public NGen (T o, NGen <T> link) {
        data = o;
        next = link;
    }

    // selectors

    public T getData() {
        return data;
    }

    public void setData(T o) {
        data = o;
    }

    public NGen <T> getNext() {
        return next;
    }

    public void setNext(NGen <T> link) {
        next = link;
    }

}  // NGen class