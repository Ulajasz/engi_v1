from clean_text import clean_txt
#from sim_word import sim_word

def main():
    input_text = input('Link:')
    print(clean_txt(input_text))

    #word = input('Słowo do sima: ')
    #print(sim_word(clean_txt, word))

main()