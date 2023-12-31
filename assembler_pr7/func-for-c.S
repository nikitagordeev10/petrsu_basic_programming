# Функции as , вызываемые из С
	
.globl	Numbers	# имя, ОПРЕДЕЛЕННОЕ вне этого исходного файла	
	
.text # секция команд процесора
	
.type	Read_Sym, @function	# функция циклической обработки массива
.globl	Read_Sym		# имя может ИСПОЛЬЗОВАТЬСЯ вне этого исх. файла

# -------------------------------------------------------------------
# -------------------------------------------------------------------
# -------------------------------------------------------------------

Read_Sym:
/*
	Читает <Параметр1> символов из массива <Параметр2>
	и передает их на обработку функции Trans_Sym.
	Результат размещается в массив Numbers
*/

	# Стандартный пролог фунции
	
	pushl %ebp 	 # сохранить в стеке значение, бывшее в вызывающей
	movl  %esp, %ebp # обеспечить адресный доступ к параметрам и
			 # локальным переменнным в стеке путем базовой 
			 # адресации через ebp
	                 

	# Тело функции

	subl %ecx, %ecx   # инициализация счетчика цикла	


NextSym:	
	movl 12(%ebp), %edx  # адрес второго параметра-массива в edx

	# вызов функции Trans_Sym	
	
	subl %ebx, %ebx	     	    # подготовка ebx для записи символа
	movb (%edx,%ecx,1), %bl     # символ в ebx

	# Начинаем вызов Trans_Sym

	pusha		# сохранить регистры текущей функции Read_Sym	

	pushl %ebx  	# Параметр функции Trans_Sym (код 
			# символа из массива) в стек
	
	call Trans_Sym

	addl $4,%esp	# очистить стек от параметров Trans_Sym

	movl %eax, Numbers(,%ecx,4) 	# записать результат Trans-Sym

	popa	# восстановть регистры Read_Sym		
	
	incl %ecx	     # наращиваем счетчик цикла
	cmpl 8(%ebp), %ecx   # счетчик равен первому параметру?
	jne NextSym	     # ДА, повторяем
			     # НЕТ - выходим из цикла

	# Стандартный эпилог функции

	movl %ebp, %esp # восстановить указатель стека
	popl %ebp       # восстановить ebp
	ret		# возврат в вызывающую
	
	# конец Read_Sym

	
# -------------------------------------------------------------------
# -------------------------------------------------------------------
# -------------------------------------------------------------------

.type	Trans_Sym, @function  	
.globl Trans_Sym
Trans_Sym:

/*
    Функция преобразования кода символа в числовое значение
    <Пареметр1> преобразуется в число и возвращается в eax    
*/

	# Стандартный пролог фунции

	pushl %ebp 	 # сохранить в стеке значение, бывшее в вызывающей
	movl  %esp, %ebp # обеспечить адресный доступ к параметрам и 
			 # локальным переменнным в стеке путем базовой 
			 # адресации через ebp

	# тело функции

	movl 8(%ebp), %eax  # параметр в eax

	cmpb $'9', %al 	 # NNN код больше кода символа '9' ?
	ja Ret_error     # NNN ДА - на возврат -1
	cmpb $'0', %al	 # NNN код меньше кода сивола '0' ?
	jb Ret_error     # NNN ДА - на возврат -1
	
	subl $0x30, %eax # NNN получение числового значения
	
	jmp Ret_norm 	 # NNN на возврат числ. значения цифры

Ret_error:

	movl $0, %eax	 # NNN для возврата если код не символ цифры

Ret_norm:	

	# Стандартный эпилог функции

	movl %ebp, %esp # восстановить указатель стека
	popl %ebp       # восстановить ebp
	ret		# возврат в вызывающую

	# конец Trans_Sym

# -------------------------------------------------------------------
# -------------------------------------------------------------------
# -------------------------------------------------------------------

.type	Sum, @function	# функция циклической обработки массива
.globl	Sum		# имя может ИСПОЛЬЗОВАТЬСЯ вне этого исх. файла
Sum:

/*
    Функция преобразования кода символа в числовое значение
    <Пареметр1> преобразуется в число и возвращается в eax    
*/

# Стандартный пролог фунции
	
	pushl %ebp 	 # сохранить в стеке значение, бывшее в вызывающей
	movl  %esp, %ebp # обеспечить адресный доступ к параметрам и
			 # локальным переменнным в стеке путем базовой 
			 # адресации через ebp
	                 

	# Тело функции

	subl %ecx, %ecx   # инициализация счетчика цикла	
	subl %eax, %eax

NextNum:

	addl Numbers(,%ecx,4), %eax
		
	incl %ecx	     # наращиваем счетчик цикла
	cmpl 8(%ebp), %ecx   # счетчик равен первому параметру?
	jne NextNum	     # ДА, повторяем
			     # НЕТ - выходим из цикла

	# Стандартный эпилог функции

	movl %ebp, %esp # восстановить указатель стека
	popl %ebp       # восстановить ebp
	ret		# возврат в вызывающую
	
	# конец Sum

	
	
	

.end

