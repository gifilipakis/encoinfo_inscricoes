from random import *


class Inscrito:
    def __init__(self, nome, telefone, evento):
        self.nome = nome
        self.tel = telefone
        self.preco = int
        self.evento = evento

    def escolher_fila(self):
        x = sample(self.evento.atendente, 1)
        x[0].atender(self)


class Aluno(Inscrito):
    def __init__(self, nome, telefone, evento, universidade):
        super().__init__(nome, telefone, evento)
        self.uni = universidade


class Profissional(Inscrito):
    def __init__(self, nome, telefone, evento, empresa):
        super().__init__(nome, telefone, evento)
        self.emp = empresa


class Professor(Inscrito):
    def __init__(self, nome, telefone, evento, universidade):
        super().__init__(nome, telefone, evento)
        self.uni = universidade


class Evento:
    def __init__(self, nome, dataI, dataF, limite):
        self.nome = nome
        self.dataI = dataI
        self.dataF = dataF
        self.limite = limite
        self.inscrito = []
        self.atendente = []

    def relatorio(self):
        print('RELATÓRIO')
        precoA = 0
        precoP = 0
        precoProf = 0
        for i in self.atendente:
            alunos = 0
            professores = 0
            profissionais = 0
            for j in i.atendidos:
                if type(j) == Aluno:
                    alunos += 1
                    precoA += 50
                elif type(j) == Professor:
                    professores += 1
                    precoP += 100
                else:
                    profissionais += 1
                    precoProf += 120
            print(' Atendente:', i.nome, '- ', alunos, 'Alunos', '- ', professores, 'Professores', '- ', profissionais,
                  'Profissionais', '- ', 'Total:', alunos + professores + profissionais)
        print(' Total pago(Alunos): R$', precoA, '\n', 'Total pago(Professores): R$', precoP, '\n',
              'Total pago(Profissionais): R$',
              precoProf, '\n', 'Total pago geral: R$', precoA + precoP + precoProf)


class Atendente:
    def __init__(self, nome, evento):
        self.nome = nome
        self.evento = evento
        self.atendidos = []
        self.evento.atendente.append(self)

    def atender(self, inscrito):
        if len(self.evento.inscritos) < self.evento.limite:
            print('Bem-vindo!')
            if type(inscrito) == Aluno:
                inscrito.preco = 50
            elif type(inscrito) == Professor:
                inscrito.preco = 100
            else:
                inscrito.preco = 120
            self.evento.inscritos.append(inscrito)
            print('Sua inscrição foi realizada com sucesso! O preço pago foi R$', inscrito.preco)
        else:
            print('Sinto muito, não há mais vagas disponíveis :(')
            return self.evento.relatorio()
        self.atendidos.append(inscrito)

    def teste(self):
        nomes = ['Ana', 'João', 'Maria', 'Mario', 'João Vitor']
        universidades = ['Ulbra', 'UFT', 'Católica', 'ITOP', 'ITPAC']
        empresas = ['Empresa1', 'Empresa2', 'Empresa3']
        i = 0
        while i <= 100:
            x = sample(nomes, 1)
            y = sample(universidades, 1)
            z = sample(empresas, 1)

            a1 = Aluno(x, randint(1, 100), e1, y)
            p1 = Professor(x, randint(1, 100), e1, y)
            prof1 = Profissional(x, randint(1, 100), e1, z)

            inscrito = [a1, a1, a1, a1, a1, a1, a1, p1, p1, prof1]
            w = sample(inscrito, 1)

            w[0].escolher_fila()
            i += 1
        print(i)


e1 = Evento('ENCOINFO', '21/5', '25/5', 100)
at1 = Atendente('Ana', e1)
at2 = Atendente('Maria', e1)
at3 = Atendente('João', e1)
at1.teste()
print('')
e1.relatorio()