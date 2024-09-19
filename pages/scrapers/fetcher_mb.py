import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd





def mb():

    scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive']

    creds = ServiceAccountCredentials.from_json_keyfile_name('archive_key.json', scope)

    client = gspread.authorize(creds)

    sheet = client.open('manila_bulletin_archive').sheet1

    _scraped_dates = sheet.col_values(1)
    _article_dates = sheet.col_values(2)
    _urls = sheet.col_values(3)

    df = pd.DataFrame({'Scraped Date':_scraped_dates, 'Article Date':_article_dates, 'URL':_urls})

    return df


