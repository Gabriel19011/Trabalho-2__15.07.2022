class Cliente:
    def __init__(self, nome: str, dataNascimento: str, cpf: str, placa: str, modelo: str, endereco: str, id: int = None) -> None:
        self.__id = id
        self.__nome = nome
        self.__dataNascimento = dataNascimento
        self.__cpf = cpf
        self.__placa = placa
        self.__modelo = modelo
        self.__endereco = endereco

    def setNome(self, x: str) -> dict:
        """colocar o nome no json"""
        self.__nome = x

    def getNome(self) -> str:
        """pegar o nome do json"""
        return self.__nome

    def setCPF(self, m: str) -> dict:
        """colocar o CPF no json"""
        self.__cpf = m

    def getCPF(self) -> str:
        """pegar o CPF do json"""
        return self.__cpf

    def setdataNascimento(self, y: str) -> dict:
        """colocar o data de Nascimento no json"""
        self.__dataNascimento = y

    def getdataNascimento(self) -> str:
        """pegar o data de Nascimento do json"""
        return self.__dataNascimento

    def setPlaca(self, n: str) -> dict:
        """colocar a Placa no json"""
        self.__placa = n

    def getPlaca(self) -> str:
        """pegar a placa do json"""
        return self.__placa

    def setModelo(self, z: str) -> dict:
        """colocar o modelo no json"""
        self.__modelo = z

    def getModelo(self) -> str:
        """pegar o modelo do json"""
        return self.__modelo

    def setendereco(self, p: str) -> dict:
        """colocar o Endereço no json"""
        self.__endereco = p

    def getendereco(self) -> str:
        """pegar o Endereço do json"""
        return self.__endereco

    def setId(self, d: int) -> dict:
        """colocar o id no json"""
        self.__id = d

    def getId(self) -> int:
        """pegar o id do json"""
        return self.__id
