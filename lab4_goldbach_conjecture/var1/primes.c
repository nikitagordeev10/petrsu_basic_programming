#include<stdio.h>
int main(){
    int i, N, t, k;

    printf("Введите верхнюю границу отрезка подбора простых чисел: ");
    scanf("%d", &N);
    for (k=2; k<=N; k++){
        i = 2;
        t = 0;
        while(i < k){
            if (k%i==0){
                t++;
            }
            i++;
        }
        if(t==0){
            printf("%d ", k);
        }
    }
    printf("\n");
}
