import java.util.Scanner;
import java.awt.*;

public class Fractals {
    //public double Area = 0;

    public static void main(String[] args) {
        System.out.println("Please choose your shape (Circle, Rectangle, Triangle)");
        Scanner MyScanner = new Scanner(System.in);
        String choice = MyScanner.nextLine();
        if (choice.equals("Rectangle")) {
            Canvas createR = new Canvas();
            recursiveR(createR, Color.BLUE, 540, 300, 500, 400, 0);
            //System.out.println("This is the Area:" + Area);
        }
        else if (choice.equals("Triangle")) {
            Canvas createT = new Canvas();
            recursiveT(createT, Color.BLUE, 525, 500, 500, -400, 0);
        }
        else if (choice.equals("Circle")) {
            Canvas createC = new Canvas();
            recursiveC(createC, Color.BLUE, 780, 550, 200, 0);
        }
        else if (choice.equals("LabTriangle")) {
            Canvas createT = new Canvas();
            recursiveLT(createT, Color.BLUE, 525, 100, 500, -400, 0);
        }
    }

    public static void recursiveC(Canvas createC, Color c, double pos_x, double pos_y, double radius, int count) {
        if (count == 8) {
            return;
        } else {
            Circle theCircle = new Circle(pos_x, pos_y, radius);
            Color nextcolor = c;
            if (c == Color.BLUE) {
                nextcolor = Color.GREEN;
            }
            else if (c == Color.GREEN) {
                nextcolor = Color.RED;
            }
            else if (c == Color.RED) {
                nextcolor = Color.BLUE;
            }
            theCircle.setColor(nextcolor);
            createC.drawShape(theCircle);
            count++;
            recursiveC(createC, nextcolor, pos_x - radius*1.5, pos_y, radius/2, count);
            recursiveC(createC, nextcolor, pos_x + radius*1.5, pos_y, radius/2, count);
            recursiveC(createC, nextcolor, pos_x, pos_y - radius*1.5, radius/2, count);
            recursiveC(createC, nextcolor, pos_x, pos_y + radius*1.5, radius/2, count);


        }
    }

    public static void recursiveT(Canvas createT, Color c, double pos_x, double pos_y, double width, double height, int count) {

        if (count == 8) {
            return;
        } else {
            Triangle theTriangle = new Triangle(pos_x, pos_y, width, height);
            Color nextcolor = c;

            // This is how to change the color of the Triangles every time it runs recursively
            if (c == Color.BLUE) {
                nextcolor = Color.GREEN;
            }
            else if (c == Color.GREEN) {
                nextcolor = Color.RED;
            }
            else if (c == Color.RED) {
                nextcolor = Color.BLUE;
            }
            theTriangle.setColor(nextcolor);
            createT.drawShape(theTriangle);
            count++;
            recursiveT(createT, nextcolor,pos_x - width/2, pos_y, width / 2, height / 2, count); // Draw a triangle in a different position
            recursiveT(createT, nextcolor, pos_x + width, pos_y, width / 2, height / 2, count); // Draw a triangle in a different position
            recursiveT(createT, nextcolor, pos_x + width/4, pos_y + height / 2, width / 2, height / 2, count); // Draw a triangle in a different position
        }
    }
    public static void recursiveR(Canvas createR, Color c, double pos_x, double pos_y, double width, double height, int count) {
        if (count == 8) {
            return;
        } else {
            Rectangle theRectangle = new Rectangle(pos_x, pos_y, width, height);
            Color nextcolor = c;
            if (c == Color.BLUE) {
                nextcolor = Color.GREEN;
            } else if (c == Color.GREEN) {
                nextcolor = Color.RED;
            } else if (c == Color.RED) {
                nextcolor = Color.BLUE;
            }
            theRectangle.setColor(nextcolor);
            createR.drawShape(theRectangle);
            count++;
            recursiveR(createR, nextcolor,pos_x - width/2, pos_y - height/2, width / 2, height / 2, count);
            recursiveR(createR, nextcolor, pos_x - width/2, pos_y + height, width / 2, height / 2, count);
            recursiveR(createR, nextcolor, pos_x + width, pos_y - height/2, width / 2, height / 2, count);
            recursiveR(createR, nextcolor,pos_x + width, pos_y + height, width / 2, height / 2, count);
            //area += theRectangle.calculateArea();
        }
    }
    public static void recursiveLT(Canvas createT, Color c, double pos_x, double pos_y, double width, double height, int count) {

        if (count == 8) {
            return;
        } else {
            Triangle theTriangle = new Triangle(pos_x, pos_y, width, height);
            Color nextcolor = c;
            if (c == Color.BLUE) {
                nextcolor = Color.GREEN;
            } else if (c == Color.GREEN) {
                nextcolor = Color.RED;
            } else if (c == Color.RED) {
                nextcolor = Color.BLUE;
            }
            theTriangle.setColor(nextcolor);
            createT.drawShape(theTriangle);
            count++;
            recursiveLT(createT, nextcolor, pos_x - width / 2, pos_y, width / 2, height / 2, count);
            recursiveLT(createT, nextcolor, pos_x + width, pos_y, width / 2, height / 2, count);
            recursiveLT(createT, nextcolor, pos_x + width / 4, pos_y - height, width / 2, height / 2, count);
        }
    }
}
