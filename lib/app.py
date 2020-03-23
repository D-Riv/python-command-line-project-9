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

in_book = True

while in_book == True: 


  ui = """
  Welcome to Your Contact Book 

  1. Add new contacts
  2. View contact list
  3. Search contact list
  4. Update contact list 
  5. Delete contact list
  6. Exit application
  """
  print(ui)

  def add_contact():
    add_contact = Contact(entrydate=input("Enter entry date: "),  name=input("Enter contact name: "), address=input("Enter contact adddress: "), phone=input("Enter contact phone number: "))
    add_contact.save()
    print(ui)
    # user_res = int(input("Select: "))
    # if user_res == 1: 
    #   add_contact()
    # elif user_res == 2: 
    #   view_contact()
    # elif user_res == 3: 
    #   search_contact()

  def view_contact():
    contact_list = Contact.select()
    for contact in list(contact_list): 
      print(f"\n Entry Date: {contact.entrydate}\n Contact Name: {contact.name}\n Contact Address: {contact.address}\n Contact Phone Number: {contact.phone}\n")
    # my_table = db.read_sql('select * from contact', connection)

  def search_contact():
    user_input = str(input("""
    Search for a Specific Contact
    Search by date, name, address, or phone number
    Enter here: """))

    search = Contact.get(Contact.name == user_input)
    search2 = Contact.get(Contact.entrydate == user_input)
    search3 = Contact.get(Contact.address == user_input)
    search4 = Contact.get(Contact.phone == user_input)

    if search:
      print(f"\n Entry Date: {search.entrydate}\n Contact Name: {search.name}\n Contact Address: {search. address}\n Contact Phone Number: {search.phone}")
    elif search2:
      print(f"\n Entry Date: {search.entrydate}\n Contact Name: {search.name}\n Contact Address: {search. address}\n Contact Phone Number: {search.phone}")
    elif search3: 
      print(f"\n Entry Date: {search.entrydate}\n Contact Name: {search.name}\n Contact Address: {search. address}\n Contact Phone Number: {search.phone}")
    elif search4: 
      print(f"\n Entry Date: {search.entrydate}\n Contact Name: {search.name}\n Contact Address: {search. address}\n Contact Phone Number: {search.phone}")


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
