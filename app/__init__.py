import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Cria a instância da aplicação Flask
app = Flask(__name__)

# Configuração da Base de Dados SQLite
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
RAIZ_PROJETO = os.path.dirname(BASE_DIR)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(RAIZ_PROJETO, 'database.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa a extensão da Base de Dados
db = SQLAlchemy(app)

# IMPORTANTE: Importar os modelos e as rotas depois de criar app e db
# Isto evita importações circulares e regista as rotas no Flask
from app import models, routes

with app.app_context():
    db.create_all()
    # Inicializa dados padrão para locais se a tabela estiver vazia
    if models.Local.query.first() is None:
        locais_iniciais = [
            models.Local(
                nome="1. Torre de Belém",
                descricao="Construída no século XVI às margens do Rio Tejo, a Torre de Belém é um dos monumentos mais emblemáticos do estilo manuelino e simboliza a era das navegações portuguesas.",
                imagem="https://thumb.wikimedia.org/wikipedia/commons/thumb/f/fa/Bel%C3%A9m_Tower_in_Lisbon%2C_Portugal.jpg/330px-Bel%C3%A9m_Tower_in_Lisbon%2C_Portugal.jpg",
                link="https://pt.wikipedia.org/wiki/Torre_de_Bel%C3%A9m"
            ),
            models.Local(
                nome="2. Castelo de São Jorge",
                descricao="Localizado numa das colinas mais altas de Lisboa, este castelo medieval oferece uma vista panorâmica incrível sobre toda a cidade e o Rio Tejo.",
                imagem="https://thumb.wikimedia.org/wikipedia/commons/thumb/1/17/Castelo_de_S%C3%A3o_Jorge_%2810251035013%29.jpg/330px-Castelo_de_S%C3%A3o_Jorge_%2810251035013%29.jpg",
                link="https://pt.wikipedia.org/wiki/Castelo_de_S%C3%A3o_Jorge"
            ),
            models.Local(
                nome="3. Bairro da Alfama",
                descricao="O bairro mais antigo de Lisboa, famoso pelas ruas estreitas, varandas com roupa a secar e pelo som do Fado a ecoar pelas tavernas.",
                imagem="https://thumb.wikimedia.org/wikipedia/commons/thumb/c/c1/Alfama%2C_Lisboa_-_2010-09-09.jpg/250px-Alfama%2C_Lisboa_-_2010-09-09.jpg",
                link="https://pt.wikipedia.org/wiki/Alfama"
            )
        ]
        db.session.bulk_save_objects(locais_iniciais)
        db.session.commit()
