import sys
import json
import requests

API_SIGNUP_URL = 'https://developer.nytimes.com/get-started'

class ArchiveAPI():
    def __init__(self, key):
        if key is None:
            raise Exception('Must provide an API key.             If you don\'t have one, go to {} to sign up for one'                            .format(API_SIGNUP_URL))
        else:
            self.key = key
            
    def fetch_articles(self, month, year):
        """
        month: integer 1-12
        year : integer 1851-2019
        
        returns a request object
        """
        
        resp = requests.get('https://api.nytimes.com/svc/archive/v1/2019/1.json?api-key={}'.format(self.key))
        print('inside fetch_articles')
        try:
            if resp.status_code != 200:
                print("Error:")
                if resp.status_code == 401:
                    raise Exception('Unauthorized request, check                    api-key is set.')
                if resp.status_code == 429:
                    raise Exception('Too many requests. You reached                     your per minute or per day rate limit.')
            else:
                return resp
        except:
            print('No Resp')

    def json_to_dataframe(self, json_file):
        """
        json_file:  a .json file which has been pulled from the Archive API and serialized in JSON format.
        """
        with open(json_file) as json_file:  
            data = json.load(json_file)
        return pd.DataFrame.from_dict(data['docs'])

if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv) != 4:
        raise IOError('User must specify API key, month, and year')
    API_KEY,MONTH,YEAR = sys.argv[1:]
    #TODO check that inputs are valid.
    archiveAPI = ArchiveAPI(API_KEY)
    articles = archiveAPI.fetch_articles(MONTH, YEAR)

    #TODO allow user to specify output dir
    with open('response.json', 'w') as outfile:
        json.dump(articles.json()['response'], outfile)
