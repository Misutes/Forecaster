import urllib.request
import os
import xml.etree.ElementTree as ET


val_nm_rq = 'R01235'
# creation url
def get_url():
    start_date = '01/01/2016'
    end_date = '01/01/2018'
    url = f'http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={start_date}&date_req2={end_date}&VAL_NM_RQ={val_nm_rq}'
    return url


# parsing web-page from url
def get_date(url, name):
    page = urllib.request.urlopen(url)
    raw_date = page.read()
    with open(f'{name}.xml', 'wb') as f:
        f.write(raw_date)
    date = ET.parse(f'{name}.xml')
    os.remove(f'{name}.xml')
    return date


# creation list of exchange rates from date
def formation_date(date, branch):
    main_branch = date.getroot()
    sub_branches = [element for element in main_branch]
    need_branches = [element.find(f'{branch}').text for element in sub_branches]
    return need_branches


# general function
def get_exchange_rates():
    url = get_url()
    date = get_date(url, 'Currency')
    rates = [float(value.replace(',', '.')) for value in formation_date(date, 'Value')]
    return rates


def get_val_list():
    url = 'http://www.cbr.ru/scripts/XML_val.asp?d=0'
    date = get_date(url, 'val_list')
    name = formation_date(date, 'Name')
    code = formation_date(date, 'ParentCode')
    val = {}
    for (n, c) in zip(name, code):
        val[n] = c
    return val


