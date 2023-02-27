#online library management system based on oops
# create library class
# display book
# lend book -(who owns the book if not present in libary
# add book
# return book
# create a main function and run an infinite while loop asking users for their input

######ctrl+d shortcut
class Library:
  def __init__(self,list,name):
    self.booksList=list
    self.name=name
    self.lendDict={}
  def displayBook(self):
    print(f"we have following books in {self.name} lib")
    for book in self.booksList:
      print(book)
  def lendBook(self,user,book):
    if book not in self.lendDict.keys():
      self.lendDict.update({book:user})
      print("Lender-Book database has been updated.\n You can take the book now")
    else:
      print(f"Book is already being used by {self.lendDict[book]}")
  def addBook(self,book):
    self.booksList.append(book)
    print("Thank you. we greatly appreciate your donation")
  def returnBook(self,book):
      if book in self.booksList:
          self.booksList.remove(book)
          print(f"Thank you for returning {book} book.")
      else:
          print("Either this book is not belongs to this library or\nYou are returning wrong book,please kindly check book name")

if __name__=='__main__':
  pritam=Library(['python','rich dad poor dad','Harry Potter'],'prit')

  while(True):
    print(f'Welcome to the {pritam.name} library.\n')
    print("1.Display book")
    print("2.lend a book")
    print("3.Donate a book")
    print("4.Return book")
    user_choice = input("Enter your choice to continue: ")
    if user_choice=='1':
      pritam.displayBook()
    elif user_choice=='2':
      book=input('Enter the name of book you want to lend: ')
      if book in pritam.booksList:
          user=input('Enter your name: ')
          pritam.lendBook(user,book)
      else:
          print(f"sorry but {book} is not available in our library ")
    elif user_choice=='3':
      book=input('Enter the name of the book you want to add: ')
      pritam.addBook(book)
    elif user_choice=='4':
      book=input('Enter the name of the book you want to return: ')
      pritam.returnBook(book)
    else:
      print("Not a valid option")

    print('Press q to quit and c to continue')
    user_choice2=""
    while (user_choice2 !='q' and user_choice2 !='c'):
      user_choice2=input()
      if user_choice2=='q':
        exit()
      elif user_choice2=='c':
        continue
      else:
          print('Not a valid option')