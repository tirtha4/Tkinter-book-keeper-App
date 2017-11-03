#! /usr/bin/env python
import sys
import database


try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import support_app



def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    support_app.set_Tk_var()
    top = New_Toplevel_1 (root)
    support_app.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel_1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    support_app.set_Tk_var()
    top = New_Toplevel_1 (w)
    support_app.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None





class New_Toplevel_1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        root.iconbitmap("books.ico")
        top.geometry("600x450+257+39")
        top.title("Book-Keeper")
        top.configure(background="#5b5b5b")

        def get_selected_row(event):
            try:
                    global selected_item
                    selection=self.Scrolledlistbox1.curselection()
                    if selection is not ():
                        selected_item = self.Scrolledlistbox1.get(selection)
                        self.Entry1.delete(0,END)
                        self.Entry1.insert(END,selected_item[1])
                        self.Entry2.delete(0,END)
                        self.Entry2.insert(END,selected_item[2])
                        self.Entry3.delete(0,END)
                        self.Entry3.insert(END,selected_item[3])
                        self.Entry4.delete(0,END)
                        self.Entry4.insert(END,selected_item[4])
            except IndexError:
                pass

        def view_funct():
            self.Scrolledlistbox1.delete(0,END)
            for line in database.view():
                self.Scrolledlistbox1.insert(END,line)
        def search_funct():
            self.Scrolledlistbox1.delete(0,END)
            for line in database.search(support_app.Title_var.get(),support_app.isbn_var.get(), \
                                            support_app.author_var.get(),support_app.year_var.get()):
                self.Scrolledlistbox1.insert(END,line)
        def insert_funct():
            if support_app.Title_var.get() is not None:
                database.insert(support_app.Title_var.get(),support_app.isbn_var.get(), \
                                support_app.author_var.get(),support_app.year_var.get())

            self.Scrolledlistbox1.delete(0,END)
            self.Scrolledlistbox1.insert(END,(support_app.Title_var.get(),"|",support_app.isbn_var.get(),support_app.author_var.get(),support_app.year_var.get()))

        def delete_funct():
            try:
                database.delete(selected_item[0])
            except NameError:
                pass

        def update_funct():
            try:
                database.update(selected_item[0],support_app.Title_var.get(),support_app.isbn_var.get(), \
                                            support_app.author_var.get(),support_app.year_var.get())
            except NameError:
                pass


        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.02, rely=0.02, relheight=0.19, relwidth=0.96)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(width=575)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.12, rely=0.12, height=21, width=54)
        self.Label1.configure(background="#d9d9d9",disabledforeground="#a3a3a3",text='''Title''',width=54)

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.12, rely=0.59, height=21, width=53)
        self.Label2.configure(background="#d9d9d9",disabledforeground="#a3a3a3",text='''Author''',width=53)


        self.Label3 = Label(self.Frame1)
        self.Label3.place(relx=0.57, rely=0.12, height=21, width=31)
        self.Label3.configure(background="#d9d9d9",disabledforeground="#a3a3a3",text='''ISBN''',width=54)

        self.Label4 = Label(self.Frame1)
        self.Label4.place(relx=0.57, rely=0.59, height=21, width=29)
        self.Label4.configure(background="#d9d9d9",disabledforeground="#a3a3a3",text='''Year''',width=54)


        self.Entry1 = Entry(self.Frame1)
        self.Entry1.place(relx=0.23, rely=0.12, relheight=0.24, relwidth=0.16)
        self.Entry1.configure(font="TkFixedFont",width=94,textvariable=support_app.Title_var)

        self.Entry2 = Entry(self.Frame1)
        self.Entry2.place(relx=0.23, rely=0.59, relheight=0.24, relwidth=0.16)
        self.Entry2.configure(font="TkFixedFont",width=94,textvariable=support_app.author_var)

        self.Entry3 = Entry(self.Frame1)
        self.Entry3.place(relx=0.66, rely=0.12, relheight=0.24, relwidth=0.16)
        self.Entry3.configure(font="TkFixedFont",width=94,textvariable=support_app.isbn_var)


        self.Entry4 = Entry(self.Frame1)
        self.Entry4.place(relx=0.66, rely=0.59, relheight=0.24, relwidth=0.16)
        self.Entry4.configure(font="TkFixedFont",width=94,textvariable=support_app.year_var)


        self.Scrolledlistbox1 = ScrolledListBox(top)
        self.Scrolledlistbox1.place(relx=0.03, rely=0.24, relheight=0.7
                , relwidth=0.54)
        self.Scrolledlistbox1.configure(background="white")
        self.Scrolledlistbox1.configure(disabledforeground="#a3a3a3")
        self.Scrolledlistbox1.configure(font="TkFixedFont")
        self.Scrolledlistbox1.configure(foreground="black")
        self.Scrolledlistbox1.configure(highlightbackground="#d9d9d9")
        self.Scrolledlistbox1.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1.configure(selectbackground="#c4c4c4")
        self.Scrolledlistbox1.configure(selectforeground="black")
        self.Scrolledlistbox1.configure(width=10)
        self.Scrolledlistbox1.bind('<<ListboxSelect>>',get_selected_row)

        self.b1 = Button(top)
        self.b1.configure(command=view_funct,foreground="#000000",background="#d9d9d9",borderwidth="5",highlightcolor="black",pady="0",width=117)
        self.b1.place(relx=0.68, rely=0.29, height=24, width=117)
        self.b1.configure(text='''View All''')

        self.b2 = Button(top)
        self.b2.place(relx=0.68, rely=0.38, height=24, width=116)
        self.b2.configure(command=search_funct,foreground="#000000",background="#d9d9d9",borderwidth="5",highlightcolor="black",pady="0",width=117)
        self.b2.configure(text='''Search''')


        self.b3 = Button(top)
        self.b3.place(relx=0.68, rely=0.47, height=24, width=117)
        self.b3.configure(command=insert_funct,foreground="#000000",background="#d9d9d9",borderwidth="5",highlightcolor="black",pady="0",width=117)
        self.b3.configure(text='''Insert Data''')


        self.b4 = Button(top)
        self.b4.place(relx=0.68, rely=0.56, height=24, width=117)
        self.b4.configure(command=update_funct,foreground="#000000",background="#d9d9d9",borderwidth="5",highlightcolor="black",pady="0",width=117)
        self.b4.configure(text='''Update Selected''')


        self.b5 = Button(top)
        self.b5.place(relx=0.68, rely=0.64, height=24, width=121)
        self.b5.configure(command=delete_funct,foreground="#000000",background="#d9d9d9",borderwidth="5",highlightcolor="black",pady="0",width=117)
        self.b5.configure(text='''Delete Selected''')


        self.b6 = Button(top)
        self.b6.place(relx=0.68, rely=0.73, height=24, width=120)
        self.b6.configure(command=root.destroy,foreground="#000000",background="#d9d9d9",borderwidth="5",highlightcolor="black",pady="0",width=117)
        self.b6.configure(text='''Close''')






# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = Pack.__dict__.keys() | Grid.__dict__.keys() \
                  | Place.__dict__.keys()
        else:
            methods = Pack.__dict__.keys() + Grid.__dict__.keys() \
                  + Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, Listbox):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

if __name__ == '__main__':
    vp_start_gui()
