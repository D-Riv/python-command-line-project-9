from peewee import *
from datetime import date
import argparse

db = PostgresqlDatabase('contactbook', user='DRivera', password='',
                        host='localhost', port=5432)



class BasesModel(Model): 
  class Meta: 
    database = db

class Contact(BasesModel):
  entrydate = CharField()
  name = CharField()
  address = CharField()
  phone = CharField()


db.connect()
db.drop_tables([Contact])
db.create_tables([Contact])

# contact = Contact(entrydate=date(2020, 3, 23), name="Dennis", address="12250 Pinyon lane", p)
# contact.save()


parser = argparse.ArgumentParser(description="Save a collection of contacts")
parser.add_argument("-c")
args = parser.parse_args()

if __name__ == '__main__':
    args = parser.parse_args()

ui = """
Welcome to Your Contact Book 

1. Add new contacts
2. View contact list
3. Search contact list
4. Update contact list 
5. Delete contaact list
6. Exit application
"""
print(ui)

def add_contact():
  add_contact = Contact(entrydate=input("Enter entry date: "),  name=input("Enter contact name: "), address=input("Enter contact adddress: "), phone=input("Enter contact phone number: "))
  add_contact.save()

def view_contact():
  contact_list = Contact.select().where(Contact.name)
  print(contact_list[0].name)
  # my_table = db.read_sql('select * from contact', connection)

def search_contact():
  user_input = input("""
  Search for a Specific Contact
  Search by date, name, address, or phone number
  Enter here: 
  """)

  search = Contact.get(Contact.name == user_input)
  print(search.name)


user_res = int(input("Select: "))
if user_res == 1: 
  add_contact()
elif user_res == 2: 
  view_contact()
elif user_res == 3: 
  search_contact()
# elif user-res == 4: 
#   update-contact()
# elif user-res == 5: 
#   remove-contact()
# elif user-res == 6: 
#   close-contact()
# else :
#   print("Not an option sorry")
