import gspread
from oauth2client.service_account import ServiceAccountCredentials

class Google_Auth():
    def __init__(self):
        self.secret = 'googleDriveAPI_secret.json'
        self.client = None

    def connect_gdrive(self):
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(self.secret, scope)
        self.client = gspread.authorize(creds)
  
    def fetchAll_url2miniurl(self, filename="miniurl"):
        # Find a workbook by name and open the first sheet
        # Make sure you use the right name here.
        sheet = self.client.open(filename).sheet1

        # Extract and print all of the values
        list_of_hashes = sheet.get_all_records()

        url2miniurl = {}
        for item in list_of_hashes:
            url2miniurl[item['orginalURL']] = item['miniURL']

        return url2miniurl
