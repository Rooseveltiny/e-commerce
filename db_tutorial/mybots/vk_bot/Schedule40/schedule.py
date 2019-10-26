
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
# import re
import xlrd

### this module allows to get schedule

def find_col_and_string(sheet, name):

    try:

        for col in range(0,100):

            cell = sheet.cell(2, col)
            if cell.value == name:

                return {'string': 2, 'col': col}


    except Exception as er:

        print("can't find! {}".format(er))
   
def get_clean_lists(list_one, list_two, list_three):

    list_one_new = []
    list_two_new = []
    list_three_middle = []   
    list_three_new = []

    for i, value in enumerate(list_one):

        if list_one[i] != "": #and list_two[i] != '': 

            list_one_new.append(value)

    for i, value in enumerate(list_two):

        if list_one[i] != "": 

            list_two_new.append(value)

    for i, value in enumerate(list_three):

        if value != "" and len(str(value)) <= 5:

            list_three_middle.append(value)

    list_three_new.append('')

    for i, value in enumerate(list_two_new[1:len(list_two_new)]):

        if value != '':

            if len(list_three_middle):

                list_three_new.append(list_three_middle.pop(0))

            else: 

                list_three_new.append("")

        else:

            list_three_new.append("")


    list_three_new = [ 'каб. ' + i if type(i) == str else 'каб. ' + str(int(i)) for i in list_three_new ]
    list_three_new = [i if len(i.replace(" ", "")) > 4 else "" for i in list_three_new]

    return list_one_new, list_two_new, list_three_new



def load_schedule_from_site():

    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
        }
        
    r = requests.get(url="https://s11028.edu35.ru/2013-06-12-15-17-31/raspisanie", headers = headers)
    soup = BeautifulSoup(r.content.decode('utf-8'), features = 'lxml')
    
    # soup = BeautifulSoup(html, "lxml")


    links = soup.findAll('a', {'class': 'at_url'})

    link = links[-1]['href']
    

    schedule = requests.get(link)
    out = open("schedule.xls", "wb")

    out.write(schedule.content)
    out.close()

def get_text(list_one, list_two, list_three):

    result = ''
    for i, value in enumerate(list_one):

        result = result + list_one[i] + ' - '+list_two[i]+ ' - '+str(list_three[i])+ '\n'

    return result

def get_schedule(grade):

    load_schedule_from_site()

    ###### FOR FORMAT XLS ######

    book = xlrd.open_workbook("schedule.xls")
    sheet = book.sheet_by_index(0)
    place_of_time = find_col_and_string(sheet, 'Время')
    place_of_objects = find_col_and_string(sheet, grade.lower())
    


    values_of_time = sheet.col_values(place_of_time.get('col'), start_rowx=place_of_time.get('string'), end_rowx=50)
    
    values_of_subjects = sheet.col_values(place_of_objects.get('col'), start_rowx = place_of_objects.get('string'), end_rowx=50)
    values_of_stadiums = sheet.col_values(place_of_objects.get('col') + 1, start_rowx = place_of_objects.get('string'), end_rowx=50)


    values_of_time, values_of_subjects, values_of_stadiums = get_clean_lists(values_of_time, values_of_subjects, values_of_stadiums)

    return get_text(values_of_time, values_of_subjects, values_of_stadiums)
  

if __name__ == '__main__':

    print(get_schedule('6г'))


