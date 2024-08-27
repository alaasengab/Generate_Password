from tkinter import * 
from tkinter import messagebox
from random import randint, choice, shuffle
# import pyperclip optional if you want the password to be copied automatically 
#---------------Generate Passowrd Description -----------------
"""This Python application generates strong, 
random passwords based on user-specified criteria. 
Users can enter their email address to receive the generated password."""


#---------------Functions-----------------------------------

#---------------Generate Password----------------------------

def generate_password():
    
    #initiating variables 
    letters = list(map(chr,range(97,123))) 
    numbers =[]
    for i in range(11):
        numbers.append(str(i))
    symbols = ['!', '@', '#', '$', "%", "^", "&", '*', '(', ')', "+","-" ,"="]

    num_letters = randint(8,10)#int(input("how many numbers of letters"))
    num_symbols=  randint(2,4)#int(input("how many numbers of sybmols"))
    num_numbers = randint(2,4) #int(input("how many numbers of numbers"))


    #using comprehension instead of for loop because it is shorter and more readable 
    password_letters= [choice(letters) for _ in range(num_letters) ]
    password_symbols= [choice(symbols) for _ in range(num_symbols)]
    password_numbers=[choice(numbers) for _ in range (num_numbers)]

    password_list= password_letters + password_symbols + password_numbers
    #shuffle password from random 
    shuffle(password_list)

    #display password as a string 
    # password=""
    # for char in password_list:
    #     password += char
    password="".join(password_list)
    password_entry.insert(END,password)
    
    #print(password)


#---------------Save Password ----------------------------------

def delete(entry):
    entry.delete(0,END)
    
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    #validate that the entry is valid 
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ooops", message="Please don't leave any field empty!")
    else: 
    #messagebox.showinfo(title="Title", message="Message")
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email: {email} \n Password: {password} \nIs it okay to save?" )
        if is_ok: 
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} || {email} || {password} \n")
                delete(website_entry)
                delete(password_entry)
            


#-------------------------------UI Setup -----------------------
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

#Canvas Picture 
canvas = Canvas(width=200, height=200,bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
print(type(logo_img))
canvas.create_image(100,100,image= logo_img)
canvas.grid(column=1, row=0)

#------------------- Labels------------------- 
# website label 
website_label = Label(text="Website:", bg="white")
website_label.grid(column=0,row=1)
username_label = Label(text="Email/Username:", bg="white")
username_label.grid(column=0,row=2)
password_label = Label(text="Password:", bg="white")
password_label.grid(column=0,row=3)

#Entires 
website_entry = Entry(width=37, highlightbackground="white")
website_entry.grid(row=1,column=1,  columnspan=2)
website_entry.focus()
email_entry= Entry(width=37, highlightbackground="white")
email_entry.grid(row=2,column=1,  columnspan=2)
email_entry.insert(END,"alaaeldin.sengab@gmail.com")
password_entry= Entry(width=20, highlightbackground="white")
password_entry.grid(row=3,column=1)

#Buttons 
generate_button = Button(text="Generate Password",highlightbackground="white",command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", highlightbackground="white", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
