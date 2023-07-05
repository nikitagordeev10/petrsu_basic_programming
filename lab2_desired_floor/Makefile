# цель по умолчанию (при вызове make или make floor)
# собираем программу floor из объектного файла floor.o
floor: floor.o
	gcc -g -O0 -o floor floor.o

floor.o: floor.c
	gcc -g -O0 -c -Wall -Wextra -pedantic -pedantic-errors -ansi -std=c11 floor.c

# команда indent используется для автоформатирования кода
# -kr: используется стиль форматирования K&R
# -nut: запрещает использование табуляции для отступов
# -ts4: устанавливает размер отступа равным 4 пробелам
# main.c: файл, который будет отформатирован
indent:
	indent -kr -nut -ts4 main.c

# цель clean (при вызове make clean)
# удаляем программу и объектные файлы
clean:
	rm floor.o

Что за файлы: dryrun.log и targets.log