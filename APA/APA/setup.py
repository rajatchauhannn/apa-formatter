'''

Singh, V. P., Ranawat, R. P., Mathur, R. & Malhothara, S. (2020). How to be hot? Journal of hotness, 14(9), 560-570.
Singh, V. P., Ranawat, R. P., Mathur, R. & Malhothara, S. (2020). uses of hotness. Journal of hotness, 14(9), 560-570.
Singh, V. P., Ranawat, R. P., Mathur, R. & Malhothara, S. (2020). uses of hotness. Journal of hotness.
Singh, V. P., Ranawat, R. P., Mathur, R. & Malhothara, S. (2020). uses of hotness. Journal of hotness, 560-570.
Singh, V. P., Ranawat, R. P., Mathur, R. & Malhothara, S. (2020). uses of hotness. Journal of hotness, 14(9).

'''
import os
from tkinter import Tk, Label, Button, Entry, RIDGE, DISABLED, NORMAL, filedialog, END
class main_menu:
    def __init__(self, root):
        self.master = root
        root.title("APA")
        root.resizable(False, False)
        root.geometry('320x160')
        root.configure(background='#2B2B2B')

        vname = root.register(self.name_entry)

        self.label = Label(root, text="APA FORMATTER",bg = '#4D4D4D',fg = 'grey',font ='ariel 16 bold').place(x=0, y= 0, width = 320, height = 40,)
        self.name = Label(root, text='Name: ',bg = '#2B2B2B',fg = 'white',font='bold 10').place(x= 10, y =60 )
        self.name = Entry(root, validate="key", validatecommand=(vname, '%P'),bg = '#2B2B2B',fg = 'yellow',font='bold 10')
        self.name.place(x= 100, y =60 )

        self.path = os.path.dirname(os.path.abspath(__file__))
        self.dir = Label(root, text='Directory:',bg = '#2B2B2B',fg = 'white',font='bold 10').place(x= 10, y =90 )

        self.dir = Label(root, text=self.path,bg = '#2B2B2B',fg = '#F9F0D9',font='bold 10', )
        self.dir.place(x= 100, y =91 )


        self.browsebtn = Button(text = 'BROWSE',relief = RIDGE, state = NORMAL, bg = '#2B2B2B',fg ='white',font ='bold 10', command = lambda:[(APA_main_menu.select_path())])
        self.browsebtn.place(x=65,y=125, width =80, height = 30)

        self.startbtn = Button(text = 'START',relief = RIDGE, state = DISABLED, bg = '#2B2B2B',fg ='white',font ='bold 10', command = lambda:[(APA_main_menu.CLOSE(root), APA_main_menu.START())])

        self.startbtn.place(x=175,y=125, width =80, height = 30)

    def select_path(self):
        self.path = filedialog.askdirectory()
        if self.path == '':
            self.path = os.path.dirname(os.path.abspath(__file__))
        self.dir.config(text = self.path)
        self.startbtn.config(state = NORMAL)
    def CLOSE(self, root):
        root.destroy()

    def START(self):
        from APA.GUI import GUI


    def name_entry(self, name):
        try:
            self.name = name + '.docx'
            if self.name != '':
                main_menu.name = self.name
                self.startbtn.config(state = NORMAL)
                return True
            else:
                self.startbtn.config(state = DISABLED)
                main_menu.name = ''
                return True
        except:
            self.startbtn.config(state = DISABLED)
            self.name = None
            return False


if __name__ == '__main__':
    exit()
else:
    root = Tk()
    APA_main_menu = main_menu(root)
    root.mainloop()

