import gspread
from oauth2client.service_account import ServiceAccountCredentials

class Google_Sheet():
    def __init__(self):
        self.secret = 'googleDriveAPI_secret.json'
        self.sheet = None

    def connect_gsheets(self, filename="miniurl"):
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(self.secret, scope)
        client = gspread.authorize(creds)
        self.sheet = client.open(filename).sheet1
  
    def fetchAll_url2miniurl(self):
        list_of_records = self.sheet.get_all_records()
        totalRecord = len(list_of_records) +2 

        url2miniurl = {}
        for record in list_of_records:
            url2miniurl[record['orginalURL']] = record['miniURL']

        return totalRecord, url2miniurl

    def write2gsheet(self, orginalURL, miniURL):
        lastrow = len(self.sheet.get_all_records()) +2
        data = [orginalURL,miniURL]

        self.sheet.insert_row(data, lastrow)

# testing
def main():
    gsheet = Google_Sheet()
    gsheet.connect_gsheets()
    print(gsheet.fetchAll_url2miniurl())

if __name__ == "__main__":
    main()