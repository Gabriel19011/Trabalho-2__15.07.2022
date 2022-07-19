import json
from random import random
from dao.Cliente import Cliente


class ManipulaDao:
    def __init__(self, filename: str = "data.json") -> None:
        self.__filename = filename   


    def __loadFile(self) -> list:
        """Retorna uma lista de estudantes"""
        # self.x =__filename
        file = open(self.__filename, "r", encoding='utf-8')
        data = file.read()
        return json.loads(data)
    
    def __saveFile(self, data: list):
        """Salva a lista de estudantes"""
        newData = []
        for c in data:
            n = {}
            for chave, valor in c.__dict__.items():
                chave = chave.replace('_Cliente__', '')
                n[chave] = valor
            
            newData.append(n)

        
        file = open(self.__filename, "w+", encoding='utf-8')
        data = json.dumps(newData)
        file.write(data)
        file.close()

    def adicionar(self, cliente: Cliente) -> Cliente:
        data = self.selecionarTodos()
        cliente.setId(int(round(random() * 10000, 0)))
        data.append(cliente)
        self.__saveFile(data)

        return cliente

    def editar(self, c: Cliente) -> None:
        data = self.selecionarTodos()

        for e in data:
            if e.getId() == c.getId():
                data.remove(e)
                c.setId(c.getId())
                data.append(c)
                self.__saveFile(data)
                break

            # self.__saveFile(data)

    def deletar(self, id: int) -> None:
        # data = self.__loadFile()
        data = self.selecionarTodos()
        for e in data:
            if e.getId() == id:
                data.remove(e)
                break
        self.__saveFile(data)

    def selecionar(self, id: int) -> Cliente:
        data = self.__loadFile()
        for e in data:
            if e['id'] == id:
                return Cliente(e['nome'], e['dataNascimento'], e['cpf'],e['placa'], e['modelo'], e['endereco'], e['id'])
        return None

    def selecionarTodos(self) -> list:
        data = self.__loadFile()
        clientes=[]
        for e in data:
            c = Cliente(e['nome'], e['dataNascimento'], e['cpf'],
                    e['placa'], e['modelo'], e['endereco'], e['id'])
            clientes.append(c)
        return clientes

      