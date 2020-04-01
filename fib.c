#include<stdio.h>
int fib_recursivo(unsigned int n){
        if (n==0){
           return 0;

        }else{
              if (n==1){
                return 1;

             }else{
                if (n==2){
                        return 1;
                }else{

                       return fib_recursivo(n-1)+fib_recursivo(n-2);
                }
            }

        }
}
int main(){
        unsigned int num,resp;
        printf("digite um numero:\t");
        scanf("%d",&num);
        resp=fib_recursivo(num);
        printf("Fib(%d):%d\n",num,resp);
        return 0;
}
