package shape;
import java.awt.Graphics;

public class Rectangle extends Shape {
    private int height = 0;
    private int width = 0;

    public void draw(Graphics g) {
        int x = (getCenter().getX() - width/2);
        int y = (getCenter().getY() - height/2);
        g.drawRect(x, y, width, height);
    }

    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }

    public int getWidth() {
        return width;
    }
    public void setWidth(int width) {
        this.width = width;
    }
}
