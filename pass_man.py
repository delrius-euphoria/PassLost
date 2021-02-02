import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog
import pyglet
import shelve
from make import create, insert
from hash import hasher,unhasher, pbkdf
import tkinter.simpledialog

pyglet.font.add_file('fonts/kenyan coffee rg.ttf')
pyglet.font.add_file('fonts/coolvetica compressed rg.ttf')
pyglet.font.add_file('fonts/Roboto-Black.ttf')
title_font = ('Kenyan Coffee Rg',25)
label_font = ('Verdana Pro Light',16)

root = tk.Tk()
s = ttk.Style()
s.configure('menu.TButton',font=label_font,width=50)
new_win = None
existing_win = None
save_path = None

def new():
    global new_win, save_path, pressed

    pressed = True
    def none():
        global new_win
        new_win.destroy()
        new_win = None
    
    def show():
        global pressed
        if pressed:
            master_pw.config(show='')
            master_passw_conf.config(show='')
            pressed = False
        else:
            master_pw.config(show='●')
            master_passw_conf.config(show='●')
            pressed = True
        
    if new_win:
        return
    
    save_path = filedialog.asksaveasfile(title='Location to save file',filetypes=[('Database files','*.db')]
                                        ,defaultextension=[('Database files','*.db')])
    if not save_path:
        return
    # open(save_path+'.db','w')
    new_win = tk.Toplevel()
    
    tk.Label(new_win,text='Enter your details here',font=label_font).grid(row=0,column=0,columnspan=3,sticky='ew',pady=10)
    tk.Label(new_win,text='Enter master password').grid(row=1,column=0)
    master_pw = ttk.Entry(new_win,width=60,show='●',font=(0,11))
    master_pw.grid(row=1,column=1,ipady=5,padx=10)
    
    tk.Label(new_win,text='Confirm master password').grid(row=2,column=0)
    master_passw_conf = ttk.Entry(new_win,width=60,show='●',font=(0,11))
    master_passw_conf.grid(row=2,column=1,ipady=5,padx=10,pady=10)

    btn = ttk.Button(new_win,text='Show',command=show)
    btn.grid(row=1,column=2)

    ttk.Button(new_win,text='Submit details',command=lambda: submit(master_pw,master_passw_conf,save_path.name)).grid(row=3,column=0,pady=(10,0),columnspan=3,sticky='ew')
    new_win.protocol('WM_DELETE_WINDOW',none)

def existing():
    path = filedialog.askopenfilename(title='Location to save file',filetypes=[('Database files','*.db')]
                                        ,defaultextension=[('Database files','*.db')])
    if not path:
        return
    name = path.split('/')[-1].split('.')[0]
    passw = tkinter.simpledialog.askstring('Password','Enter your master password',show='●')
    
    if passw is None:
        return
    
    with shelve.open('datas/data') as file:
        master_pw = file[path][path][:32]
        salt = file[path][path][32:]

    user_try = pbkdf(passw.encode('utf8'),salt)[0]
    if user_try == master_pw:
        main_win(path,name)
    else:
        messagebox.showerror('Invalid',f'Invalid master password for selected database: {name}')
    
def submit(e1,e2,path):
    if e1.get() == e2.get():
        passw = e1.get().encode('utf-8')
        hashed,salt = pbkdf(passw)
        with shelve.open('datas/data') as file:
            file[path] = {path:hashed+salt}
        
        create(path,path.split('/')[-1].split('.')[0])
        new_win.destroy()
        main_win(path,path.split('/')[-1].split('.')[0])
    
    else:
        messagebox.showerror('Error','Make sure to verify both passwords and use 16 digit passwords.',parent=new_win)

def main_win(path,name):
    
    main = tk.Toplevel()
    columns = (('Sl.No', 60),("Username", 300), ("url", 200))
    tree = ttk.Treeview(main, height=20, columns=[
                                        x[0] for x in columns], show='headings')
    tree.grid(row=0, column=0, sticky='news')

    # setup columns attributes
    for col, width in columns:
        tree.heading(col, text=col)
        tree.column(col, width=width, anchor=tk.CENTER)
    
    con = sqlite3.connect(path)
    c = con.cursor()
    c.execute('SELECT username,url FROM {}'.format(name))
    data = c.fetchall()
    output = [tuple((i, *item)) for i, item in enumerate(data,start=1)]
    # loop = tree_val(path,output)
    for item in output:
        tree.insert('','end',value=item)

    def pop_menu(event):
        item = tree.identify_row(event.y)
        tree.selection_set(item)
        popup1.post(event.x_root, event.y_root)

    def copy():
        row_id = tree.selection()[0]
        id = tree.item(row_id,'values')[0]
        passw = tree_val(path,name,int(id))
        main.clipboard_clear()
        main.clipboard_append(passw.decode('utf8'))

    popup1 = tk.Menu(main, tearoff=0)
    popup1.add_command(label='Copy', command=copy)
    popup1.add_command(label='Add data', command=lambda: add_data(data,name))

    # tree.bind('<Double-1>',lambda e: add_data(path,name))
    tree.bind('<Button-3>', pop_menu)
    # tree.bind('<<TreeviewSelect>>',selected)

    ttk.Button(main,text='Add data',command=lambda: add_data(path,name)).grid(row=1,column=0,sticky='ew')
    ttk.Button(main,text='Refresh',command=lambda:refresh(main,path,name)).grid(row=2,column=0,sticky='ew')

def add_data(path,name):
    global pressed
    pressed = True
    
    def show():
        global pressed
        if pressed:
            passw_e.config(show='')
            pressed = False
        else:
            passw_e.config(show='●')
            pressed = True

    data_win = tk.Toplevel()
    tk.Label(data_win,text='Enter your details here',font=label_font).grid(row=0,column=0,columnspan=3,sticky='ew')

    tk.Label(data_win,text='Username/email').grid(row=1,column=0)
    username_e = ttk.Entry(data_win,width=60,font=(0,11))
    username_e.grid(row=1,column=1,ipady=5,pady=(10,0))
    
    tk.Label(data_win,text='Password').grid(row=2,column=0)
    passw_e = ttk.Entry(data_win,width=60,show='●',font=(0,11))
    passw_e.grid(row=2,column=1,ipady=5,padx=10,pady=5)

    tk.Label(data_win,text='Website').grid(row=3,column=0,padx=10)
    url_e = ttk.Entry(data_win,width=60,font=(0,11))
    url_e.grid(row=3,column=1,ipady=5,padx=10)

    btn = ttk.Button(data_win,text='Show',command=show)
    btn.grid(row=2,column=2)

    ttk.Button(data_win,text='Store data',command=lambda:store(path,name,username_e.get(),passw_e.get(),url_e.get())).grid(row=4,column=0,pady=(10,0),columnspan=3,sticky='ew')

def store(path,name,user,passw,url):
    with shelve.open('datas/data') as file:
        master = file[path][path][:32]
    hashed = hasher(master,passw.encode('utf-8'))
    insert(path,name,user,hashed,url)

def refresh(win,path,name):
    win.destroy()
    main_win(path,name)

def tree_val(path,name,id):
    with shelve.open('datas/data') as file:
        master = file[path][path][:32]
    
    con = sqlite3.connect(path)
    c = con.cursor()
    c.execute('SELECT password FROM {}'.format(name))
    data = c.fetchall()
    final = []
    give = []
    for j in data:
        final.append(unhasher(master,j[0]))
    return final[id-1]
    # for x,y in zip(out,final):
    #     lst = list(x)
    #     lst[2] = y
    #     tup = tuple(lst)
    #     give.append(tup)

    return give

tk.Label(root,text='Welcome to Password Manager',font=title_font).grid(row=0,column=0,padx=20
                                                        ,sticky='ew',columnspan=2)
ttk.Button(root,text='Create a new password database',command=new,width=50,style='menu.TButton').grid(row=1,column=0,ipady=5,padx=10,pady=5)
ttk.Button(root,text='Open existsting database',command=existing,width=50,style='menu.TButton').grid(row=2,column=0,ipady=5,padx=10,pady=5)

root.mainloop()


