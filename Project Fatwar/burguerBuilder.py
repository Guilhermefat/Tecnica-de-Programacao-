from abc import ABC, abstractmethod


class fatec(ABC):
    @abstractmethod
    def entrar(self,pessoa):
        pass


class Aluno(fatec):
    def entrar(self, pessoa):
        return f"O {pessoa}  Pessoa da Fatec "

class Fabricafatec:
    def criar_pessoafat(self,cargo):
        if cargo=="Aluno":
            return Aluno()
 
fabrica_pessoafat = Fabricafatec()
print("\n-------------------Bem-Vindo-a-Fatec-----------------")
f= str(input("Digite S para se-cadastrar ou digite Q para sair: "))
if f == "Q":
    print("\nfinalizando atendimento...\n")
    exit()
while f!="Q":
    (str(input("\nInforme o seu nome: ")))
    f= str(input("\nDigite S para se-cadastrar novamente ou digite Q para sair: \n"))


class burguerfat:
    def __init__(self):
        self.pao = None
        self.carne = None
        self.queijo = None
        self.vegetal = None
        self.bebida = None

    def __str__(self):

        return f"\nSeu lanche esta Pronto:\n\nPão: {self.pao}\nCarne: {self.carne}\nQueijo: {self.queijo}\nVegetal: {self.vegetal}\nBebidas: {self.bebida}\n \nBom Apetite!!!\n"
      
class burguerBuilder:
    def __init__(self) -> None:
        self.burguer = burguerfat()
  
    def build_pao(self):
    
        print("\n======  Escolha seu Pão  ======= \n")
        print("Digite GS para escolher Granola Salgada ")
        print("Digite IB para escolher Italiano Branco ")
        print("Digite  G para escolher 9 Grãos \n")
  
        meat_statement = str(input("Digite qual opção deseja: "))
        if meat_statement ==   "GS":
            self.burguer.pao= "Granola Salgada"
        elif meat_statement == "IB":
            self.burguer.pao= "Italiano Branco"
        elif meat_statement == "G":
            self.burguer.pao = "9 Grãos"
        else:
            print("Não temos esse Pão\n")
    
    def build_carne(self):
      
        print("\n======  Escolha sua Carne  ======= \n")
        print("Digite FR para escolher Frango Ranch ")
        print("Digite SC para escolher Steak Churrasco ")
        print("Digite CS para escolher Carne Supreme ")
       
      

        bread_statement = str(input("\nDigite qual opção deseja: "))
        if bread_statement ==  "FR":
            self.burguer.carne= "Frango Ranch"
        elif bread_statement == "SC":
            self.burguer.carne = "Steak Churrasco"
        elif bread_statement == "CS":
            self.burguer.carne = "Carne Supreme"
        else:
            print("Não temos esse Carne\n")

    def build_queijo(self):
        
        print("\n======  Escolha seu Queijo  ======= \n")
        print("Digite QM para escolher Queijo Mussarela ")
        print("Digite S para escolher Suíço ")
        print("Digite C para escolher Cheddar ")
 

        bread_statement = str(input("\nDigite qual opção deseja: "))
        if bread_statement ==  "QM":
            self.burguer.queijo= "Queijo Mussarela"
        elif bread_statement == "S":
            self.burguer.queijo = "Suíço"
        elif bread_statement == "C":
            self.burguer.queijo = "Cheddar"
        else:
            print("Não temos esse Queijo\n")

    def build_vegetal(self):
        print("\n======  Escolha seu Vegetal  ======= \n")
        print("Digite CR para escolher Cebola Roxa ")
        print("Digite A para escolher Azeitonas ")
        print("Digite P para escolher Pimentão")

        bread_statement = str(input("\nDigite qual opção deseja: "))
        if bread_statement ==  "CR":
            self.burguer.vegetal= "Cebola Roxa"
        elif bread_statement == "A":
            self.burguer.vegetal = "Azeitonas"
        elif bread_statement == "P":
            self.burguer.vegetal = "Pimentão"
        else:
            print("Não temos esse Vegetal\n")

    def build_bebida(self):
        print("\n======  Escolha sua Bebida  ======= \n")
        print("Digite R para escolher Refrigerante ")
        print("Digite NO para escolher Natural One ")
        print("Digite A para escolher Água ")
 


        bread_statement = str(input("\nDigite qual opção deseja: "))
        if bread_statement ==  "R":
            self.burguer.bebida= "Refrigerante"
        elif bread_statement == "NO":
            self.burguer.bebida = "Natural One"
        elif bread_statement == "A":
            self.burguer.bebida = "Água"
        else:
            print("Não temos esse Vegetal\n")


    def get_burguer(self):
        return self.burguer

class Pessoa:
    def __init__(self, builder):
        self.builder = builder

    def construct_burguer(self):
        self.builder.build_pao()
        self.builder.build_carne()
        self.builder.build_queijo()
        self.builder.build_vegetal()
        self.builder.build_bebida()


print("\nDigite S para Sair")
print("Digite F para ficar na FatWay\n")



a = str(input("Você deseja sair ou comer um lanche na Fatway?: \n"))

if a == "S":
    print("Você está saindo da FatWay")
else:
    print("\nIniciando atendimento...\n")
    hamburguer = burguerBuilder()
    pessoa = Pessoa(hamburguer)
    pessoa.construct_burguer() 
    lanche = hamburguer.get_burguer()
    print(lanche)


