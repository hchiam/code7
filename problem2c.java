// 2.c) No local variables.
public class problem2c{

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
         n -= 1;
         return (int)((Math.pow((1+Math.sqrt(5))/2,n)-Math.pow((1-Math.sqrt(5))/2,n))/Math.sqrt(5));
     }
}
