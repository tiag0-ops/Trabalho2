from app import db

# Modelo da tabela de Locais Turísticos
class Local(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    imagem = db.Column(db.String(300), nullable=False)
    link = db.Column(db.String(300), nullable=False)

# Modelo da tabela de Restaurantes
class Restaurante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    zona = db.Column(db.String(100), nullable=False)
    especialidade = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.String(20), nullable=False) # Barato, Médio, Caro
