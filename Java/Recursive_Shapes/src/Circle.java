import java.awt.*;
import java.lang.Math;

public class Circle {
    double radius;
    double pos_x;
    double pos_y;
    Color color;

    public Circle(double pos_x, double pos_y, double radius) {
        this.radius = radius;
        this.pos_x = pos_x;
        this.pos_y = pos_y;

    }

    public double calculatePerimeter() {
        double perimeter = 2 * Math.PI * radius;
        return perimeter;
    }

    public double calculateArea() {
        double area = Math.PI * radius * radius;
        return area;
    }

    public void setColor(Color c) {
        color = c;
    }

    public void setPos(double pos_x, double pos_y) {
        this.pos_x = pos_x;
        this.pos_y = pos_y;
    }

    public void setRadius(double radius) {
        this.radius = radius;
    }

    public Color getColor() {
        return color;
    }

    public double getXPos() {
        return this.pos_x;
    }

    public double getYPos() {
        return this.pos_y;
    }

    public double getRadius() {
        return this.radius;
    }

}
