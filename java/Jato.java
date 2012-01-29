/* Exemplo traduzido de Head First Object Oriented Analysis and Design
*/

public class Jato extends Aviao{
    private static final int MULTIPLICADOR = 2;

    public Jato() {
        super();
    }

    public void setVelocidade(int vel) {
        super.setVelocidade(vel * MULTIPLICADOR);
    }

    public void acelerar() {
        super.setVelocidade(getVelocidade() * 2);
    }

}