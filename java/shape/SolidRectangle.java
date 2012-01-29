package shape;
import java.awt.Color;
import java.awt.Graphics;

public class SolidRectangle extends Rectangle {
    public void draw(Graphics g) {
        super.draw(g);
        int width = getWidth()-1;
        int height = getHeight()-1;
        int x = (getCenter().getX() - width/2);
        int y = (getCenter().getY() - height/2);
        g.setColor(Color.GRAY);
        g.fillRect(x, y, width, height);
    }
}
