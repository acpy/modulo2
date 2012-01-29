/* Exemplo traduzido de Head First Object Oriented Analysis and Design
*/

public class TesteVoo3 {
    public static void main(String[] args) {
        Jato jato1 = new Jato();
        jato1.velocidade = 212;
        System.out.println(jato1.velocidade);
        Jato jato2 = new Jato();
        jato2.setVelocidade(212);
        System.out.println(jato2.getVelocidade());
    }
}