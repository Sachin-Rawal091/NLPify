import json

class Database:

    def add_data(self,name,email,passowrd):

        with open(r'NLPAPP\nlp.json','r') as rd:
            database = json.load(rd)
        if not email or email in database:
            return 0
        else:
            database[email] = [name,passowrd]
            with open(r'NLPAPP\nlp.json','w') as wd:
                json.dump(database,wd)
            return 1

    def search(self,email,password):
        with open(r'NLPAPP\nlp.json','r') as rf:
            database = json.load(rf)
            if email in database:
                if database[email][1] == password:
                    return 1 
                else:
                    return 0 
            else :
                return 0