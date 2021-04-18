''''
Leonhard, D., & Brugger, P. (1998). Creative, paranormal, and delusional thought: A consequence of right
hemisphere semantic activation? Neuropsychiatry, Neuropsychology, & Behavioral Neurology, 11(4), 177–183.
'''

# TODO CREATE BROWSE BUTTON AND SUBMIT BUTTON
# TODO ADD ET.AL OPTION WHEN SIS IS AWAKE
# TODO CREATE AN ACTIVE ERROR FEEDBACK

from datetime import date

#Variables

class naming:

    def __init__(self, first=None, second=None, third=None, fourth=None):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth



    def correct_names(self):
        corrected_1, corrected_2, corrected_3, corrected_4 = [], [], [], []
        if self.first != None:
            self.first = self.first.split()
            for i in self.first:
                if i == self.first[0]:
                    i += ', '
                i = i.capitalize()
                if i != self.first[0].capitalize() + ', ':
                    if i[-1] != '.':
                        i += '.'
                        corrected_1.append(i)
                    else:
                        corrected_1.append(i)
                else:
                    corrected_1.append(i)

        if self.second !=None:
            self.second = self.second.split()
            for i in self.second:
                if i == self.second[0]:
                    i += ', '
                i = i.capitalize()
                if i != self.second[0].capitalize() + ', ':
                    if i[-1] != '.':
                        i += '.'
                        corrected_2.append(i)
                    else:
                        corrected_2.append(i)
                else:
                    corrected_2.append(i)

        if self.third != None:
            self.third = self.third.split()
            for i in self.third:
                if i == self.third[0]:
                    i += ', '
                i = i.capitalize()
                if i != self.third[0].capitalize() + ', ':
                    if i[-1] != '.':
                        i += '.'
                        corrected_3.append(i)
                    else:
                        corrected_3.append(i)
                else:
                    corrected_3.append(i)
        if self.fourth != None:
            self.fourth = self.fourth.split()
            for i in self.fourth:
                if i == self.fourth[0]:
                    i += ', '
                i = i.capitalize()
                if i != self.fourth[0].capitalize() + ', ':
                    if i[-1] != '.':
                        i += '.'
                        corrected_4.append(i)
                    else:
                        corrected_4.append(i)
                else:
                    corrected_4.append(i)

        return corrected_1, corrected_2, corrected_3, corrected_4





    def append_names(self):

        appended_name = ''
        if self.fourth != None and self.third == '' and self.second == '' and self.first == '':
            appended_name = self.fourth + ' '
        elif self.fourth == '' and self.third != None and self.second == '' and self.first == '':
            appended_name = self.third + ' '
        elif self.fourth == '' and self.third == '' and self.second != None and self.first == '':
            appended_name = self.second + ' '
        elif self.fourth == '' and self.third == '' and self.second == '' and self.first != None:
            appended_name = self.first + ' '

        elif self.fourth != None and self.third != None and self.second == '' and self.first == '':
            appended_name = self.third + ' & ' + self.fourth
        elif self.fourth != None and self.third == '' and self.second != None and self.first == '':
            appended_name = self.second + ' & ' + self.fourth
        elif self.fourth != None and self.third == '' and self.second == '' and self.first != None:
            appended_name = self.fourth + ' & ' + self.first
        elif self.fourth == '' and self.third != None and self.second != None and self.first == '':
            appended_name = self.third + ' & ' + self.second
        elif self.fourth == '' and self.third != None and self.second == '' and self.first != None:
            appended_name = self.third + ' & ' + self.first
        elif self.fourth == '' and self.third == '' and self.second != None and self.first != None:
            appended_name = self.second + ' & ' + self.first

        elif self.fourth != None and self.third != None and self.second != None and self.first == '':
            appended_name = self.second + ', ' + self.third + ' & ' +  self.fourth
        elif self.fourth == '' and self.third != None and self.second != None and self.first != None:
            appended_name = self.first + ', ' + self.second + ' & ' +  self.third
        elif self.fourth != None and self.third != None and self.second == '' and self.first != None:
            appended_name = self.first + ', ' + self.second + ' & ' +  self.fourth
        elif self.fourth != None and self.third == '' and self.second != None and self.first != None:
            appended_name = self.first + ', ' + self.second + ' & ' +  self.fourth

        elif self.fourth != None and self.third != None and self.second != None and self.first != None:
            appended_name = self.first + ', ' + self.second + ', ' + self.third + ' & ' + self.fourth
        else:
            return appended_name

        return appended_name

def nameAPA(name1=None, name2=None, name3=None, name4=None):
    if name4 != None:
        name_string = naming(name1, name2, name3, name4)
        tuple = name_string.correct_names()
        corrected__1 = tuple[0]
        corrected__2 = tuple[1]
        corrected__3 = tuple[2]
        corrected__4 = tuple[3]
        name_string = naming(' '.join(corrected__1),' '.join(corrected__2), ' '.join(corrected__3),' '.join(corrected__4))
        return name_string.append_names()

    elif name3 != None:
        name_string = naming(name1, name2, name3)
        tuple = name_string.correct_names()
        corrected__1 = tuple[0]
        corrected__2 = tuple[1]
        corrected__3 = tuple[2]
        name_string = naming(' '.join(corrected__1),' '.join(corrected__2), ' '.join(corrected__3), '')
        return name_string.append_names()

    elif name2 != None:
        name_string = naming(name1, name2)
        tuple = name_string.correct_names()
        corrected__1 = tuple[0]
        corrected__2 = tuple[1]
        name_string = naming(' '.join(corrected__1),' '.join(corrected__2), '', '')
        return name_string.append_names()

    elif name1 != None:
        name_string = naming(name1)
        tuple = name_string.correct_names()
        corrected__1 = tuple[0]
        name_string = naming(' '.join(corrected__1), '', '','')
        return name_string.append_names()

    else:
        name_string = naming()
        return name_string


class cls_year:
    EOL = '. '
    def __init__(self, year):
        self.year = year

    def correct_year(self):
        if self.year != None:
            current_year = date.today().year
            if self.year[0] == '(' and self.year[-1] == ')' and len(self.year[1:5]) == 4 and self.year[1:5].isdigit() and int(self.year[1:5]) <= current_year:
                self.year += cls_year.EOL
                return self.year
            elif len(self.year) == 4 and self.year.isdigit() and int(self.year) <= current_year:
                self.year = '(' + self.year + ')'
                self.year += cls_year.EOL
                return self.year
            else:
                return 'Invalid Year'
        return 'Invalid Year'



def yearAPA(year):
    year_string = cls_year(year)
    return year_string.correct_year()




class cls_topic:

    def __init__(self, topic):
        self.topic = topic


    def correct_topic(self):
        if self.topic != '':
            if self.topic[-1] == '.' or self.topic[-1] == '?' or self.topic[-1] == '!':
                self.topic.split()
                splt = self.topic.replace(self.topic[0], self.topic[0].capitalize(), 1)
                ''.join(splt)
                splt += ' '
                return splt
            else:
                self.topic += '. '
                self.topic.split()
                splt = self.topic.replace(self.topic[0], self.topic[0].capitalize(), 1)
                ''.join(splt)
                return splt
        else:
            return 'Err(Low)'

def topicAPA(topic):
    topic_string = cls_topic(topic)
    return topic_string.correct_topic()





class cls_book:
    EOL = ', '
    def __init__(self, book):
        self.book = book

    def correct_book(self):
        if self.book != '':
            self.book.split()
            splt = self.book.replace(self.book[0], self.book[0].capitalize(), 1)
            print(splt)
            ''.join(splt)
            if cls_volume.volume_avail == False and cls_issue.issue_avail == False and cls_page.page_avail == False:
                cls_book.EOL = '. '
                self.book = splt + cls_book.EOL
                return self.book
            else:
                self.book = splt + cls_book.EOL
                return self.book
        else:
            return 'Err(Low)'


def bookAPA(book):
    book_string = cls_book(book)
    return book_string.correct_book()







class cls_volume:
    volume_avail = False
    EOL = ', '

    def __init__(self, volume):
        self.volume = volume

    def correct_volume(self):
        if self.volume.isnumeric():
            cls_volume.volume_avail = True
            if cls_page.page_avail == False and cls_issue.issue_avail == False:
                cls_volume.EOL = '. '
                self.volume += cls_volume.EOL
                return self.volume
            else:
                cls_volume.EOL = ''
                self.volume += cls_volume.EOL
                return self.volume
        elif self.volume == '':
            return self.volume
        return 'Invalid Volume'


def volumeAPA(volume):
    volume_string = cls_volume(volume)
    return volume_string.correct_volume()









class cls_issue:
    issue_avail = False
    EOL = ', '

    def __init__(self, issue):
        self.issue = issue

    def correct_issue(self):
        if cls_page.page_avail == False:
            cls_issue.EOL = '. '
        if self.issue != '':
            cls_issue.issue_avail = True
            if self.issue[0] == '(' and self.issue[-1] ==')':
                self.issue += cls_issue.EOL
                return self.issue
            elif self.issue.isnumeric():
                self.issue = '(' + self.issue + ')' + cls_issue.EOL
                cls_issue.issue_avail = True
                return self.issue
        else:
            return self.issue
        return 'Invalid Issue'

def issueAPA(issue):
    issue_string = cls_issue(issue)
    return issue_string.correct_issue()








class cls_page:
    page_avail = False
    def __init__(self, page):
        self.page = page

    def correct_page(self):
        if self.page != '':
            splt = self.page.replace('-','')
            if splt.isnumeric():
                cls_page.page_avail = True
                self.page += '.'
                self.page.split()
                splt = self.page.replace(self.page[0], self.page[0].capitalize(), 1)
                ''.join(splt)
                return splt
            else:
                return 'Invalid Page'
        return ''

def pageAPA(page):
    page_string = cls_page(page)
    return page_string.correct_page()









