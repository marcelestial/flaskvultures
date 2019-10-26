#Import from peewee
from peewee import *

#Connect to the SQLite database
db = SqliteDatabase('vultures.db')

#Define what a 'Vulture' is
class Vulture(Model):
  #These are all the fields it has
  speciesId = IntegerField(primary_key=True)
  speciesName = TextField()
  description = TextField()

  class Meta:
    #data is coming from vultures.db
    database = db
    #and it's in the table called 'Vultures'
    db_table = 'Vultures'
