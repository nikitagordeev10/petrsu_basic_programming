#Входные данные
input_string = "101023"

# Решение
def check(t):
    if len(t) < 4 and int(t) < 256 and int(t) > 0 and len(t) > 0:
        return True
    else:
        return False

correct_ip = []
for part1 in range(0, min(3, len(input_string)-3)):
    buf1_string = input_string[0:part1+1]

    if check(buf1_string):
        for part2 in range(part1+1, len(input_string)-2):
            buf2_string = input_string[part1+1:part2+1]

            if check(buf2_string):
                for part3 in range(part2+1, len(input_string)-1):
                    buf3_string = input_string[part2+1:part3+1]

                    if check(buf3_string):
                        for part4 in range(part3 + 1, len(input_string)):
                            buf4_string = input_string[part3+1:]

                            if check(buf4_string):
                                correct_ip.append(".".join([buf1_string,buf2_string,buf3_string,buf4_string]))
print(set(correct_ip))
