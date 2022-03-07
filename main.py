from clean_text import clean_txt
from check_dict import check_dict
from topic import topic as tp
import tkinter as tk
from tkinter import font as tkfont
from tkinter import filedialog as filed
import draw_plot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# if __name__ == '__main__':
#      input_text = input('Link:')
#      x = clean_txt(input_text)
#      y = check_dict(x)
#      tp(y)

# #inicjalizacja ramek
class Default(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        top = tk.Frame(self)
        self.title("Praca inżynierska")
        #self.geometry("1000x500")
        top.pack(side = "top", fill="none", expand = True)
        top.grid_rowconfigure(0, minsize = 800, weight = 1)
        top.grid_columnconfigure(0, minsize = 800, weight = 1)


        self.frames={}
        for F in (Mainp, Resultp):
            frame = F(top, self)
            self.frames[F] = frame
            self.frames[F].grid(row=0, column=0, sticky = "nsew")
        self.show_frame(Mainp)

    #uruchamianie poszczególnych okienek

    def show_frame(self, cont, temp=()):
        frame = self.frames[cont]

        if type(frame) is Resultp:
            frame.plot(temp)
        frame.tkraise()

#ramka początkowa
class Mainp(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        button_font = tkfont.Font(family="Times", size="14", weight="bold")
        #inicjowane widgety

        #####################################################
        self.address = tk.Entry(self, exportselection=0, width = 80)
        self.address.place(x=140, y=200)
        #########################################################
        self.add_txt = tk.Button(self, text="Dodaj plik tekstowy",
                                  command=self.browse_files,
                                  width=25,
                                  bg = "#D3C48B",
                                  fg="black",
                                  font=button_font)
        self.add_txt.place(x=250, y = 300)
        ###########################################################
        self.next_win = tk.Button(self, text="Wyszukaj",
                                  command=lambda:self.check_if_valid(),
                                  width=25,
                                  bg = "#D3C48B",
                                  fg="black",
                                  font=button_font)
        self.next_win.place(x = 250, y = 400)
        ###########################################################
        self.placeholder = tk.Label(self, text="")
        self.placeholder.place(x=350, y=500)
        ###########################################################
        self.info = tk.Label(self, text="Podaj link do artykułu lub wybierz plik tekstowy:")
        self.info.place(x=250, y=100)
        ##########################################################
    #funkcje buttonów
    def change_state(self):
        self.address.insert(0, self.filename)
    def show_results(self):

         txt = clean_txt(self.address.get())
         temp = check_dict(txt)
         text_in_dict = temp[0]
         skipped = temp[1]
         similarity = tp(text_in_dict)
         temp2 = (similarity, skipped)
         self.controller.show_frame(Resultp, temp2)

    def check_if_valid(self):
        if self.address.get().startswith('http') or self.address.get().endswith('.odt') or self.address.get().endswith('.docx'):
            self.show_results()
        else: self.placeholder["text"] = "Podano złe dane"

    def browse_files(self):
        self.filename = filed.askopenfilename(initialdir="/",
                                         title="Wybierz plik...",
                                         filetypes=(
                                             ("Pliki ODT", "*.odt*"),
                                            ("Pliki DOCX", "*.docx*")
                                         ))
        self.change_state()
#ramka wynikowa
class Resultp(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.parent = parent
        button_font = tkfont.Font(family="Times", size="14", weight="bold")


        #inicjowane widgety
        # self.placeholder = tk.Label(self, text=text_var)
        # self.placeholder.place(x = 550, y = 100)

        back_win = tk.Button(self, text="Wykonaj ponownie",
                                   command=lambda: controller.show_frame(Mainp),
                                   width=20,
                                   bg = "#D3C48B",
                                   fg="black",
                                   font=button_font)
        back_win.place(x = 550, y = 200)

        exitb = tk.Button(self, text="Zakończ",
                               command=lambda: app.destroy(),
                               width=20,
                               bg = "#D3C48B",
                               fg = "black",
                               font = button_font)
        exitb.place(x = 550, y = 400)

    #wyświetlanie wykresu
    def plot(self, temp):
        if temp is not None:
            result = draw_plot.draw_plot(temp)
            fig = result[0]
            canvas = FigureCanvasTkAgg(fig)
            canvas.get_tk_widget().place(x = 20, y = 20)
            canvas.draw()
            text_var = "Pominięto {} słów z wprowadzonego tekstu.".format(result[1])
            self.placeholder = tk.Label(self, text=text_var)
            self.placeholder.place(x = 550, y = 100)
        else:
            self.placeholder.configure(text="Wystąpił błąd")

app = Default()
app.mainloop()


