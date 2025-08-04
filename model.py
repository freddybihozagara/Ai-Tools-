from AiTools import app, db

class AiTools (db.Model):
   id = db.column(db.Integer, primary_key=True)
   name = db.column(db.String, unique=True, nullable=False)
   url = db.column(db.String, unique=True, nullable=False)

   def __init__(self,name,url):
       self.name = name
       self.url = url

   def __repr__(self):
       return '<AiTools %d>' % self.id

   with app.app_context():
    db.create_all()
