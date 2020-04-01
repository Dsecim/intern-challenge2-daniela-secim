import java.util.Scanner;

public class Matrix_d{
        public static void main(String[] args){
     Scanner input= new Scanner(System.in);
     System.out.print("digite o número de casos");
     int choice= input.nextInt();
     System.out.println();
     for(int k=0;k<choice;k++){
                System.out.print("digite as proporções da matriz:");
                int N = input.nextInt();
                System.out.println("Matrix("+N+")"+"("+N+")");
                int num=(int) Math.pow(2,(N-1));
                int val=num;
                //utiliza os operadores de deslocamento
                for (int i=0;i<N;i++){
                        for (int j=num;j>0;j=j/2){
                                if((val&j)!=0)System.out.print("1 ");
                                else System.out.print("0 ");
                        }
                        System.out.println();
                        val=val>>1;
                }
      }
   }
}
