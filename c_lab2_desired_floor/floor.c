#include<stdio.h>

int main(void)
{
    /* Номер квартиры */
    int flat_number;

    /* Число квартир на этаже */
    int flats_per_floor;
 
    /* Запрашиваем квартиру, в которой проживает адресат */
    printf("Введите номер интересующей квартиры: ");
    scanf("%d", &flat_number);

    /* Запрашиваем число квартир на этаже */
    printf("Введите число квартир на каждом этаже: ");
    scanf("%d", &flats_per_floor);

    /* Рассчитываем и выводим номер этажа */
    int floor_number = 1 + (flat_number - 1) / flats_per_floor;
    printf("Вам нужно подняться на этаж %d\n", floor_number);

    return 0;
}
