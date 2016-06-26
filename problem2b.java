// 2.b) No loop.  Only constants, no variables.
// (The same code technically fulfills the requirements for 2.e) as well.)
public class problem2b{
    
    public static void main(String []args){
        System.out.println("1->0: " + fibonat(1));
        System.out.println("2->1: " + fibonat(2));
        System.out.println("3->1: " + fibonat(3));
        System.out.println("4->2: " + fibonat(4));
        System.out.println("5->3: " + fibonat(5));
        System.out.println("6->5: " + fibonat(6));
        System.out.println("7->8: " + fibonat(7));
    }
    
    public static int fibonat(int n) {
        n -= 1; // account for index starting at 0 in Java
        final double r5, Phi, phi; // these are all constants
        r5 = Math.sqrt(5);
        Phi = Math.pow((1+r5)/2,n);
        phi = Math.pow((1-r5)/2,n);
        return (int)((Phi-phi)/r5);
    }
}
