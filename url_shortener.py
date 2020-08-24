

class URL_Shortener():

    def __init__(self):
        self.url2miniurl = None
        self.id = 1

    def shortener_url(self, formData):
        orginal_url = formData['orginalURL']
        extension = formData['extension']
        update = False
        if(orginal_url[-1]=="/"):
            orginal_url = orginal_url[:-1]
        if(orginal_url in self.url2miniurl):
            miniurl = self.url2miniurl[orginal_url]
        else:
            update = True
            if(extension):
                miniurl = extension
            else:
                miniurl = self.encode(self.id)
                self.id += 1
            self.url2miniurl[orginal_url] = miniurl
            

        return update, orginal_url, miniurl

    def encode(self, id):
        char = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        base = len(char)

        ret = []

        while id > 0:
            val = id % base
            ret.append(char[val])
            id = id//base
            leadingzero = (3 - len(str(id))) * "0"

        return leadingzero + "".join(ret[::-1])

    def getOrginalURL(self, extension):
        # print(self.url2miniurl)
        mini2orginalURL = {v: k for k, v in self.url2miniurl.items()}
        if(extension in mini2orginalURL):
            orginalURL = mini2orginalURL[extension]
        else:
            orginalURL = None

        return orginalURL
