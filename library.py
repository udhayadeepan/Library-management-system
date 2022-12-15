from tkinter import*
from tkinter import messagebox
TotalBooks={'8100':'Python by guido','8101':'C++ ','8102':'Artifical Intelligence','8103':'Cyber Security','8104':'Electronics circuits','8105':'java by stroustrupe','8106':'Embedded system'}#list of all books in the library
AvailableBooks={'8100':'Python by guido','8101':'C++ ','8102':'Artifical Intelligence','8103':'Cyber Security','8104':'Electronics circuits','8105':'java by stroustrupe','8106':'Embedded system'}#list of currently available books in the libtrary
WithdrawnBooks={} 
win=Tk()
win.title('library management')
win.geometry('255x175')
win.resizable(False,False)
Label(win,text='LIBRARY MANAGEMENT',bg='light green').pack(fill=X)
win.configure(bg='light blue')
a=Label(win,text='WELCOME',bg='light blue') 
a.pack(pady=50)

f1=Frame(win)
add_frame=Frame(win)
list_frame=Frame(win)
mylist=Listbox(list_frame)
wd_frame=Frame(win)
re_frame=Frame(win)
sw_frame=Frame(win)
scroll=Scrollbar(list_frame)


def add():
      add_frame.pack(fill='both')
      f1.pack_forget()
      
      Label(add_frame,text='Adding a new book to the library').grid(row=0,column=1)
      Label(add_frame,text='Book Name').grid(row=2,column=0)
      Name=Entry(add_frame)
      Name.grid(row=2,column=1)
      Label(add_frame,text='Book ID').grid(row=1,column=0)
      Id=Entry(add_frame)
      Id.grid(row=1,column=1)
      
      def Add_book():
            if len(Id.get())!=0 and len(Name.get())!=0:
                  TotalBooks[Name.get()]=Id.get()#add name and ID of the book to dictionary
                  AvailableBooks[Id.get()]=Name.get()
            
                  print('Book successfully added')
                  Name.delete(0,END)
                  Id.delete(0,END)
                  temp.configure(text="Book Added to Library")
            #messagebox.showinfo('message','Book successfully added to the library')
            else:
                    temp.configure(text="ERROR")
      Button(add_frame,text='Add book',command=Add_book).grid(row=3,column=1)
      temp=Label(add_frame)
      temp.grid(row=4,column=1,sticky="nsew")
      
def available_books():
            f1.pack_forget()
            list_frame.pack(fill='both')
            
            #mylist=Listbox(list_frame,yscrollcommand=scroll.set)
            #mylist.pack(fill="both")
            #scroll.pack(side='right',fill=Y)
            #scroll.config(command=mylist.yview)
            
            
            #mylist.delete(0,END)
            #mylist.pack_forget()
            mylist.pack(fill='both')
            #str="LIST OF AVAILABLE BOOKS"
           # mylist.insert(END,str)
            str="-------------------------------------------"
            mylist.insert(END,str)
            str="ID      NAME"
            mylist.insert(END,str)
            str="-------------------------------------------"
            mylist.insert(END,str)
            for i,j in AvailableBooks.items():
                  st=i+"-"+j
                  mylist.insert(END,st)
            
      
def withdraw():
         wd_frame.pack(fill=BOTH)
         f1.pack_forget()
         Label(wd_frame,text='Withdraw a Book').grid(row=0,column=1)
         Label(wd_frame,text='Book ID').grid(row=1,column=0)
         Label(wd_frame,text='Student Name').grid(row=2,column=0)
         a=Entry(wd_frame)
         a.grid(row=1,column=1)
         b=Entry(wd_frame)
         b.grid(row=2,column=1)
         def wdbook():
                  BookID=a.get()

                  
                  if BookID in AvailableBooks:#check the book is currently available 
                        StudentName=b.get()
                        if len(StudentName)==0:
                            #m=messagebox.askretrycancel('warning','student name cannot be empty')
                            temp.configure(text='student name cannot be empty')
                            #if m==False:
                               #restore()
                                  
                        else:
                            if StudentName in WithdrawnBooks:#check if student already a member
                                  if len(WithdrawnBooks[StudentName])<2:#check whether the student has already taken 2 books
                                        WithdrawnBooks[StudentName].append(BookID)
                                        AvailableBooks.pop(BookID)#remove the book from available list
                                        print("'",TotalBooks[BookID],"'",'book is given to',StudentName)
                                  else:
                                        messagebox.showinfo('warning','Already 2 books taken by the student')
                                        temp.configure(text='WARNING:Already 2 books taken by the student')
                            else:
                                  WithdrawnBooks[StudentName]=[]#if student new to library ,a new profile is created for that student
                                  WithdrawnBooks[StudentName].append(BookID)
                                  AvailableBooks.pop(BookID)
                                  w=("'",TotalBooks[BookID],"'", 'book is given to', StudentName)
                                  messagebox.showinfo('INFO',w)
                  else:
                       #messagebox.showinfo('message','currently the book is unavailable')
                       temp.configure(text="currently the book is unavailable")
               
         Button(wd_frame,text='withdraw',command=wdbook).grid(row=3,column=1)
         temp=Label(wd_frame)
         temp.grid(row=4,column=1,sticky="nsew")
def re():
      re_frame.pack(fill=BOTH)
      f1.pack_forget()
      Label(re_frame,text='Return a Book').grid(row=0,column=1)
      Label(re_frame,text='Book ID').grid(row=1,column=0)
      a=Entry(re_frame)
      a.grid(row=1,column=1)
      def ret():
            BookID=a.get()
            if BookID not in TotalBooks.keys():
                  messagebox.showerror('error','Wrong BookID')
            for i in WithdrawnBooks.values():
                  if BookID in i:
                        i.remove(BookID)#remove the book from withdrawn list
                        AvailableBooks[BookID]=TotalBooks[BookID]#add the book back to availablebooks
                        m=("'",TotalBooks[BookID],"'",' book is returned.')
                        messagebox.showinfo('INFO',m)
                        
                  else:
                        messagebox.showerror('error','Invalid BookID')
            
      Button(re_frame,text='Return',command=ret).grid(row=3,column=1)
def stu_wd():
      sw_frame.pack(fill=BOTH)
      f1.pack_forget()
      Label(sw_frame,text='Book withdrawn by Student').grid(row=0,column=1)
      Label(sw_frame,text='Student Name').grid(row=1,column=0)
      a=Entry(sw_frame)
      a.grid(row=1,column=1)
      def withdraw():
            StudentName=a.get()
            l=Listbox(sw_frame)
            l.grid(row=3,column=1,sticky='nsew')
            if StudentName in WithdrawnBooks:#whether the student taken any book
                  if len(WithdrawnBooks[StudentName])==0:
                        messagebox.showinfo('INFO','No books were taken by the student')
                  else:
                        print('BookID  -  BookName')
                        for i in WithdrawnBooks[StudentName]:
                              l.insert(END,TotalBooks[i])

            else:
                  print('The student doesn\'t taken any books yet')
      Button(sw_frame,text='Show Detail',command=withdraw).grid(row=2,column=1)
      
      
def restore():
      f1.pack(fill='both')
      a.pack_forget()
      list_frame.pack_forget()
      mylist.forget()
      mylist.delete(1,len(AvailableBooks)+5)
      scroll.pack_forget()
      add_frame.pack_forget()
      wd_frame.pack_forget()
      re_frame.pack_forget()
      sw_frame.pack_forget()
      b1=Button(f1,text='Add a new book',command=add).pack(fill=X)
      b2=Button(f1,text='List of available books',command=available_books).pack(fill=X)
      b3=Button(f1,text='withdraw a book',command=withdraw).pack(fill=X)
      b4=Button(f1,text='Return a book',command=re).pack(fill=X)
      b5=Button(f1,text='Book withdrawn by student',command=stu_wd).pack(fill=X)

Button(win,text='Home',command=restore,bg='yellow').pack(side='bottom',fill=X)
win.mainloop()

