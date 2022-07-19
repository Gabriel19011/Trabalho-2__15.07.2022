from flask import redirect, render_template, request
from flask_classful import FlaskView, route
from dao import ManipulaDao
from dao import Cliente


class CacaView(FlaskView):
    dao = ManipulaDao()
    route_base = '/'

    def index(self):
        return "<br>"

    @route('/alterar/<int:id>', methods=['POST'])
    @route('/cadastrar', methods=['POST'])
    def cadastrar(self, id: int = None):
        body = dict(request.form)
        c = Cliente(body['nome'], body['dataNasc'], body['cpf'],
                    body['placa'], body['modelo'], body['endereco'])
        if id:
            c.setId(id)
            self.dao.editar(c)
        else:
            self.dao.adicionar(c)
        return redirect("/listar")

    @route('/deletar/<int:id>', methods=['GET'])
    def deletar(self, id: int):
        self.dao.deletar(id)
        return redirect("/listar")

    @route('/cadastro/<int:id>', methods=['GET'])
    @route('/cadastro', methods=['GET'])
    def form(self, id: int = None):
        if id:
            # print(self.dao.selecionar(id))
            return render_template("form.html", dados=self.dao.selecionar(id))

        return render_template("form.html")

    @route('/listar', methods=['GET'])
    def listar(self):
        return render_template("listar.html", lista=self.dao.selecionarTodos())
