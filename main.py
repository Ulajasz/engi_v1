from clean_text import clean_txt
from check_dict import check_dict
from topic import topic as tp
import tkinter as tk
from tkinter import font as tkfont
from tkinter import filedialog as filed
from gensim.models import Word2Vec


if __name__ == '__main__':
     input_text = input('Link:')
     x = clean_txt(input_text)
     y = check_dict(x)
     tp(y)

# #inicjalizacja ramek
# class Default(tk.Tk):
#
#     def __init__(self, *args, **kwargs):
#         tk.Tk.__init__(self, *args, **kwargs)
#         top = tk.Frame(self)
#         self.title("Praca inżynierska")
#         #self.geometry("1000x500")
#         top.pack(side = "top", fill="none", expand = True)
#         top.grid_rowconfigure(0, minsize = 400, weight = 1)
#         top.grid_columnconfigure(0, minsize = 600, weight = 1)
#
#         self.frames={}
#         for F in (Mainp, Resultp):
#             frame = F(top, self)
#             self.frames[F] = frame
#             self.frames[F].grid(row=0, column=0, sticky = "nsew")
#         self.show_frame(Mainp)
#
#     #uruchamianie poszczególnych okienek
#     def show_frame(self, cont, most_frq = []):
#         frame = self.frames[cont]
#         #to chyba zmienić na wykres
#         # if type(frame) is Resultp:
#         #      frame.draw(most_frq)
#         #frame.pack(fill="both", expand=1)
#         frame.tkraise()
#
# #ramka początkowa
# class Mainp(tk.Frame):
#
#     def __init__(self, parent, controller): #, height, width, bg):
#         self.controller = controller
#         tk.Frame.__init__(self, parent)
#         button_font = tkfont.Font(family="Times", size="16", weight="bold")
#         #inicjowane widgety
#         #TU DAJ NA ŚRODEK I JAKO PLACEHOLDER PUSTE OKNO DLA ŚCIEŻKI
#         add_txt = tk.Button(self, text="Dodaj plik tekstowy",
#                                   command=self.browse_files,
#                                   width=25,
#                                   bg = "#196F3D",
#                                   fg="#E9F7EF",
#                                   font=button_font)
#         add_txt.place(x=300, y = 30)
#         #DODAĆ DLA LINKA HTTP!!!!!!
#
#         self.next_win = tk.Button(self, text="Wyszukaj",
#                                   command=lambda: self.show_results(),
#                                   state="disabled",
#                                   width=25,
#                                   bg = "#196F3D",
#                                   fg="#E9F7EF",
#                                   font=button_font)
#         self.next_win.place(x = 300, y = 100)
#
#         #MOZE SIE PRZYDA
#         self.filename = None
#         self.placeholder = tk.Label(self, text="Nie wybrano pliku")
#         self.placeholder.place(x = 50, y = 50)
#
#     #funkcje buttonów
#     def change_state(self):
#         self.placeholder["text"] = "mam plik"
#         self.next_win["state"] = "normal"
#     def browse_files(self):
#         self.filename = filed.askopenfilename(initialdir="/",
#                                          title="Wybierz plik...",
#                                          filetypes=(
#                                              ("Pliki ODT", "*.odt*"),
#                                             ("Pliki DOCX", "*.docx*")
#                                          ))
#         self.change_state()
#
#     def show_results(self):
#
#          txt = clean_txt(self.filename)
#          most_frq = sim_word(txt)
#          self.controller.show_frame(Resultp, most_frq)
#
# #ramka wynikowa
# class Resultp(tk.Frame):
#     def __init__(self, parent, controller): #, height, width, bg):
#         tk.Frame.__init__(self, parent)
#         self.parent = parent
#         button_font = tkfont.Font(family="Times", size="16", weight="bold")
#
#         #inicjowane widgety
#         self.placeholder = tk.Label(self, text="jestem")
#         self.placeholder.place(x = 50, y = 50)
#
#         back_win = tk.Button(self, text="Wykonaj ponownie",
#                                    command=lambda: controller.show_frame(Mainp),
#                                    width=25,
#                                    bg = "#196F3D",
#                                    fg="#E9F7EF",
#                                    font=button_font)
#         back_win.place(x = 300, y = 30)
#
#         exitb = tk.Button(self, text="Zakończ",
#                                command=lambda: app.destroy(),
#                                width=25,
#                                bg = "#196F3D",
#                                fg = "#E9F7EF",
#                                font = button_font)
#         exitb.place(x = 300, y = 100)
#         #if most_frq is not None:
#          #   self.placeholder.configure(text="dostałem wynik")
#     #wyświetlanie obrazu
#     #def draw(self, most_frq):
#         #model = Word2Vec.load('wiki.word2vec.model')
#         #
#             # img = Image.open(img_name)
#             # img1 = ImageTk.PhotoImage(img)
#             # self.placeholder.configure(image=img1, height = 800, width = 800)
#             # self.placeholder.image = img1
#
#
# app = Default()
# app.mainloop()


