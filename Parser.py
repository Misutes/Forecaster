import urllib.request
import os
import xml.etree.ElementTree as ET


def get_url():
    val_nm_rq = 'R01235'
    start_date = '01/02/2019'
    end_date = '01/02/2020'
    url = f'http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={start_date}&date_req2={end_date}&VAL_NM_RQ={val_nm_rq}'
    return url


def get_date(url):
    page = urllib.request.urlopen(url)
    raw_date = page.read()
    with open('Currency.xml', 'wb') as f:
        f.write(raw_date)
    date = ET.parse('Currency.xml')
    os.remove('Currency.xml')
    return date


def formation_date(date):
    main_branch = date.getroot()
    sub_branches = [element for element in main_branch]
    need_branches = [element.find('Value').text for element in sub_branches]
    rates = [float(value.replace(',', '.')) for value in need_branches]
    return rates


def get_exchange_rates():
    url = get_url()
    date = get_date(url)
    return formation_date(date)

