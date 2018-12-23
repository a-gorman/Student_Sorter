import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_results(sheet_name,credential_file):

    scope = 'https://www.googleapis.com/auth/spreadsheets.readonly https://www.googleapis.com/auth/drive'

    credentials = ServiceAccountCredentials.from_json_keyfile_name(credential_file, scope)

    gc = gspread.authorize(credentials)

    wks = gc.open(sheet_name).sheet1

    return wks.get_all_values()