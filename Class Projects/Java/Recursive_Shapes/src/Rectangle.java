import java.awt.*;
import java.lang.Math;

public class Rectangle {
    double pos_x;
    double pos_y;
    double width;
    double height;
    Color color;

    public Rectangle(double pos_x, double pos_y, double width, double height) {
        this.pos_x = pos_x;
        this.pos_y = pos_y;
        this.width = width;
        this.height = height;
    }

    public double calculatePerimeter() {
        double perimeter = 2 * (width + height);
        return perimeter;
    }

    public double calculateArea() {
        double Area = width * height;
        return Area;
    }

    public void setColor(Color c) {
        color = c;

    }

    public void setPos(double pos_x, double pos_y) {
        this.pos_x = pos_x;
        this.pos_y = pos_y;

    }

    public void setHeight(double height) {
        this.height = height;
    }

    public void setWidth(double width) {
        this.width = width;
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

    public double getHeight() {
        return height;
    }

    public double getWidth() {
        return width;
    }

}

