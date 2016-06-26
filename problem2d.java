// 2.d) Tail recursion (the function calls itself on the last line in said function).
public class problem2d{

     public static void main(String []args){
        System.out.println("1->0: " + fibonat(1,0,1));
        System.out.println("2->1: " + fibonat(2,0,1));
        System.out.println("3->1: " + fibonat(3,0,1));
        System.out.println("4->2: " + fibonat(4,0,1));
        System.out.println("5->3: " + fibonat(5,0,1));
        System.out.println("6->5: " + fibonat(6,0,1));
        System.out.println("7->8: " + fibonat(7,0,1));
     }
     
     public static int fibonat(int stepsLeft, int prev, int curr) {
         //"tail recursion"
         //recursive, non-modified return line as last line
         if (stepsLeft == 1) {
             // for the last step:
            return prev;
         } else {
             // for all the other steps:
             int currHold = curr;
             currHold = curr;
             curr += prev;
             prev = currHold;
            return fibonat(stepsLeft-1,prev,curr);
         }
     }
     
}