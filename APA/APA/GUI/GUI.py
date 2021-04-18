from tkinter import Tk, Label, Button, Entry, scrolledtext, DISABLED, LEFT, FLAT, NORMAL, Text, END, INSERT, RAISED, RIDGE, GROOVE, Checkbutton, READABLE

from APA.APA import APA
from APA import setup

class main:
    topic_value, name_value, year_value, book_value, volume_value, issue_value, page_value = '','','','','','',''


    def __init__(self, root):
        self.master = root
        root.title("APA")
        root.resizable(False, False)
        root.geometry('1024x600')
        root.configure(background='#2B2B2B')


        self.label = Label(root, text="APA FORMATTER",bg = '#4D4D4D',fg = 'grey',font ='ariel 19 bold').place(x=0, y= 0, width = 1050, height = 40,)


        self.submitbtn = Button(text = 'SUBMIT',relief = RIDGE, state = DISABLED, bg = '#2B2B2B',fg ='white',font ='bold 10', command = lambda:[(APA_inputs.enter_txt())])
        self.submitbtn.place(x=90,y=550, width =80, height = 30)

        self.savebtn = Button(text = 'SAVE',relief = RIDGE, state = DISABLED, bg = '#2B2B2B',fg ='green',font ='bold 10', command = lambda:[(APA_txt.save_txt())])
        self.savebtn.place(x=190,y=550, width =80, height = 30)

        self.exitbtn = Button(text = 'EXIT',relief = RIDGE, state = NORMAL, bg = '#2B2B2B',fg ='white',font ='bold 10', command = lambda:[(exit()), root.destroy()])
        self.exitbtn.place(x=290,y=550, width =80, height = 30)

        self.label= Label(text = setup.APA_main_menu.name, bg = '#2B2B2B',fg ='white',font ='bold 10').place(x=700,y=50)

class verify:
    def __init__(self, root):
        self.verify_name1 = Label(root, fg = 'green', bg ='#2B2B2B', bd=0, font ='bold 18', state = DISABLED)
        self.verify_name1.place(x=360, y =77)

        self.verify_name2 = Label(root, fg = 'green', bg ='#2B2B2B', bd=0, font ='bold 18', state = DISABLED)
        self.verify_name2.place(x=360, y =107)

        self.verify_name3 = Label(root, fg = 'green', bg ='#2B2B2B', bd=0, font ='bold 18', state = DISABLED)
        self.verify_name3.place(x=360, y =137)

        self.verify_name4 = Label(root, fg = 'green', bg ='#2B2B2B', bd=0, font ='bold 18', state = DISABLED)
        self.verify_name4.place(x=360, y =167)

        self.verify_year = Label(root, fg = 'green', bg ='#2B2B2B', bd=0, font ='bold 18', state = DISABLED)
        self.verify_year.place(x=220, y =217)

        self.verify_volume = Label(root, fg='green', bg='#2B2B2B', bd=0, font='bold 18', state=DISABLED)
        self.verify_volume.place(x=220, y=427)

        self.verify_issue = Label(root, fg='green', bg='#2B2B2B', bd=0, font='bold 18', state=DISABLED)
        self.verify_issue.place(x=220, y=457)

        self.verify_page = Label(root, fg='green', bg='#2B2B2B', bd=0, font='bold 18', state=DISABLED)
        self.verify_page.place(x=220, y=487)

        self.etal = Checkbutton(root, text = 'Et.al?',bg = '#2B2B2B',fg = 'orange',font='bold 12', bd = 0,activebackground='#2B2B2B', activeforeground = 'orange', command = lambda:[APA_inputs.hide_names()])
        self.etal.place(x= 110, y = 195)
        self.et_al = False



class entries(main, verify):


    def __init__(self, root):
        super().__init__(root)
        verify.__init__(self, root)

        self.name1 = Label(root, text='First Name:',bg = '#2B2B2B',fg = '#F9F0D9',font='bold 10').place(x= 10, y =80 )
        self.name2 = Label(root, text="Second Name:",bg = '#2B2B2B',fg = '#F9F0D9',font='bold 10').place(x= 10, y =110 )
        self.name3 = Label(root, text="Third Name:",bg = '#2B2B2B',fg = '#F9F0D9',font='bold 10').place(x= 10, y = 140)
        self.name4 = Label(root, text="Fourth Name:",bg = '#2B2B2B',fg = '#F9F0D9',font='bold 10').place(x= 10, y = 170)
        self.year = Label(root, text='Year:',bg = '#2B2B2B',fg = '#B0B9D9',font='bold 10').place(x= 10, y = 220)
        self.topic = Label(root, text="Topic(s):",bg = '#2B2B2B',fg = '#F8D8C0',font='bold 10').place(x= 10, y = 250)
        self.book = Label(root, text="Book(s):",bg = '#2B2B2B',fg = '#F8D8C0',font='bold 10').place(x= 10, y = 330)
        self.volume = Label(root, text="Volume(s):",bg = '#2B2B2B',fg = '#B0D9D9',font='bold 10').place(x= 10, y = 430)
        self.issue = Label(root, text="Issue(s):",bg = '#2B2B2B',fg = '#B0D9D9',font='bold 10').place(x= 10, y = 460)
        self.page = Label(root, text="Page(s)",bg = '#2B2B2B',fg = '#B0D9D9',font='bold 10').place(x= 10, y = 490)


        self.req = Label(root, text = '*', fg = 'orange', bg = '#2B2B2B', bd = 0) .place(x=85, y=80)
        self.req = Label(root, text = '*', fg = 'orange', bg = '#2B2B2B', bd = 0).place(x=100, y=110)
        self.req = Label(root, text = '*', fg = 'orange', bg = '#2B2B2B', bd = 0).place(x=85, y=140)
        self.req = Label(root, text = '*', fg = 'orange', bg = '#2B2B2B', bd = 0).place(x=95, y=170)
        self.req = Label(root, text = '*', fg = 'orange', bg = '#2B2B2B', bd = 0).place(x=70, y=250)
        self.req = Label(root, text = '*', fg = 'orange', bg = '#2B2B2B', bd = 0).place(x=70, y=330)


        vname1 = root.register(self.name1_entry)
        vname2 = root.register(self.name2_entry)
        vname3 = root.register(self.name3_entry)
        vname4 = root.register(self.name4_entry)
        vyear = root.register(self.year_entry)
        vtopic = root.register(self.topic_entry)
        vbook = root.register(self.book_entry)
        vvolume = root.register(self.volume_entry)
        vissue = root.register(self.issue_entry)
        vpage = root.register(self.page_entry)


        self.iname1 = Entry(root, validate="key", validatecommand=(vname1, '%P'),width = 40,bg = '#3C3F41',fg = 'yellow',relief = FLAT,highlightbackground='#2B2B2B',highlightthickness = 0.5,highlightcolor = 'black')
        self.iname1.place(x= 110, y =80 )
        self.iname2 = Entry(root,validate = "key", validatecommand=(vname2, '%P'),width = 40,bg = '#3C3F41',fg = 'yellow',relief = FLAT,highlightbackground='#2B2B2B',highlightthickness = 0.5,highlightcolor = 'black')
        self.iname2.place(x= 110, y =110 )
        self.iname3 = Entry(root,validate = "key", validatecommand=(vname3, '%P'),width = 40,bg = '#3C3F41',fg = 'yellow',relief = FLAT,highlightbackground='#2B2B2B',highlightthickness = 0.5,highlightcolor = 'black')
        self.iname3.place(x= 110, y =140 )
        self.iname4 = Entry(root,validate = "key", validatecommand=(vname4, '%P'),width = 40,bg = '#3C3F41',fg = 'yellow',relief = FLAT,highlightbackground='#2B2B2B',highlightthickness = 0.5,highlightcolor = 'black')
        self.iname4.place(x= 110, y =170 )
        self.year = Entry(root,validate = "key", validatecommand=(vyear, '%P'),width = 20,bg = '#3C3F41',fg = 'yellow',relief = FLAT,highlightbackground='#2B2B2B',highlightthickness = 0.5,highlightcolor = 'black').place(x= 90, y = 220)
        self.topic = Entry(root,validate = "key", validatecommand=(vtopic, '%P'),bg = '#3C3F41',fg = 'yellow',relief = FLAT,highlightbackground='#2B2B2B',highlightthickness = 0.5,highlightcolor = 'black').place(width = 304, height = 70, x= 90, y = 250)
        self.book = Entry(root,validate = "key", validatecommand=(vbook, '%P'),bg = '#3C3F41',fg = 'yellow',relief = FLAT,highlightbackground='#2B2B2B',highlightthickness = 0.5,highlightcolor = 'black').place(width = 304,height = 70,x= 90, y = 330)
        self.volume = Entry(root,validate = "key", validatecommand=(vvolume, '%P'),width = 20,bg = '#3C3F41',fg = 'yellow',relief = FLAT,highlightbackground='#2B2B2B',highlightthickness = 0.5,highlightcolor = 'black').place(x= 90, y = 430)
        self.issue = Entry(root,validate = "key", validatecommand=(vissue, '%P'),width = 20,bg = '#3C3F41',fg = 'yellow',relief = FLAT,highlightbackground='#2B2B2B',highlightthickness = 0.5,highlightcolor = 'black').place(x= 90, y = 460)
        self.page = Entry(root,validate = "key", validatecommand=(vpage, '%P'),width = 20,bg = '#3C3F41',fg = 'yellow',relief = FLAT,highlightbackground='#2B2B2B',highlightthickness = 0.5,highlightcolor = 'black').place(x= 90, y = 490)

        self.verify_name1.config(text = '☐')
        self.verify_name2.config(text = '☐')
        self.verify_name3.config(text = '☐')
        self.verify_name4.config(text = '☐')
        self.verify_year.config(text='☐')
        self.verify_volume.config(text='☐')
        self.verify_issue.config(text='☐')
        self.verify_page.config(text='☐')


        self.correctname1 = self.correctname2 = self.correctname3 = self.correctname4 = self.correcttopic = self.correctbook= self.correctyear = self.correctyear = self.correctissue = self.correctpage = ' '

    def name1_entry(self, name1):
        try:
            if name1 != None:
                self.name1 = name1
                if self.et_al == True:
                    self.name2 = self.name3 = self.name4 = None
                self.correctname1 = APA.nameAPA(name1, self.name2, self.name3, self.name4)

                if self.name1 == '':
                    self.verify_name1.config(text='☐', state = DISABLED)

                else:
                    self.verify_name1.config(text='☑', state = NORMAL)

                if self.correctname1 != ' ':
                    if(self.correcttopic != ' ' or self.correctbook != ' '):
                        main.name_value = self.correctname1
                        self.submitbtn.config(state=NORMAL, relief = RAISED)

                else:
                    self.submitbtn.config(state=DISABLED, relief = RIDGE)
                print(self.correctname1)
                main.name_value = self.correctname1

                return True
            else:
                return False
        except IndexError:
            self.name1 = None
            return True

    def name2_entry(self, name2):
        try:
            if name2 != None:
                self.name2 = name2
                if self.et_al == True:
                    self.name2 = self.name3 = self.name4 = None
                self.correctname2 = APA.nameAPA(self.name1, name2, self.name3, self.name4)
                if self.name2 == '':
                    self.verify_name2.config(text='☐', state = DISABLED)

                else:
                    self.verify_name2.config(text='☑', state = NORMAL)

                if self.correctname2 != ' ':
                    if(self.correcttopic != ' ' or self.correctbook != ' '):
                        main.name_value = self.correctname2
                        self.submitbtn.config(state=NORMAL, relief = RAISED)
                else:
                    self.submitbtn.config(state=DISABLED, relief = RIDGE)
                main.name_value = self.correctname2
                print(self.correctname2)

                return True
            else:
                return False
        except IndexError:
            self.name2 = None
            return True

    def name3_entry(self, name3):
        try:
            if name3 != None:
                self.name3 = name3
                if self.et_al == True:
                    self.name2 = self.name3 = self.name4 = None
                self.correctname3 = APA.nameAPA(self.name1, self.name2, name3, self.name4)
                if self.name3 == '':
                    self.verify_name3.config(text='☐', state = DISABLED)

                else:
                    self.verify_name3.config(text='☑', state = NORMAL)

                if(self.correcttopic != ' ' and self.correctbook != ' '):
                    main.name_value = self.correctname3
                    self.submitbtn.config(state=NORMAL, relief = RAISED)
                else:
                    self.submitbtn.config(state=DISABLED, relief = RIDGE)
                main.name_value = self.correctname3
                print(self.correctname3)
                return True
            else:
                return False
        except IndexError:
            self.name3 = None
            return True

    def name4_entry(self, name4):
        try:
            if name4 != None:
                self.name4 = name4
                if self.et_al == True:
                    self.name2 = self.name3 = self.name4 = None
                self.correctname4= APA.nameAPA(self.name1, self.name2, self.name3, name4)
                if self.name4 == '':
                    self.verify_name4.config(text='☐', state = DISABLED)

                else:
                    self.verify_name4.config(text='☑', state = NORMAL)

                if(self.correcttopic != ' ' and self.correctbook != ' '):
                    main.name_value = self.correctname4
                    self.submitbtn.config(state=NORMAL, relief = RAISED)

                else:
                    self.submitbtn.config(state=DISABLED, relief = RIDGE)
                main.name_value = self.correctname4
                print(self.correctname4)
                return True
            else:
                return False
        except IndexError:
            self.name4 = None
            return True

    def year_entry(self, year):
        try:
            if year != None:
                main.year_value = ''
                self.year = year
                self.correctyear = APA.yearAPA(year)
                if self.correctyear == 'Invalid Year':
                    self.verify_year.config(text='☒',fg = '#8B0000', state = NORMAL)
                else:
                    self.verify_year.config(text='☑',fg = 'green', state = NORMAL)
                    main.year_value = self.correctyear
                print(self.correctyear)

                self.year = ''
                return True
            else:
                return False
        except IndexError:
            self.verify_year.config(text='☐', state=DISABLED)
            return True

    def topic_entry(self, topic):
        try:
            if topic != None:
                self.topic = topic
                self.correcttopic = APA.topicAPA(topic)
                if self.correcttopic != 'Err(Low)':
                    if(self.correctname1 != ' ' or self.correctname2 != ' ' or self.correctname3 != ' ' or self.correctname4 != ' '):
                        if self.correctbook != ' ':
                            main.topic_value = self.correcttopic
                            self.submitbtn.config(state=NORMAL, relief = RAISED)
                else:
                    self.submitbtn.config(state=DISABLED, relief = RIDGE)
                main.topic_value = self.correcttopic
                print(self.correcttopic)

                return True
            else:
                self.submitbtn.config(state=DISABLED)
                return False
        except IndexError:
            self.topic = None
            return True
    def book_entry(self, book):
        try:
            if book != None:
                self.book = book
                self.correctbook = APA.bookAPA(book)
                if self.correctbook != 'Err(Low)':
                    if(self.correctname1 != ' ' or self.correctname2 != ' ' or self.correctname3 != ' ' or self.correctname4 != ' ' and self.correcttopic != ' '):
                        main.book_value = self.correctbook
                        self.submitbtn.config(state=NORMAL, relief = RAISED)
                else:
                    self.submitbtn.config(state=DISABLED, relief = RIDGE)
                main.book_value = self.correctbook
                print(self.correctbook)
                return True
            else:
                return False
        except:
            return True

    def volume_entry(self, volume):
        try:
            if volume != None:
                self.volume = volume
                self.correctvolume = APA.volumeAPA(volume)
                if self.correctvolume == 'Invalid Volume':
                    self.verify_volume.config(text='☒',fg = '#8B0000', state = NORMAL)
                    main.volume_value = ''
                elif self.correctvolume == '':
                    self.verify_volume.config(text='☐', state=DISABLED)
                    main.volume_value = ''
                else:
                    self.verify_volume.config(text='☑',fg = 'green', state = NORMAL)
                    main.volume_value = self.correctvolume
                print(self.correctvolume)
                return True
            else:
                return False
        except IndexError:
            self.verify_volume.config(text='☐', state=DISABLED)
            return True

    def issue_entry(self, issue):
        try:
            if issue != None:
                self.issue = issue
                self.correctissue = APA.issueAPA(issue)
                if self.correctissue == 'Invalid Issue':
                    self.verify_issue.config(text='☒',fg = '#8B0000', state = NORMAL)
                    main.issue_value = ''
                elif self.correctissue == '':
                    self.verify_issue.config(text='☐', state=DISABLED)
                    main.issue_value = ''
                else:
                    self.verify_issue.config(text='☑',fg = 'green', state = NORMAL)
                    main.issue_value = self.correctissue
                print(self.correctissue)
                return True
            else:
                return False
        except IndexError:
            return True

    def page_entry(self, page):
        try:
            if page != None:
                self.page = page
                self.correctpage = APA.pageAPA(page)
                if self.correctpage == 'Invalid Page':
                    self.verify_page.config(text='☒',fg = '#8B0000', state = NORMAL)
                    main.page_value = ''
                elif self.correctpage == '':
                    self.verify_page.config(text='☐', state=DISABLED)
                    main.page_value = ''
                else:
                    self.verify_page.config(text='☑',fg = 'green', state = NORMAL)
                    main.page_value = self.correctpage
                print(self.correctpage)
                return True
            else:
                return False
        except IndexError:
            return True

    def enter_txt(self):
        if self.et_al == False:
            total_txt = main.name_value + main.year_value + main.topic_value + main.book_value + main.volume_value + main.issue_value + main.page_value + '\n' + '\n'
        elif self.et_al == True:
            total_txt = main.name_value + 'et.al. ' + main.year_value + main.topic_value + main.book_value + main.volume_value + main.issue_value + main.page_value + '\n' + '\n'
        APA_txt.set_txt(total_txt)
        APA_inputs.__init__(root)
        self.savebtn.config(state =NORMAL, relief = RAISED)

    def hide_names(self):

        self.et_al = True
        self.correctname1 = self.correctname2 = self.correctname3 = self.correctname4 = ' '
        self.name1 = self.iname1.get()
        APA_inputs.name1_entry(self.name1)
        self.iname2.config(state = DISABLED, disabledbackground = '#4F4B41')
        self.iname3.config(state = DISABLED, disabledbackground = '#4F4B41')
        self.iname4.config(state = DISABLED, disabledbackground = '#4F4B41')
        self.etal = Checkbutton(root,  text = 'Et.al?',bg = '#2B2B2B',fg = 'orange',font='bold 12', bd = 0,activebackground='#2B2B2B', activeforeground = 'orange', command = lambda:[APA_inputs.show_names()])
        self.etal.select()
        self.etal.place(x= 110, y = 195)


    def show_names(self):

        self.et_al = False
        self.iname2.config(state = NORMAL)
        self.iname3.config(state = NORMAL)
        self.iname4.config(state = NORMAL)

        self.name1 = self.iname1.get()
        self.name2 = self.iname2.get()
        self.name3 = self.iname3.get()
        self.name4 = self.iname4.get()

        APA_inputs.name1_entry(self.name1)
        APA_inputs.name2_entry(self.name2)
        APA_inputs.name3_entry(self.name3)
        APA_inputs.name4_entry(self.name4)


        self.etal = Checkbutton(root, text = 'Et.al?',bg = '#2B2B2B',fg = 'orange',font='bold 12', bd = 0,activebackground='#2B2B2B', activeforeground = 'orange', command = lambda:[APA_inputs.hide_names()])
        self.etal.deselect()
        self.etal.place(x= 110, y = 195)



class txt:
    def __init__(self, root):
        self.txt = scrolledtext.ScrolledText(root,state = NORMAL, relief = FLAT,bg = '#4F4B41',fg = '#999900',highlightbackground='#2B2B2B',highlightthickness = 1,highlightcolor = 'black', width=67, height=30)
        self.txt.place(x = 450,y = 80)
        self.txt.insert(END, main.topic_value)
        self.txt.config(state = DISABLED)
        self.chathead = setup.APA_main_menu.name
    def set_txt(self, total_txt):
        self.txt.config(state = NORMAL)
        self.txt.insert(END, total_txt)
        self.all_txt = self.txt.get('1.0', END)
        self.txt.config(state= DISABLED)


    def save_txt(self):
        file = open(setup.APA_main_menu.path + '\\' +self.chathead, 'a+')
        file.write(self.all_txt)
        file.close()
        self.txt = scrolledtext.ScrolledText(root,state = NORMAL, relief = FLAT,bg = '#4F4B41',fg = '#999900',highlightbackground='#2B2B2B',highlightthickness = 1,highlightcolor = 'black', width=67, height=30)
        self.txt.place(x = 450,y = 80)



while setup.APA_main_menu.name != None and type(setup.APA_main_menu.name) == str:
    root = Tk()
    APA_gui = main(root)
    APA_inputs = entries(root)
    APA_txt = txt(root)
    APA_verify = verify(root)
    setup.APA_main_menu.name = None
    root.mainloop()
