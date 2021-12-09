from config import app, db, FLASK_PORT

from model import *

from endpoint import *

# cria todas tabelas ainda nao criadas
# como os modelos foram importados acima, ja estao mapeados e as tabelas serao criadas
db.create_all()
app.run(port = FLASK_PORT, debug=True)

