from tkinter import *
class Funcs():
    def Limpa_tela(self):
        self.dobra1_entry.delete(0, END)
        self.dobra2_entry.delete(0, END)
        self.dobra3_entry.delete(0, END)
        self.idade_entry.delete(0, END)
        self.altura_entry.delete(0,END)
        self.peso_entry.delete(0, END)
    def calcular_gordura_corporal(self):
        try:
            dobra1 = float(self.dobra1_entry.get())
            dobra2 = float(self.dobra2_entry.get())
            dobra3 = float(self.dobra3_entry.get())
            idade = int(self.idade_entry.get())

            soma_dobras = dobra1 + dobra2 + dobra3
            gordura_corporal = (0.29288 * soma_dobras) - (0.0005 * soma_dobras * soma_dobras) + (0.15845 * idade) - 5.76377

            self.lb_info1["text"] = "Meça as seguintes dobras cutâneas (em milímetros) com paquímetros de gordura corporal: Peitoral, Abdominal e Coxa. Densidade Corporal = 1,10938 – (0,0008267 x soma das dobras cutâneas) + (0,0000016 x quadrado da soma das dobras cutâneas) – (0,0002574 x idade)"
            self.lb_resultado["text"] = f"A porcentagem de gordura corporal é: {gordura_corporal:.2f}%"
        except ValueError:
            self.lb_resultado["text"] = "Valores inválidos"

    def Cal_imc(self):
        try:
            peso = float(self.peso_entry.get())
            altura = float(self.altura_entry.get())
            imc = peso / (altura * altura)
            result_imc = imc
            self.lb_info1[
                "text"] = "Abaixo do peso: IMC < 18,5 / Peso normal: 18,5 <= IMC < 25 / Sobrepeso: 25 <= IMC < 30 / Obesidade grau I: 30 <= IMC < 35 / Obesidade grau II: 35 <= IMC < 40 / Obesidade grau III (obesidade mórbida): IMC >= 40"
            self.lb_resultado["text"] = "Seu IMC é: " + str(result_imc)
        except ValueError:
            self.lb_resultado["text"] = "Valores inválidos"

class Application(Funcs):
    def __init__(self):
        self.root = Tk()
        self.tela()
        self.frames_da_tela()
        self.dados()
        self.Menus()

        self.root.mainloop()
    def tela(self):
        self.root.title("Canivete do Peso")
        self.root.geometry("720x560")
        self.root.configure(background='#466bdb')
        self.root.resizable(True, True)
    def frames_da_tela(self):
        self.frame1 = Frame(self.root, bd=4, bg='#bac8f2', highlightbackground='#838a9e', highlightthickness='3')
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame2 = Frame(self.root, bd=4, bg='#bac8f2', highlightbackground='#838a9e', highlightthickness='3')
        self.frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def dados(self):
        self.bt_limpar = Button(self.frame1, text="Limpar Medidas ", command=self.Limpa_tela)
        self.bt_limpar.place(relx=0.5, rely=0.03, relheight=0.2, relwidth=0.2)

        self.lb_dobra1 = Label(self.frame1, text="Dobras Peitoral", anchor="center")
        self.lb_dobra1.place(relx=0.15, rely=0.01, relheight=0.1, relwidth=0.16)

        self.dobra1_entry = Entry(self.frame1)
        self.dobra1_entry.place(relx=0.01, rely=0.11, relheight=0.1, relwidth=0.4)

        self.lb_dobra2 = Label(self.frame1, text="Dobras Abdominal", anchor="center")
        self.lb_dobra2.place(relx=0.15, rely=0.22, relheight=0.1, relwidth=0.16)

        self.dobra2_entry = Entry(self.frame1)
        self.dobra2_entry.place(relx=0.01, rely=0.32, relheight=0.1, relwidth=0.4)

        self.lb_dobra3 = Label(self.frame1, text="Dobras Coxa", anchor="center")
        self.lb_dobra3.place(relx=0.15, rely=0.44, relheight=0.1, relwidth=0.14)

        self.dobra3_entry = Entry(self.frame1)
        self.dobra3_entry.place(relx=0.01, rely=0.53, relheight=0.1, relwidth=0.4)

        self.lb_idade = Label(self.frame1, text="Idade", anchor="center")
        self.lb_idade.place(relx=0.01, rely=0.66, relheight=0.1, relwidth=0.09)

        self.idade_entry = Entry(self.frame1)
        self.idade_entry.place(relx=0.01, rely=0.76, relheight=0.1, relwidth=0.09)

        self.lb_altura = Label(self.frame1, text="altura", anchor="center")
        self.lb_altura.place(relx=0.15, rely=0.66, relheight=0.1, relwidth=0.09)

        self.altura_entry = Entry(self.frame1)
        self.altura_entry.place(relx=0.15, rely=0.76, relheight=0.1, relwidth=0.09)

        self.lb_peso = Label(self.frame1, text="Peso", anchor="center")
        self.lb_peso.place(relx=0.32, rely=0.66, relheight=0.1, relwidth=0.06)

        self.peso_entry = Entry(self.frame1)
        self.peso_entry.place(relx=0.30, rely=0.76, relheight=0.1, relwidth=0.1)

        self.lb_resultado = Label(self.frame2, text=".........")
        self.lb_resultado.place(relx=0.01, rely=0.32, relheight=0.1, relwidth=0.4)

        self.lb_info1 = Label(self.frame2)
        self.lb_info1.place(relx=0.5, rely=0.20, relheight=0.6, relwidth=0.3)
        self.lb_info1.config(wraplength=200, anchor="w")

    def Menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def Quit():
            self.root.destroy()

        menubar.add_cascade(label="Opções", menu=filemenu)
        menubar.add_cascade(label="Sobre", menu=filemenu2)
        filemenu.add_command(label="Calculo de Porcentagem de gordura corporal", command=self.calcular_gordura_corporal)
        filemenu.add_command(label="Calcular IMC", command=self.Cal_imc)
        filemenu2.add_command(label="Sair", command=Quit)

Application()