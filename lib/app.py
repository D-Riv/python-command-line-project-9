from peewee import *

db = PostgresqlDatabase('contactbook', user='DRivera', password='',
                        host='localhost', port=5432)

db.connect()



ui = """
1. Add new contacts
2. View contact list
3. Search contact list
4. Update contact list 
5. Delete contaact list
6. Exit application
"""