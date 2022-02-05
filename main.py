from clean_text import clean_txt
from sim_word import sim_word
from vocabulary import vocabulary

def main():

    input_text = input('Link:')
    x = clean_txt(input_text)

    #word = input('Słowo do sima: ')
    y = sim_word(x)
    #print(type(clean_txt))
    vocabulary(y)
    #print(x)
main()

