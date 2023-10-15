/* программа вычисления и вывода (в стандартный вывод) суммы одноцифровых чисел. */

.include "my-macro" 		# подключение файла с макроопределениями

.bss
    .lcomm c, 1    		# буфер для чтения байта из файла stdin. Размер -- 1 байт
    .lcomm n, 1	
    .lcomm buf_output, 2 	# буфер для вывода. Размер -- 2 байта
    .lcomm sign, 1		# буфер для знака. Размер -- 2 байта
    
.data
	sum: .word 0		# переменная для суммы
	str_len: .long 0 	# переменная -- количество цифр в числе для вывода
	
	max_ten: .long 5       # 65535 (short int)
	max_oct: .long 6	# 177777
	max_bin: .long 16  	# 1111 1111 1111 1111
	
.text				# секция команд процесора
.global _start			# точка входа - глобальная метка

_start:

show_prompt:
    Puts "Введите цифру"

kbd_input:
    Getchar $c          	# макровызов ввода байта из stdin в промежуточный буфер c

    cmpl $0, %eax       	# наступило событие EOF (конец файла stdin)?
    	je stop         	# да -> на завершение программы

    cmpb $'\n', c  		# это символ перевода строки ?
        je get_num_10		# ДА - считаем сумму

    cmpb $'-', c		# это символ '-' ?
    je set_sign		# да -> идем записывать предшествующий символ в set_sign

    cmpb $'9', c        	# код больше кода символа '9'?
    	ja reset_sign    	# ДА - игнорируем

    cmpb $'0', c        	# код меньше кода символа '0'?
    	jb reset_sign    	# ДА - игнорируем

    movb c, %al		# копируем значение из с %al		
    movb %al, n		# копируем значение из %al в n

    bt $1, sign
    jc reset_sign
    orb $2, sign
    jmp kbd_input    
    
set_sign:
    movb $1, sign
    movb $0, n
    jmp kbd_input

reset_sign:
    movb $0, sign
    jmp kbd_input

get_num_10:
    xorl %eax, %eax	# обнуление %eax

    movb n, %al		# передаем в %al число
    subb $'0', %al		# получаем числовое значение
    cmpb $3, sign
    jne nextdigit_10
    negw %ax
    movb $0, sign
	
nextdigit_10:
    addw %ax, sum
    jo print_err_of 	# проверка на переполнение
	    
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
    addb $'0', %dl         	# получаем код числа. 
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

    movb c, %al		# копируем значение из с %al		
    movb %al, n		# копируем значение из %al в n
    
    
    
    
/*    
get_num_8:
    xorl %eax, %eax	# обнуление %eax

    movb n, %al		# передаем в %al число
    subb $'0', %al		# получаем числовое значение
    cmpb $3, sign
    jne nextdigit_8
    negw %ax
    movb $0, sign
	
nextdigit_8:
    addw %ax, sum
    jo print_err_of 	# проверка на переполнение
	    
    Puts "-- сумма в 8 системе счисления: "

    movw $8, %bx    		# в %ebx копируем текущую СС 
    movl max_oct, %esi  	# передаем в esi адрес первого элемента 
    movw sum, %ax 		# копируем сумму в %eax
    xorl %edi, %edi     	# обнуление %edi. Будем записывать итоговый буфер вывода
	xorl %ecx, %ecx	# обнуление %ecx. Будет счетчик цикла длины строки вывода

get_strlen_8:			# здесь идёт получение str_len для вывода
    incl %ecx               	# увеличение длины строки вывода
    xorl %edx, %edx		# обнуление %edx. хранения остатка
    divw %bx                	# делим %ax на %bx, остаток в %dx, в %ax храним целую часть
    addb $'0', %dl         	# получаем код числа. 
    movb %dl, buf_output(%esi) # копируем содержимое %edx в буфер по нужному смещению

    cmpw $0, %ax            	# дошли до нуля? (в %ax пусто?)
    	je additional_8  	# да -> заканчиваем преобразование и готовим буфер к выводу

    decl %esi               	# нет -> уменьшаем %esi на 1
    jmp get_strlen_8     	# и переходим в начало циклa

    
additional_8:
	incl max_oct  		# прибавляем 1 для сравнения
	movl %ecx, str_len 	# отправляем полученный %ecx в качестве значения длины строки

out_strlen_8:			# формирование массива для вывода 
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
    movw $'0',buf_output          # обнуляем буфер вывода
    decl max_oct

    movb c, %al		# копируем значение из с %al		
    movb %al, n		# копируем значение из %al в n

    bt $1, sign
    jc reset_sign
    orb $2, sign
    jmp kbd_input 

set_sign:
    movb $1, sign
    movb $0, n
    jmp kbd_input

reset_sign:
    movb $0, sign
    jmp kbd_input
        
get_num_2:
    xorl %eax, %eax	# обнуление %eax

    movb n, %al		# передаем в %al число
    subb $'0', %al		# получаем числовое значение
    cmpb $3, sign
    jne nextdigit_2
    negw %ax
    movb $0, sign
	
nextdigit_2:
    addw %ax, sum
    jo print_err_of 	# проверка на переполнение
	    
    Puts "-- сумма в 2 системе счисления: "

    movw $2, %bx    		# в %ebx копируем текущую СС 
    movl max_bin, %esi  	# передаем в esi адрес первого элемента 
    movw sum, %ax 		# копируем сумму в %eax
    xorl %edi, %edi     	# обнуление %edi. Будем записывать итоговый буфер вывода
	xorl %ecx, %ecx	# обнуление %ecx. Будет счетчик цикла длины строки вывода

get_strlen_2:			# здесь идёт получение str_len для вывода
    incl %ecx               	# увеличение длины строки вывода
    xorl %edx, %edx		# обнуление %edx. хранения остатка
    divw %bx                	# делим %ax на %bx, остаток в %dx, в %ax храним целую часть
    addb $'0', %dl         	# получаем код числа. 
    movb %dl, buf_output(%esi) # копируем содержимое %edx в буфер по нужному смещению

    cmpw $0, %ax            	# дошли до нуля? (в %ax пусто?)
    	je additional_2  	# да -> заканчиваем преобразование и готовим буфер к выводу

    decl %esi               	# нет -> уменьшаем %esi на 1
    jmp get_strlen_2     	# и переходим в начало циклa

    
additional_2:
	incl max_bin  		# прибавляем 1 для сравнения
	movl %ecx, str_len 	# отправляем полученный %ecx в качестве значения длины строки

out_strlen_2:			# формирование массива для вывода 
    cmpl max_bin, %esi  	# в %esi максимальное возможное количество цифр в числе?
    	je output_2     	# да -> выход

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
    movl str_len, %edx      	# параметр 3: количество байтов для вывода
    int $0x80			# выполнить системный вызов

    Puts ""
    movw $'0',buf_output          # обнуляем буфер вывода
    decl max_bin        
*/        
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
