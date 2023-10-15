/* программа вычисления и вывода (в стандартный вывод) суммы одноцифровых чисел. */

.include "my-macro" 		# подключение файла с макроопределениями

.data
	sum: .word 0		# переменная для суммы
	str_len: .long 0 	# переменная -- количество цифр в числе для вывода
	
	max_ten: .long 5       # 65535 (short int)
	max_oct: .long 6	# 177777
	max_bin: .long 16  	# 1111 1111 1111 1111
	
.bss
    .lcomm c, 1    		# буфер для чтения байта из файла stdin. Размер -- 1 байт
    .lcomm n, 1	
    .lcomm buf_output, 2 	# буфер для вывода. Размер -- 2 байта

.text

.global _start

_start:

show_prompt:
    Puts "Введите цифру"

kbd_input:
    Getchar $c          	# макровызов ввода байта из stdin в промежуточный буфер c

    cmpl $0, %eax       	# наступило событие EOF (конец файла stdin)?
    	je stop         	# да -> на завершение программы

    cmpb $'\n', c  		# это символ перевода строки ?
        je sum_num		# да -> идем записывать предшествующий символ в eax

    cmpb $'9', c        	# код больше кода символа '9'?
    	ja print_err_msg    	# да -> на вывод сообщения об ошибке

    cmpb $'0', c        	# код меньше кода символа '0'?
    	jb print_err_msg    	# да -> на вывод сообщения об ошибке

    movb c, %al		# копируем значение из с %al		
    movb %al, n		# копируем значение из %al в n

    jmp kbd_input

sum_num:
	xorl %eax, %eax	# обнуление %eax

	movb n, %al		# передаем в %al число
	subb $'0', %al		# получаем числовое значение
	addw %ax, sum
	jc print_err_of 	# проверка на переполнение
	
nextdigit_10:
    Puts "-- сумма в 10 системе счисления: "

    movw $10, %bx    		# в %ebx копируем текущую СС 
    movl max_ten, %esi  	# передаем в esi адрес первого элемента 
    movw sum, %ax 		# копируем сумму в %eax
    xorl %edi, %edi     	# обнуление %edi. Будем записывать итоговый буфер вывода
	xorl %ecx, %ecx	# обнуление %ecx. Будет счетчик цикла длины строки вывода

get_strlen_10:			# здесь идёт получение str_len для вывода
    incl %ecx               	# увеличение длины строки вывода
    xorl %edx, %edx		# обнуление %edx. хранения остатка
    divw %bx                	# делим %ax на %bx, остаток в %dx, в %ax храним целую часть
    addb $'0', %dl         	# получаем код числа. (add, т.к. при перемещении %dl в buf_output у содерижмого отнимается 48)
    movb %dl, buf_output(%esi) # копируем содержимое %edx в буфер по нужному смещению

    cmpw $0, %ax            	# дошли до нуля? (в %ax пусто?)
    	je additional_10  	# да -> заканчиваем преобразование и готовим буфер к выводу

    decl %esi               	# нет -> уменьшаем %esi на 1
    jmp get_strlen_10     	# и переходим в начало циклa

    
additional_10:
	incl max_ten  		# прибавляем 1 для сравнения
	movl %ecx, str_len 	# отправляем полученный %ecx в качестве значения длины строки

out_strlen_10:			# формирование массива для вывода 
    cmpl max_ten, %esi  	# в %esi максимальное возможное количество цифр в числе?
    	je output_10     	# да -> выход

    movb buf_output(%esi), %al 	# копируем байт по адресу buf_output(%esi) в %eax
    movb $0, buf_output(%esi)  	# записываем 0 по адресу buf_output(%esi)
    movb %al, buf_output(%edi) 	# записываем значение %al по адресу buf_output(%edi)
    inc %esi                		# увеличиваем %esi на 1
    inc %edi                		# увеличиваем %edi на 1
    jmp out_strlen_10    		# переходим в начало цикла

output_10:   # вывод суммы
	movl $4, %eax			# номер сист. вызова write
	movl $1, %ebx			# параметр 1: дескриптор стандартного вывода	
	movl $buf_output, %ecx		# параметр 2: адрес памяти с выводимыми символами
	movl str_len, %edx      	# параметр 3: количество байтов для вывода
	int $0x80			# выполнить системный вызов

	Puts ""
	movw $'0',buf_output          # обнуляем буфер вывода
	decl max_ten


nextdigit_8:
	Puts "-- сумма в 8 системе счисления: "

    movw $8, %bx    		# в %ebx копируем текущую СС 
    movl max_oct, %esi  	# передаем в esi адрес первого элемента (т.к. у Intel порядок байтов little endian, мы идем с конца массива (а+max -- начало чтения))
    movw sum, %ax 		# копируем сумму в %eax
    xorl %edi, %edi     	# обнуление %edi. Будем через него записывать итоговый буфер вывода
	xorl %ecx, %ecx	# обнуление %ecx. Будем использовать его как счетчик цикла -- длина строки вывода

# здесь идёт получение str_len для вывода
get_strlen_8:
    incl %ecx               	# увеличение длины строки вывода
    xorl %edx, %edx		# обнуление %edx. Будем использовать его для хранения остатка
    divw %bx                	# делим %ax на %bx, остаток в %dx
    addb $'0', %dl         	# получаем код числа.
    movb %dl, buf_output(%esi) # копируем содержимое %edx в буфер по нужному смещению

    cmpw $0, %ax            	# дошли до нуля? (в %ax пусто?)
    	je additional_8	# да -> заканчиваем преобразование и готовим буфер к выводу

    decl %esi               	# нет -> уменьшаем %esi на 1
    jmp get_strlen_8     	# и переходим в начало циклa

    
additional_8:
	incl max_oct  		# прибавляем 1 для сравнения
	movl %ecx, str_len 	# отправляем полученный %ecx в качестве значения длины строки

# формирование массива для вывода #
out_strlen_8:
    cmpl max_oct, %esi  	# в %esi максимальное возможное количество цифр в числе?
    	je output_8     	# да -> выход

    movb buf_output(%esi), %al 	# копируем байт по адресу buf_output(%esi) в %eax
    movb $0, buf_output(%esi)  	# записываем 0 по адресу buf_output(%esi)
    movb %al, buf_output(%edi) 	# записываем значение %al по адресу buf_output(%edi)
    inc %esi                		# увеличиваем %esi на 1
    inc %edi                		# увеличиваем %edi на 1
    jmp out_strlen_8    		# переходим в начало цикла

output_8:   # вывод суммы

	movl $4, %eax			# номер сист. вызова write
	movl $1, %ebx			# параметр 1: дескриптор стандартного вывода	
	movl $buf_output, %ecx		# параметр 2: адрес памяти с выводимыми символами
	movl str_len, %edx      	# параметр 3: количество байтов для вывода
	int $0x80			# выполнить системный вызов

	Puts ""
	movw $'0',buf_output		# обнуляем буфер вывода
	decl max_oct


nextdigit_2:
    Puts "-- сумма в 2 системе счисления: "

    movw $2, %bx    			# в %ebx копируем текущую СС 
    movl max_bin, %esi  		# передаем в esi адрес первого элемента (т.к. у Intel порядок байтов little endian, мы идем с конца массива (а+max -- начало чтения))
    movw sum, %ax 			# копируем сумму в %eax
    xorl %edi, %edi     		# обнуление %edi. Будем через него записывать итоговый буфер вывода
	xorl %ecx, %ecx		# обнуление %ecx. Будем использовать его как счетчик цикла -- длина строки вывода

# Получение str_len для вывода
get_strlen_2:
    incl %ecx               		# увеличение длины строки вывода
    xorl %edx, %edx           	# обнуление %edx. Будем использовать его для хранения остатка
    divw %bx                		# делим %ax на %bx, остаток в %dx
    addb $'0', %dl         		# получаем код числа.
    movb %dl, buf_output(%esi) 	# копируем содержимое %edx в буфер по нужному смещению

    cmpw $0, %ax            		# дошли до нуля? (в %ax пусто?)
    	je additional_2  	    	# да -> заканчиваем преобразование и готовим буфер к выводу

    decl %esi               		# нет -> уменьшаем %esi на 1
    jmp get_strlen_2     		# и переходим в начало циклa

    
additional_2:
	incl max_bin  			# прибавляем 1 для сравнения
	movl %ecx, str_len 		# отправляем полученный %ecx в качестве значения длины строки

	
out_strlen_2:
    cmpl max_bin, %esi  		# в %esi максимальное возможное количество цифр в числе?
    	je output_2     		# да -> выход

    movb buf_output(%esi), %al 	# копируем байт по адресу buf_output(%esi) в %eax
    movb $0, buf_output(%esi)  	# записываем 0 по адресу buf_output(%esi)
    movb %al, buf_output(%edi) 	# записываем значение %al по адресу buf_output(%edi)
    inc %esi                		# увеличиваем %esi на 1
    inc %edi                		# увеличиваем %edi на 1
    jmp out_strlen_2    		# переходим в начало цикла


output_2:   # вывод суммы

    movl $4, %eax			# номер сист. вызова write
    movl $1, %ebx			# параметр 1: дескриптор стандартного вывода	
    movl $buf_output, %ecx		# параметр 2: адрес памяти с выводимыми символами
    movl str_len, %edx      		# параметр 3: количество байтов для вывода
    int $0x80				# выполнить системный вызов

    Puts ""
    movw $'0',buf_output          	# обнуляем буфер вывода

    Puts ""
    Puts "******************************************"
    Puts ""
    decl max_bin
    jmp show_prompt


print_err_msg:
    Puts "Ошибка: не цифровая клавиша. повторите ввод"
    jmp kbd_input


print_err_of:
    Puts "Ошибка: переполнение буфера"
    jmp stop


stop:
    Exit $0

.end
