import java.lang.Math;
import java.awt.*;

public class Triangle {
    double pos_x;
    double pos_y;
    double width;
    double height;
    private Color color;

    public Triangle(double pos_x, double pos_y, double width, double height) {
        this.pos_x = pos_x;
        this.pos_y = pos_y;
        this.width = width;
        this.height = height;
    }

    public double calculatePerimeter() {
        double side = Math.sqrt((width / 2) * (width / 2) + (height * height));
        double perimeter = side + side + width;
        return perimeter;
    }

    public double calculateArea() {
        double Area = width * height / 2;
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
        return this.height;
    }

    public double getWidth() {
        return this.width;
    }

}