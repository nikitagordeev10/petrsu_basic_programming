/* Нахождение факториала*/
	
.include "my-macro"      # подключение файла с макроопределениями

.text

.global _start
_start:
	movl $5, %eax    /* число, для которого ищется факториал */
	movl $1, %ebx    /* шаг */
L1:
	cmpl $0, %eax    /* частное = 0 ? */
	je L2            /* переход, если равно */
	imull %eax, %ebx /* умножить числа со шагом */
	decl %eax        /* уменьшить */
 	jmp L1           /* переход */

L2:
	Finish
.end
