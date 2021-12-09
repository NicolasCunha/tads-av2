#### The following content is written in brazilian portuguese. If there is any need to understand this content in another language (english), please contact me via [e-mail](mailto:nicolascunha17@gmai.com) or [LinkedIn](https://www.linkedin.com/in/nicolasfcunha/).

### Avaliação 2 da matéria "Desenvolvimento de Sistemas em Python".

Relação escolhida:
- "Pessoa (nome, cpf, email) , Disciplina (nome, carga horária, ementa), EstudanteDaDisciplina (semestre, pessoa, disciplina, media final, frequencia)"

O projeto está estruturado da seguinte forma:

- [server.py](server.py): arquivo responsável por inicializar o servidor do Flask e criar as tabelas do banco ainda não criadas através do SQL Alchemy.
- [config.py](config.py): arquivo que contém configurações do sistema, como porta do Flask e o o diretório que o SQLAlchemy criará o arquivo do banco de dados.
- [utils](utils): módulo que contém arquivos utilitários, como o arquivo [http_utils](utils/http_utils.py) utilizada conter constantes e métodos para padronizar criação de respostas dos endpoints.
- [model](model): módulo que contém classes mapeadas como Model do SQLAlchemy, representando o banco de dados.
- [endpoint](endpoint): módulo que contém arquivos responsáveis pelo mapeamento das rotas do Flask.
- [videos](videos): pasta que contém vídeos dos testes do funcionamento das rotas. Os teste foram feitos utilizando a ferramenta [Insomnia](https://insomnia.rest/) no lugar do CURL devido ao ambiente Windows. Caso não seja possível reproduzir os vídeos no formato ".mkv", o [arquivo de descrição da pasta](videos/README.md) contém links para o YouTube com os vídeos.

A relação entre as classes deste sistema - em outras palavras, o fluxo - seria:

- Requisição é recebida em uma rota (endpoint).
- Caso a requisição seja um "GET":
  - Sistema obtém todos os registros do banco de dados referente ao contexto daquela rota. Por exemplo, caso seja "Pessoa", será retornado todas as pessoas.
    ```python
    @app.route('/pessoa', methods=['get'])
    def listar_pessoas():

      pessoas = db.session.query(Pessoa).all()
      pessoas_dict = [pessoa.to_json() for pessoa in pessoas]

      return create_response(pessoas_dict, HTTP_OK)
    ```
- Caso a requisição seja um "POST":
  - Sistema tenta criar um registro no banco de dados referente ao contexto daquela rota a partir dos valores recebidos no corpo da requisição. Por exemplo, caso seja "Disciplina", será buscado as informações como nome, ementa e carga horária. O status padrão é [HTTP_OK](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status/200), porém, ao ocorrer um erro, e retornado [HTTP_ERROR](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status/500).
    ```python
    @app.route('/disciplina', methods=['post'])
    def criar_disciplina():
        requisicao = request.get_json()

        print(requisicao)

        disciplina = Disciplina(
            nome=requisicao['nome'], carga_horaria=requisicao['carga_horaria'], ementa=requisicao['ementa'])

        resultado = {}
        resultado['status'] = HTTP_OK

        try:
            db.session.add(disciplina)
            db.session.commit()
        except Exception as ex:
            resultado['status'] = HTTP_ERR
            resultado['error'] = str(ex)

        return create_response(resultado, resultado['status'])
    ```
