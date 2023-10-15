#include "bmp.h"

/*
 * Размытие движением 
 * 1/16 суммы произведений цветов в пределах матрицы 5x5
*/
void bmp_motion(bmp_image image)
{
    unsigned  int i, j;
    
    /* Получаем линейные размеры изображение */
    unsigned int w = image.header.width;
    unsigned int h = image.header.height;
    
    /* Инициализируем соответствующую заданию матрицу */
    int arr[5][5] = {    
    {2, 1, 1, 0, 0}, 
    {1, 1, 2, 1, 0}, 
    {0, 0, 1, 1, 1}, 
    {0, 0, 0, 1, 2}, 
    {0, 0, 0, 0, 1}
    };
    
    /* Для всех строк пикселей */
    for (i = 0; i < h; i++) {
        /* Для каждого пикселя */
        for (j = 0; j < w; j++){
        
	    /* Переменные длля произведения и суммы */
	    double pgr = 0.0, pred = 0.0, pb = 0.0;
	    double sgr = 0.0, sred = 0.0, sb = 0.0;

	    /* Для работы с матрицой весовых коэффициентов*/
	    int arr_i;
	    int arr_j;
	    
	    /* Начально положение в матрице весовых коэффициентов */
	    int nach_i = 0;
	    int nach_j = 0;
	    
	    /* Стартовые значения цикла, в зависимости от расположения пискселя в изображении*/ 
	    int start_k = i - 2;
	    int start_g = j - 2;

	    /* Проверка, на близкое расположение пикселя к границам изображения */
	    if (i < 2){
		start_k = 0;
		nach_i = 2 - i;
	    }
	    
	    if (j < 2){
		start_g = 0;
		nach_j = 2 - j;
	    }
	    
	    arr_i = nach_i;
	    for (unsigned int k = start_k; k < (i + 3); k++){
		arr_j = nach_j;
		for (unsigned int g = start_g; g < (j + 3); g++){
		    /* Выход за границу */
		    if ((k > h) || (g > w)){
		    	pred = 0.0;
		    	pgr = 0.0;
			pb = 0.0;
		    }
		    else{ 
			/* Получаем компоненты цвета текущего пикселя*/
			double blue = image.pixel_array[0 * h * w + k * w + g];
			double green = image.pixel_array[1 * h * w + k * w + g];
			double red = image.pixel_array[2 * h * w + k * w + g];
			
			/* Умножаем каждый цвет на весовые коэффициенты в соответствии с матрицей */
			pb = blue*arr[arr_i][arr_j];
			pgr = green*arr[arr_i][arr_j];
			pred = red*arr[arr_i][arr_j];
		    }
		    sred += pred;
		    sgr += pgr;
		    sb += pb;
		    arr_j += 1;
		}
		arr_i += 1;
	    }
	    
            /* Размываем движением  */
            image.pixel_array[0 * h * w + i * w + j] = sb / 16;
            image.pixel_array[1 * h * w + i * w + j] = sgr / 16;
	    image.pixel_array[2 * h * w + i * w + j] = sred / 16;
        }
    }
}

