
package test;

import domain.Persona;


public class TestJavaBeans {
    public static void main(String[] args) {
        //Creamos un objeto de la clase persona
        Persona persona = new Persona();
        //Mediante el metodo set, le asignamos un nombre y un apellido
        persona.setNombre("Juan");
        persona.setApellido("Perez");
        //Imprimimos el objeto persona
        System.out.println("persona = " + persona);
        
        //Obtenemos el nombre y el apellido mediante los métodos get
        System.out.println("Persona nombre: " + persona.getNombre());
        System.out.println("Persona nombre: " + persona.getApellido());
        
    }
}
