


from tkinter import *
import tkinter.ttk as ttk
from tkinter.messagebox import askyesno, showerror, showinfo
from BL.main_bl import *


def message_form(data_dict, success=True):
    Message_list = []

    if not success:
        for field, err in data_dict.items():

            Message_list.append(f'{err}')

        showerror('Error!', '\n'.join(Message_list))

    else:
        for field, msg in data_dict.items():
            Message_list.append(f'{msg}')

        showinfo('Success!', '\n'.join(Message_list))


def teacher_registration_form():
 
    def back_btn_onclick():
        form.quit()
        form.destroy()

    def done_btn_onclick():

        firstname = firstname_var.get()
        lastname = lastname_var.get()
        username = username_var.get()
        password = password_var.get()
        email = email_var.get()

        teacher = {
            'firstname' : firstname,
            'lastname' : lastname,
            'username' : username,
            'password' : password,
            'email' : email
        }

        result = save_person(type='teacher', person=teacher)

        if not result['success']:
            message_form(result['error_msg'], success=False)

            if 'firstname' in result['error_msg']:
                firstname_var.set('*** only lowercase letters ***')
            
            if 'lastname' in result['error_msg']:
                lastname_var.set('*** only lowercase letters ***')

            if 'username' in result['error_msg']:
                username_var.set('*** only alphabet or digits ***')

            if 'password' in result['error_msg']:
                password_var.set('*** 8 characters including alphabet, digits or underscore ***')

            if 'email' in result['error_msg']:
                email_var.set('')

        else:
            
            message_form(result['success_msg'], success=True)
            back_btn_onclick()

    # region form
    form = Toplevel()

    #region variable
    firstname_var = StringVar()
    lastname_var = StringVar()
    username_var = StringVar()
    password_var = StringVar()
    email_var = StringVar()
    #endregion

    # region form setting
    form.title('Student Management')
    app_icon = PhotoImage(file=r'UI\source\icon.png')
    form.iconphoto(False, app_icon)
    form.resizable(width=False, height=False)
    form.configure(bg='grey')

    window_height = 700
    window_width = 500
    x_cordinate = int((form.winfo_screenwidth()/2) - (window_width/2))
    y_cordinate = int((form.winfo_screenheight()/2) - (window_height/2))
    form.geometry(f'{window_width}x{window_height}+{x_cordinate}+{y_cordinate}')
    # endregion

    # region frame setting
    header = Frame(
        master = form,
        bg = '#c2c3c7',
        height = 50,
    )
    header.pack(side=TOP, fill=X)
    header.propagate(False)

    body = Frame(
        master = form,
        height = 80,
        bg = '#c2c3c7'
    )
    body.pack(fill=BOTH, expand=True)
    body.propagate(False)

    footer = Frame(
        master = form,
        bg = '#c2c3c7',
        height = 50,
    )
    footer.pack(side=BOTTOM, fill=X)
    footer.propagate(False)
    # endregion

    # region header
    registration_icon = PhotoImage(file=r'UI\source\menu.png')
    Label(
        master = header,
        bg = '#c2c3c7',
        fg = '#000000',
        text = 'Teacher Registration',
        font = ('calibri', 16, 'bold'),
        compound = LEFT,
        image = registration_icon,
        padx = 10
    ).pack(side=LEFT)
    # endregion

    # region Button
    back_icon = PhotoImage(file=r'UI\source\back.png')
    back = Button(
        master = footer,
        bg = '#5f574f',
        fg = '#fff1e8',
        text = 'Back',
        font = ('calibri', 14, 'bold'),
        padx = 8,
        pady = 10,
        image = back_icon,
        compound = LEFT, 
        command = back_btn_onclick  
    )
    back.pack(side=LEFT, padx=(10, 0), pady=(0, 10))

    done_icon = PhotoImage(file=r'UI\source\done.png')
    done = Button(
        master = footer,
        bg = '#50e112',
        fg = '#000000',
        text = 'Done',
        font = ('calibri', 14, 'bold'),
        padx = 8,
        pady = 10,
        image = done_icon,
        compound = LEFT,
        command = done_btn_onclick
    )
    done.pack(side=RIGHT, padx=(0, 10), pady=(0, 10))
    # endregion

    # region firstname
    Label(
        master = body,
        text = 'Firstname: ',
        bg = '#c2c3c7',
        fg = '#000000',
        anchor = W,
        font = ('calibri', 14, 'bold')
    ).pack(side=TOP, fill=X, pady=(10, 0), padx=10)

    fname_entry = Entry(
        master = body,
        font = ('calibri', 12),
        bg = '#fff1e8',
        fg = '#000000',
        bd = 1,
        textvariable = firstname_var
    )
    fname_entry.pack(side=TOP, fill=X, padx=10)
    fname_entry.insert(0, '*** only lowercase letters ***')
    # endregion

    # region lastname
    Label(
        master = body,
        text = 'Lastname: ',
        bg = '#c2c3c7',
        fg = '#000000',
        anchor = W,
        font = ('calibri', 14, 'bold')
    ).pack(side=TOP, fill=X, pady=(10, 0), padx=10)

    lname_entry = Entry(
        master = body,
        font = ('calibri', 12),
        bg = '#fff1e8',
        fg = '#000000',
        bd = 1,
        textvariable = lastname_var
    )
    lname_entry.pack(side=TOP, fill=X, padx=10)
    lname_entry.insert(0, '*** only lowercase letters ***')
    # endregion

    # region username
    Label(
        master = body,
        text = 'Username: ',
        bg = '#c2c3c7',
        fg = '#000000',
        anchor = W,
        font = ('calibri', 14, 'bold')
    ).pack(side=TOP, fill=X, pady=(10, 0), padx=10)

    username_entry = Entry(
        master = body,
        font = ('calibri', 12),
        bg = '#fff1e8',
        fg = '#000000',
        bd = 1,
        textvariable = username_var
    )
    username_entry.pack(side=TOP, fill=X, padx=10)
    username_entry.insert(0, '*** only alphabet or digits ***')
    # endregion

    # region password
    Label(
        master =body,
        text = 'Password: ',
        bg = '#c2c3c7',
        fg = '#000000',
        anchor = W,
        font = ('calibri', 14, 'bold')
    ).pack(side=TOP, fill=X, pady=(10, 0), padx=10)

    password_entry = Entry(
        master = body,
        font = ('calibri', 12),
        bg = '#fff1e8',
        fg = '#000000',
        bd = 1,
        textvariable = password_var
    )
    password_entry.pack(side=TOP, fill=X, padx=10)
    password_entry.insert(0, '*** 8 characters including alphabet, digits or underscore ***')
    # endregion

    # region email
    Label(
        master = body,
        text = 'Email: ',
        bg = '#c2c3c7',
        fg = '#000000',
        anchor = W,
        font = ('calibri', 14, 'bold')
    ).pack(side=TOP, fill=X, pady=(10, 0), padx=10)

    Entry(
        master = body,
        font = ('calibri', 12),
        bg = '#fff1e8',
        fg ='#000000',
        bd = 1,
        textvariable = email_var
    ).pack(side=TOP, fill=X, padx=10)
    # endregion

    form.mainloop()
    #endregion


def student_list_form(username):

    def onload_form():
        result = get_person(type='student')

        if not result['success']:
            message_form(result['error_msg'], success=False)
            return []
        
        return result['returndata']


    def exit_btn_onclick():
        form.quit()
        form.destroy()

    def delete_btn_onclick():
        selected_rowid = std_grid.selection()

        if not selected_rowid:
            message_form({'Selection Error!': 'Select at least one student.'}, success=False)
            return
        
        for rowid in selected_rowid:
            firstname, lastname, stdcode, class_, gender, national_code, phone, address = std_grid.item(
                rowid, 'values'
            )

            if askyesno('Warning!', f'Name: {firstname} {lastname}\nStudent Code: {stdcode}\n\nDo you want to delete this student?'):

                remove_student(key='std_code', val=stdcode)
                std_grid.delete(rowid)

    def edit_btn_onclick():
        selected_rowid = std_grid.selection()

        if (not selected_rowid) or (len(selected_rowid) > 1):
            message_form({'Selection Error!': 'Select just one student.'}, success=False)
            return

        form.withdraw()
        student_edit_form(std_grid)
        form.deiconify()

    def add_btn_onclick():
        form.withdraw()
        student_registration_form(std_grid, username)
        form.deiconify()

    std_list = onload_form()

    # region form
    form = Toplevel()

    # region form setting
    form.title('Student Management')
    app_icon = PhotoImage(file=r'UI\source\icon.png')
    form.iconphoto(False, app_icon)
    form.resizable(width=False, height=False)
    form.configure(bg='black')

    window_height = 700
    window_width = 1000
    x_cordinate = int((form.winfo_screenwidth()/2) - (window_width/2))
    y_cordinate = int((form.winfo_screenheight()/2) - (window_height/2))
    form.geometry(f'{window_width}x{window_height}+{x_cordinate}+{y_cordinate}')
    # endregion

    # region frame setting
    header = Frame(
        master = form,
        bg = '#c2c3c7',
        height = 50,
    )
    header.pack(side=TOP, fill=X)
    header.propagate(False)

    body = Frame(
        master = form,
        height = 80,
        bg = '#c2c3c7'
    )
    body.pack(fill=BOTH, expand=True)
    body.propagate(False)

    footer = Frame(
        master = form,
        bg = '#c2c3c7',
        height = 80,
    )
    footer.pack(side=BOTTOM, fill=X)
    footer.propagate(False)
    # endregion

    # region header
    Label(
        master = header,
        bg = '#c2c3c7',
        fg = '#000000',
        text = 'Student List',
        font = ('calibri', 16, 'bold'),
        compound = LEFT
    ).pack(side = LEFT)
    # endregion

    # region Button
    backimg = PhotoImage(file=r'UI\source\back.png')
    exit = Button(
        master = footer,
        bg = '#5f574f',
        fg = '#fff1e8',
        text = 'Exit',
        font = ('calibri', 12, 'bold'),
        padx = 8,
        pady = 6,
        image = backimg,
        compound = LEFT,
        command = exit_btn_onclick
    )
    exit.pack(side=LEFT, padx=(10, 0))

    addimg = PhotoImage(file=r'UI\source\add.png')
    add = Button(
        master = footer,
        bg = '#50e112',
        fg = '#000000',
        text = 'Add',
        font = ('calibri', 12, 'bold'),
        padx = 8,
        image = addimg,
        compound = LEFT,
        command = add_btn_onclick
        
    )
    add.pack(side=RIGHT, padx=(0, 10))

    editimg = PhotoImage(file=r'UI\source\edit.png')
    edit = Button(
        master = footer,
        bg = '#ffdd34',
        fg = '#000000',
        text = 'Edit',
        font = ('calibri', 12, 'bold'),
        padx = 8,
        image = editimg,
        compound = LEFT,
        command = edit_btn_onclick
        
    )
    edit.pack(side=RIGHT, padx=(0, 10))

    deleteimg = PhotoImage(file=r'UI\source\delete.png')
    delete = Button(
        master = footer,
        bg = '#ff004d',
        fg = '#000000',
        text = 'Delete',
        font = ('calibri', 12, 'bold'),
        padx = 8,
        image = deleteimg,
        compound = LEFT,
        command = delete_btn_onclick
        
    )
    delete.pack(side=RIGHT, padx=(0, 10))
    # endregion

    # region grid and scrollbar
    style = ttk.Style(form)
    style.theme_use('clam')
    style.configure('Treeview.Heading', background='#000000', foreground='#fff1e8')

    scrollbar = ttk.Scrollbar(master=body, orient='vertical')
    scrollbar.pack(side=RIGHT, fill=Y)

    std_grid = ttk.Treeview(master=body, 
                                columns=('firstname', 'lastname', 'stdcode', 'class', 'gender', 'nationalcode', 'phone', 'address'),
                                show='headings',
                                selectmode='extended'
                                )
    
    column_width = std_grid.winfo_width()

    std_grid.heading(column='firstname', text='Firstname', anchor=CENTER)
    std_grid.heading(column='lastname', text='Lastname', anchor=CENTER)
    std_grid.heading(column='stdcode', text='Student Code', anchor=CENTER)
    std_grid.heading(column='class', text='Class', anchor=CENTER)
    std_grid.heading(column='gender', text='Gender', anchor=CENTER)
    std_grid.heading(column='nationalcode', text='National Code', anchor=CENTER)
    std_grid.heading(column='phone', text='Phone', anchor=CENTER)
    std_grid.heading(column='address', text='Address', anchor=CENTER)

    std_grid.column(column='firstname', anchor=CENTER, width=column_width)
    std_grid.column(column='lastname', anchor=CENTER, width=column_width)
    std_grid.column(column='stdcode', anchor=CENTER, width=column_width)
    std_grid.column(column='class', anchor=CENTER, width=column_width)
    std_grid.column(column='gender', anchor=CENTER, width=column_width)
    std_grid.column(column='nationalcode', anchor=CENTER, width=column_width)
    std_grid.column(column='phone', anchor=CENTER, width=column_width)
    std_grid.column(column='address', anchor=CENTER, width=column_width)

    std_grid.pack(fill=BOTH, expand=True)

    std_grid.configure(yscrollcommand=scrollbar.set)
    scrollbar['command'] = std_grid.yview
    # endregion

    #region grid
    for ppl in std_list:
        if ppl['id'] == username:
            std_grid.insert('', END, values=(
                ppl['firstname'], ppl['lastname'], ppl['std_code'], ppl['class_'],
                ppl['gender'], ppl['national_code'], ppl['phone'], ppl['address']
                ))
    #endregion

    form.mainloop()
    #endregion
    

def student_registration_form(std_grid, username):

    def back_btn_onclick():
        form.quit()
        form.destroy()

    def done_btn_onclick():

        firstname = firstname_var.get()
        lastname = lastname_var.get()
        stdcode = stdcode_var.get()
        class_ = class_answer()
        gender = gender_answer()
        national_code = nationalcode_var.get()
        phone = phone_var.get()
        address = address_entry.get('1.0', 'end-1c')

        student = {
            'firstname': firstname,
            'lastname': lastname,
            'std_code': stdcode,
            'class_': class_,
            'gender': gender,
            'national_code': national_code,
            'phone': phone,
            'address': address,
            'id': username
        }

        result = save_person(type='student', person=student)

        if not result['success']:
            message_form(result['error_msg'], success=False)

            if 'firstname' in result['error_msg']:
                firstname_var.set('*** only lowercase letters ***')
            
            if 'lastname' in result['error_msg']:
                lastname_var.set('*** only lowercase letters ***')

            if 'std_code' in result['error_msg']:
                stdcode_var.set('*** must be 11 digits ***')

            if 'national_code' in result['error_msg']:
                nationalcode_var.set('*** must be 10 digits ***')

            if 'phone' in result['error_msg']:
                phone_var.set('*** can be empty or must be 11 digits ***')

        else:
            std_grid.insert('', END, values=(
                firstname, lastname, stdcode, class_, gender, national_code, phone, address
            ))
            message_form(result['success_msg'], success=True)
            back_btn_onclick()
        

    # region form
    form = Toplevel()

    #region variable
    firstname_var = StringVar()
    lastname_var = StringVar()
    stdcode_var = StringVar()
    nationalcode_var = StringVar()
    phone_var = StringVar()
    #endregion

    # region form setting
    form.title('Student Management')
    app_icon = PhotoImage(file=r'UI\source\icon.png')
    form.iconphoto(False, app_icon)
    form.resizable(width=False, height=False)
    form.configure(bg='grey')

    window_height = 700
    window_width = 500
    x_cordinate = int((form.winfo_screenwidth()/2) - (window_width/2))
    y_cordinate = int((form.winfo_screenheight()/2) - (window_height/2))
    form.geometry(f'{window_width}x{window_height}+{x_cordinate}+{y_cordinate}')
    # endregion

    # region frame setting
    header = Frame(
        master = form,
        bg = '#c2c3c7',
        height = 50,
    )
    header.pack(side=TOP, fill=X)
    header.propagate(False)

    body = Frame(
        master = form,
        height = 80,
        bg = '#c2c3c7'
    )
    body.pack(fill=BOTH, expand=True)
    body.propagate(False)

    footer = Frame(
        master = form,
        bg = '#c2c3c7',
        height = 50,
    )
    footer.pack(side=BOTTOM, fill=X)
    footer.propagate(False)
    # endregion

    # region header
    registration_icon = PhotoImage(file=r'UI\source\menu.png')
    Label(
        master = header,
        bg = '#c2c3c7',
        fg = '#000000',
        text = 'Student Registration',
        font = ('calibri', 16, 'bold'),
        compound = LEFT,
        image = registration_icon,
        padx = 10
    ).pack(side = LEFT)
    # endregion

    # region Button
    back_icon = PhotoImage(file=r'UI\source\back.png')
    back = Button(
        master = footer,
        bg = '#5f574f',
        fg = '#fff1e8',
        text = 'Back',
        font = ('calibri', 14, 'bold'),
        padx = 8,
        pady = 10,
        image = back_icon,
        compound = LEFT,
        command = back_btn_onclick  
    )
    back.pack(side=LEFT, padx=(10, 0), pady=(0, 10))

    done_icon = PhotoImage(file=r'UI\source\done.png')
    done = Button(
        master=footer,
        bg='#50e112',
        fg='#000000',
        text='Done',
        font=('calibri', 14, 'bold'),
        padx=8,
        pady=10,
        image=done_icon,
        compound=LEFT,
        command=done_btn_onclick
    )
    done.pack(side=RIGHT, padx=(0, 10), pady=(0, 10))
    # endregion

    # region firstname
    Label(
        master=body,
        text='Firstname: ',
        bg='#c2c3c7',
        fg='#000000',
        anchor=W,
        font=('calibri', 12, 'bold')
    ).pack(side=TOP, fill=X, pady=(10, 0), padx=10)

    fname_entry = Entry(
        master=body,
        font=('calibri', 12),
        bg='#fff1e8',
        fg='#000000',
        bd=1,
        textvariable=firstname_var
    )
    fname_entry.pack(side=TOP, fill=X, padx=10)
    fname_entry.insert(0, '*** only lowercase letters ***')
    # endregion

    # region lastname
    Label(
        master=body,
        text='Lastname: ',
        bg='#c2c3c7',
        fg='#000000',
        anchor=W,
        font=('calibri', 12, 'bold')
    ).pack(side=TOP, fill=X, pady=(10, 0), padx=10)

    lname_entry = Entry(
        master=body,
        font=('calibri', 12),
        bg='#fff1e8',
        fg='#000000',
        bd=1,
        textvariable=lastname_var
    )
    lname_entry.pack(side=TOP, fill=X, padx=10)
    lname_entry.insert(0, '*** only lowercase letters ***')
    # endregion

    # region student code
    Label(
        master=body,
        text='Student Code: ',
        bg='#c2c3c7',
        fg='#000000',
        anchor=W,
        font=('calibri', 12, 'bold')
    ).pack(side=TOP, fill=X, pady=(10, 0), padx=10)

    stdcode_entry = Entry(
        master=body,
        font=('calibri', 12),
        bg='#fff1e8',
        fg='#000000',
        bd=1,
        textvariable=stdcode_var
    )
    stdcode_entry.pack(side=TOP, fill=X, padx=10)
    stdcode_entry.insert(0, '*** must be 11 digits ***')
    # endregion

    # region class
    Label(
        master=body,
        text='Class: ',
        bg='#c2c3c7',
        fg='#000000',
        anchor=W,
        font=('calibri', 12, 'bold')
    ).pack(side=TOP, fill=X, pady=(10, 0), padx=10)


    def class_answer():
        class_list = ''

        if checkA.get():
            class_list += 'A' 

        if checkB.get():
            class_list += 'B'  

        if checkC.get():
            class_list += 'C'  

        if checkD.get():
            class_list += 'D'  

        class_list = ' - '.join(class_list) 

        return class_list


    checkA = IntVar()   
    checkB = IntVar()   
    checkC = IntVar()
    checkD = IntVar()


    c1 = Checkbutton(body, text='A', font=('calibri', 10), bg='#c2c3c7', padx= 15, variable=checkA, command=class_answer)
    c1.pack(anchor=W)
    c2 = Checkbutton(body, text='B', font=('calibri', 10), bg='#c2c3c7', padx= 15, variable=checkB, command=class_answer)
    c2.pack(anchor=W)
    c3 = Checkbutton(body, text='C', font=('calibri', 10), bg='#c2c3c7', padx= 15, variable=checkC, command=class_answer)
    c3.pack(anchor=W)
    c4 = Checkbutton(body, text='D', font=('calibri', 10), bg='#c2c3c7', padx= 15, variable=checkD, command=class_answer)
    c4.pack(anchor=W)
    # endregion

    # region gender
    Label(
        master=body,
        text='Gender: ',
        bg='#c2c3c7',
        fg='#000000',
        anchor=W,
        font=('calibri', 12, 'bold')
    ).pack(side=TOP, fill=X, pady=(10, 0), padx=10)

    def gender_answer():
        
        if var:
            return str(var.get())
        
    
    var = StringVar()
    var.set(None)
    

    r1 = Radiobutton(body, text='Male', font=('calibri', 10), bg='#c2c3c7', padx= 15, variable=var, value='Male', command=gender_answer)
    r1.pack(anchor=W)
    r2 = Radiobutton(body, text='Female', font=('calibri', 10), bg='#c2c3c7', padx= 15, variable=var, value='Female', command=gender_answer)
    r2.pack(anchor=W)
    # endregion

    # region national code
    Label(
        master=body,
        text='National Code: ',
        bg='#c2c3c7',
        fg='#000000',
        anchor=W,
        font=('calibri', 12, 'bold')
    ).pack(side=TOP, fill=X, pady=(10, 0), padx=10)

    ntlcode_entry = Entry(
        master=body,
        font=('calibri', 12),
        bg='#fff1e8',
        fg='#000000',
        bd=1,
        textvariable=nationalcode_var
    )
    ntlcode_entry.pack(side=TOP, fill=X, padx=10)
    ntlcode_entry.insert(0, '*** must be 10 digits ***')
    # endregion

    # region phone
    Label(
        master=body,
        text='Phone: ',
        bg='#c2c3c7',
        fg='#000000',
        anchor=W,
        font=('calibri', 12, 'bold')
    ).pack(side=TOP, fill=X, pady=(10, 0), padx=10)

    phone_entry = Entry(
        master=body,
        font=('calibri', 12),
        bg='#fff1e8',
        fg='#000000',
        bd=1,
        textvariable=phone_var
    )
    phone_entry.pack(side=TOP, fill=X, padx=10)
    phone_entry.insert(0, '*** can be empty or must be 11 digits ***')
    # endregion

    # region Address
    Label(
        master=body,
        text='Address: ',
        bg='#c2c3c7',
        fg='#000000',
        anchor=W,
        font=('calibri', 12, 'bold')
    ).pack(side=TOP, fill=X, pady=(10, 0), padx=10)

    address_entry = Text(
        master=body,
        font=('calibri', 12),
        bg='#fff1e8',
        fg='#000000',
        bd=1,
    )
    address_entry.pack(fill=BOTH, expand=True, padx=10, pady=(0, 10))
    # endregion

    form.mainloop()
    #endregion


def student_edit_form(std_grid):

    def back_btn_onclick():
        form.quit()
        form.destroy()

    def done_btn_onclick():

        new_firstname = firstname_var.get()
        new_lastname = lastname_var.get()
        stdcode = stdcode_var.get()
        new_class_ = class_answer()
        new_gender = gender_answer()
        national_code = nationalcode_var.get()
        new_phone = phone_var.get()
        new_address = address_entry.get('1.0', 'end-1c')

        result = edit_student(
            new_firstname=new_firstname,
            new_lastname=new_lastname,
            stdcode=stdcode,
            new_class_=new_class_,
            new_gender=new_gender,
            national_code=national_code,
            new_phone=new_phone,
            new_address=new_address
        )


        if not result['success']:
            message_form(result['error_msg'], success=False)

            if 'firstname' in result['error_msg']:
                firstname_var.set('(Firstname must include just lowercase letters)')
            
            if 'lastname' in result['error_msg']:
                lastname_var.set('(Lastname must include just lowercase letters)')

            if 'std_code' in result['error_msg']:
                stdcode_var.set('(Student Code must include just 11 digits)')

            if 'national_code' in result['error_msg']:
                nationalcode_var.set('(National Code must include just 10 digits)')

            if 'phone' in result['error_msg']:
                phone_var.set('(Phone can be empty or must include just 11 digits)')

        else:
            std_grid.item(row_id, values=(
                new_firstname, new_lastname, stdcode, new_class_, new_gender, national_code, new_phone, new_address
            ))
            message_form(result['success_msg'], success=True)
            back_btn_onclick()
        

    # region form
    form = Toplevel()

    #region variable
    firstname_var = StringVar()
    lastname_var = StringVar()
    stdcode_var = StringVar()
    nationalcode_var = StringVar()
    phone_var = StringVar()
    #endregion

    # region form setting
    form.title('Student Management')
    app_icon = PhotoImage(file=r'UI\source\icon.png')
    form.iconphoto(False, app_icon)
    form.resizable(width=False, height=False)
    form.configure(bg='grey')

    window_height = 700
    window_width = 500
    x_cordinate = int((form.winfo_screenwidth()/2) - (window_width/2))
    y_cordinate = int((form.winfo_screenheight()/2) - (window_height/2))
    form.geometry(f'{window_width}x{window_height}+{x_cordinate}+{y_cordinate}')
    # endregion

    # region frame setting
    header = Frame(
        master = form,
        bg = '#c2c3c7',
        height = 50,
    )
    header.pack(side=TOP, fill=X)
    header.propagate(False)

    body = Frame(
        master = form,
        height = 80,
        bg = '#c2c3c7'
    )
    body.pack(fill=BOTH, expand=True)
    body.propagate(False)

    footer = Frame(
        master = form,
        bg = '#c2c3c7',
        height = 50,
    )
    footer.pack(side=BOTTOM, fill=X)
    footer.propagate(False)
    # endregion

    # region header
    registration_icon = PhotoImage(file=r'UI\source\menu.png')
    Label(
        master = header,
        bg = '#c2c3c7',
        fg = '#000000',
        text = 'Edit Student',
        font = ('calibri', 16, 'bold'),
        compound = LEFT,
        image=registration_icon,
        padx= 10
    ).pack(side = LEFT)
    # endregion

    # region Button
    back_icon = PhotoImage(file=r'UI\source\back.png')
    back = Button(
        master=footer,
        bg='#5f574f',
        fg='#fff1e8',
        text='Back',
        font=('calibri', 14, 'bold'),
        padx=8,
        pady=10,
        image=back_icon,
        compound=LEFT,
        command=back_btn_onclick  
    )
    back.pack(side=LEFT, padx=(10, 0), pady=(0, 10))

    done_icon = PhotoImage(file=r'UI\source\done.png')
    done = Button(
        master=footer,
        bg='#50e112',
        fg='#000000',
        text='Done',
        font=('calibri', 14, 'bold'),
        padx=8,
        pady=10,
        image=done_icon,
        compound=LEFT,
        command=done_btn_onclick
    )
    done.pack(side=RIGHT, padx=(0, 10), pady=(0, 10))
    # endregion

    # region firstname
    Label(
        master=body,
        text='Firstname: ',
        bg='#c2c3c7',
        fg='#000000',
        anchor=W,
        font=('calibri', 12, 'bold')
    ).pack(side=TOP, fill=X, pady=(10, 0), padx=10)

    fname_entry = Entry(
        master=body,
        font=('calibri', 12),
        bg='#fff1e8',
        fg='#000000',
        bd=1,
        textvariable=firstname_var
    )
    fname_entry.pack(side=TOP, fill=X, padx=10)
    fname_entry.insert(0, '(Firstname must include just lowercase letters)')
    # endregion

    # region lastname
    Label(
        master=body,
        text='Lastname: ',
        bg='#c2c3c7',
        fg='#000000',
        anchor=W,
        font=('calibri', 12, 'bold')
    ).pack(side=TOP, fill=X, pady=(10, 0), padx=10)

    lname_entry = Entry(
        master=body,
        font=('calibri', 12),
        bg='#fff1e8',
        fg='#000000',
        bd=1,
        textvariable=lastname_var
    )
    lname_entry.pack(side=TOP, fill=X, padx=10)
    lname_entry.insert(0, '(Lastname must include just lowercase letters)')
    # endregion

    # region student code
    Label(
        master=body,
        text='Student Code: ',
        bg='#c2c3c7',
        fg='#000000',
        anchor=W,
        font=('calibri', 12, 'bold')
    ).pack(side=TOP, fill=X, pady=(10, 0), padx=10)

    stdcode_entry = Entry(
        master=body,
        font=('calibri', 12),
        bg='#fff1e8',
        fg='#000000',
        bd=1,
        state=DISABLED,
        textvariable=stdcode_var
    )
    stdcode_entry.pack(side=TOP, fill=X, padx=10)
    stdcode_entry.insert(0, '(Student Code must include just 11 digits)')
    # endregion

    # region class
    Label(
        master=body,
        text='Class: ',
        bg='#c2c3c7',
        fg='#000000',
        anchor=W,
        font=('calibri', 12, 'bold')
    ).pack(side=TOP, fill=X, pady=(10, 0), padx=10)


    def class_answer():
        class_list = ''

        if checkA.get():
            class_list += 'A' 

        if checkB.get():
            class_list += 'B'  

        if checkC.get():
            class_list += 'C'  

        if checkD.get():
            class_list += 'D'  

        class_list = ' - '.join(class_list) 

        return class_list


    checkA = IntVar()   
    checkB = IntVar()   
    checkC = IntVar()
    checkD = IntVar()


    c1 = Checkbutton(body, text='A', font=('calibri', 10), bg='#c2c3c7', padx= 15, variable=checkA, command=class_answer)
    c1.pack(anchor=W)
    c2 = Checkbutton(body, text='B', font=('calibri', 10), bg='#c2c3c7', padx= 15, variable=checkB, command=class_answer)
    c2.pack(anchor=W)
    c3 = Checkbutton(body, text='C', font=('calibri', 10), bg='#c2c3c7', padx= 15, variable=checkC, command=class_answer)
    c3.pack(anchor=W)
    c4 = Checkbutton(body, text='D', font=('calibri', 10), bg='#c2c3c7', padx= 15, variable=checkD, command=class_answer)
    c4.pack(anchor=W)
    # endregion

    # region gender
    Label(
        master=body,
        text='Gender: ',
        bg='#c2c3c7',
        fg='#000000',
        anchor=W,
        font=('calibri', 12, 'bold')
    ).pack(side=TOP, fill=X, pady=(10, 0), padx=10)

    def gender_answer():
        
        if var:
            return str(var.get())
          
        
    var = StringVar()
    

    r1 = Radiobutton(body, text='Male', font=('calibri', 10), bg='#c2c3c7', padx= 15, variable=var, value='Male', command=gender_answer)
    r1.pack(anchor=W)
    r2 = Radiobutton(body, text='Female', font=('calibri', 10), bg='#c2c3c7', padx= 15, variable=var, value='Female', command=gender_answer)
    r2.pack(anchor=W)
    # endregion

    # region national code
    Label(
        master=body,
        text='National Code: ',
        bg='#c2c3c7',
        fg='#000000',
        anchor=W,
        font=('calibri', 12, 'bold')
    ).pack(side=TOP, fill=X, pady=(10, 0), padx=10)

    ntlcode_entry = Entry(
        master=body,
        font=('calibri', 12),
        bg='#fff1e8',
        fg='#000000',
        bd=1,
        state=DISABLED,
        textvariable=nationalcode_var
    )
    ntlcode_entry.pack(side=TOP, fill=X, padx=10)
    ntlcode_entry.insert(0, '(National Code must include just 10 digits)')
    # endregion

    # region phone
    Label(
        master=body,
        text='Phone: ',
        bg='#c2c3c7',
        fg='#000000',
        anchor=W,
        font=('calibri', 12, 'bold')
    ).pack(side=TOP, fill=X, pady=(10, 0), padx=10)

    phone_entry = Entry(
        master=body,
        font=('calibri', 12),
        bg='#fff1e8',
        fg='#000000',
        bd=1,
        textvariable=phone_var
    )
    phone_entry.pack(side=TOP, fill=X, padx=10)
    phone_entry.insert(0, '(Phone can be empty or must include just 11 digits)')
    # endregion

    # region Address
    Label(
        master=body,
        text='Address: ',
        bg='#c2c3c7',
        fg='#000000',
        anchor=W,
        font=('calibri', 12, 'bold')
    ).pack(side=TOP, fill=X, pady=(10, 0), padx=10)

    address_entry = Text(
        master=body,
        font=('calibri', 12),
        bg='#fff1e8',
        fg='#000000',
        bd=1,
    )
    address_entry.pack(fill=BOTH, expand=True, padx=10, pady=(0, 10))
    # endregion

    #region set data form
    row_id = std_grid.selection()[0]

    firstname, lastname, stdcode, class_, gender, national_code, phone, address = std_grid.item(
        row_id, 'values'
    )

    firstname_var.set(firstname)
    lastname_var.set(lastname)
    stdcode_var.set(stdcode)

    for i in class_:
        if i == 'A':
            checkA.set(1)
        if i == 'B':
            checkB.set(1)
        if i == 'C':
            checkC.set(1)
        if i == 'D':
            checkD.set(1)    

    var.set(gender)
    nationalcode_var.set(national_code)
    phone_var.set(phone)
    address_entry.delete(1.0, END)
    address_entry.insert(END, address)

    form.mainloop()
    #endregion

    #endregion


def login_form():

    def login_btn_onclick():
        
        username = username_var.get()
        password = password_var.get()

        result = check_login(username=username, password=password)

        if not result['success']:
            message_form(result['error_msg'], success=False)
            
            if 'login' in result['error_msg']:
                username_var.set('')
                password_var.set('')

        else:
            
            form.withdraw()
            student_list_form(username)
            form.deiconify()

    def register_btn_onclick():
        form.withdraw()
        teacher_registration_form()
        form.deiconify()

    # region form
    form = Tk()

    #region variable
    username_var = StringVar()
    password_var = StringVar()
    #endregion

    # region form setting
    form.title('Student Management')
    app_icon = PhotoImage(file=r'UI\source\icon.png')
    form.iconphoto(False, app_icon)
    form.resizable(width=False, height=False)
    form.configure(bg='grey')

    window_height = 500
    window_width = 350
    x_cordinate = int((form.winfo_screenwidth()/2) - (window_width/2))
    y_cordinate = int((form.winfo_screenheight()/2) - (window_height/2))
    form.geometry(f'{window_width}x{window_height}+{x_cordinate}+{y_cordinate}')
    # endregion

    # region frame setting
    header = Frame(
        master = form,
        bg = '#c2c3c7',
        height = 50,
    )
    header.pack(side=TOP, fill=X)
    header.propagate(False)

    body = Frame(
        master = form,
        height = 80,
        bg = '#c2c3c7'
    )
    body.pack(fill=BOTH, expand=True)
    body.propagate(False)
    # endregion

    # region header
    Label(
        master = header,
        bg = '#c2c3c7',
        fg = '#000000',
        text = 'Student Management',
        font = ('calibri', 16, 'bold'),
        compound = LEFT,
    ).pack(side = TOP, pady=10)
    # endregion

    # region username
    Label(
        master=body,
        text='Username: ',
        bg='#c2c3c7',
        fg='#000000',
        anchor=W,
        font=('calibri', 14, 'bold')
    ).pack(side=TOP, fill=X, pady=(10, 0), padx=10)

    Entry(
        master=body,
        font=('calibri', 14),
        bg='#fff1e8',
        fg='#000000',
        bd=1,
        textvariable=username_var
    ).pack(side=TOP, fill=X, padx=10)
    # endregion

    # region password
    Label(
        master=body,
        text='Password: ',
        bg='#c2c3c7',
        fg='#000000',
        anchor=W,
        font=('calibri', 14, 'bold')
    ).pack(side=TOP, fill=X, pady=(30, 0), padx=10)

    Entry(
        master=body,
        font=('calibri', 14),
        bg='#fff1e8',
        fg='#000000',
        bd=1,
        textvariable=password_var
    ).pack(side=TOP, fill=X, padx=10)
    # endregion

    # region Button
    login = Button(
            master=body,
            bg='#0033ff',
            fg='#000000',
            text='LOGIN',
            font=('calibri', 16, 'bold'),
            padx=50,
            pady=6,
            compound=LEFT,
            command=login_btn_onclick   
        )
    login.pack(anchor=CENTER, pady=40)


    register = Button(
            master=body,
            bg='#ff8426',
            fg='#000000',
            text='REGISTER',
            font=('calibri', 16, 'bold'),
            padx=37,
            pady=6,
            compound=LEFT,
            command=register_btn_onclick   
        )
    register.pack(anchor=CENTER)
    # endregion

    form.mainloop()
    #endregion



