from peewee import *
from datetime import date

db = PostgresqlDatabase('contactbook', user='DRivera', password='',
                        host='localhost', port=5432)



class BasesModel(Model): 
  class Meta: 
    database = db

class Contact(BasesModel):
  entrydate = DateField()
  name = CharField()


db.connect()
db.drop_tables([Contact])
db.create_tables([Contact])

contact = Contact(entrydate=date(2020, 3, 23), name="Dennis")
contact.save()






ui = """
1. Add new contacts
2. View contact list
3. Search contact list
4. Update contact list 
5. Delete contaact list
6. Exit application
"""