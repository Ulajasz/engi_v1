from clean_text import clean_txt
from sim_word import sim_word


def main():

    input_text = input('Link:')
    x = clean_txt(input_text)

    #word = input('Słowo do sima: ')
    sim_word(x)
    #print(type(clean_txt))


main()

