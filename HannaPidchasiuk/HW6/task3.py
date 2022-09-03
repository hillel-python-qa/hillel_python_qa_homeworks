# You have the file text.txt(attached). Please count how many times each letter appears in this task.
import re

if __name__ == "__main__":
    with open("text.txt", "r") as file:
        text_for_check = file.read()

    letters_from_text = re.findall(r"[A-Za-z]{1}", text_for_check)

    counter_a = 0
    counter_b = 0
    counter_c = 0
    counter_d = 0
    counter_e = 0
    counter_f = 0
    counter_g = 0
    counter_h = 0
    counter_i = 0
    counter_j = 0
    counter_k = 0
    counter_l = 0
    counter_m = 0
    counter_n = 0
    counter_o = 0
    counter_p = 0
    counter_q = 0
    counter_r = 0
    counter_s = 0
    counter_t = 0
    counter_u = 0
    counter_v = 0
    counter_w = 0
    counter_x = 0
    counter_y = 0
    counter_z = 0
    for letter in letters_from_text:
        if letter.lower() == 'a':
            counter_a += 1
        elif letter.lower() == 'b':
            counter_b += 1
        elif letter.lower() == 'c':
            counter_c += 1
        elif letter.lower() == 'd':
            counter_d += 1
        elif letter.lower() == 'e':
            counter_e += 1
        elif letter.lower() == 'f':
            counter_f += 1
        elif letter.lower() == 'g':
            counter_g += 1
        elif letter.lower() == 'h':
            counter_h += 1
        elif letter.lower() == 'i':
            counter_i += 1
        elif letter.lower() == 'j':
            counter_j += 1
        elif letter.lower() == 'k':
            counter_k += 1
        elif letter.lower() == 'l':
            counter_l += 1
        elif letter.lower() == 'm':
            counter_m += 1
        elif letter.lower() == 'n':
            counter_n += 1
        elif letter.lower() == 'o':
            counter_o += 1
        elif letter.lower() == 'p':
            counter_p += 1
        elif letter.lower() == 'r':
            counter_r += 1
        elif letter.lower() == 's':
            counter_s += 1
        elif letter.lower() == 't':
            counter_t += 1
        elif letter.lower() == 'u':
            counter_u += 1
        elif letter.lower() == 'v':
            counter_v += 1
        elif letter.lower() == 'w':
            counter_w += 1
        elif letter.lower() == 'x':
            counter_x += 1
        elif letter.lower() == 'y':
            counter_y += 1
        elif letter.lower() == 'z':
            counter_z += 1
        else:
            continue

    print(f'Number of letter A = {counter_a}\n'
          f'Number of letter B = {counter_b}\n'
          f'Number of letter C = {counter_c}\n'
          f'Number of letter D = {counter_d}\n'
          f'Number of letter E = {counter_e}\n'
          f'Number of letter F = {counter_f}\n'
          f'Number of letter G = {counter_g}\n'
          f'Number of letter H = {counter_h}\n'
          f'Number of letter I = {counter_i}\n'
          f'Number of letter G = {counter_g}\n'
          f'Number of letter K = {counter_k}\n'
          f'Number of letter L = {counter_l}\n'
          f'Number of letter M = {counter_m}\n'
          f'Number of letter N = {counter_n}\n'
          f'Number of letter O = {counter_o}\n'
          f'Number of letter P = {counter_p}\n'
          f'Number of letter Q = {counter_q}\n'
          f'Number of letter R = {counter_r}\n'
          f'Number of letter S = {counter_s}\n'
          f'Number of letter T = {counter_t}\n'
          f'Number of letter U = {counter_u}\n'
          f'Number of letter V = {counter_v}\n'
          f'Number of letter W = {counter_w}\n'
          f'Number of letter X = {counter_x}\n'
          f'Number of letter Y = {counter_y}\n'
          f'Number of letter Z = {counter_z}\n')
