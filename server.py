from flask import Flask, request
from flask_restful import Resource, Api
from scholarly import search_author
import requests
import credentials

app = Flask(__name__)
api = Api(app)

CUSTOM_SEARCH_API_URL = 'https://www.googleapis.com/customsearch/v1/siterestrict'

class CustomSearchError(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message

def searchArticleURL(title):
    payload = {'key': credentials.GOOGLE_SEARCH_API_KEY,
                'cx': credentials.CUSTOM_SEARCH_ENGINE_ID,
                'q': title}
    response = requests.get(CUSTOM_SEARCH_API_URL, params=payload)
    data = dict(response.json())
    if 'error' in data:
        raise CustomSearchError(data['error']['code'], data['error']['message'])
    totalResults = int(data['searchInformation']['totalResults'])
    if totalResults > 0:
        return data['items'][0]['link']
    else:
        return ''

class Author(Resource):
    def get(self):
        try:
            author_name = request.args.get('name')
            search_query = search_author(author_name)
            author = next(search_query).fill()
            articles = []
            for pub in author.publications:
                title = pub.bib['title']
                articleURL = searchArticleURL(title)
                if articleURL:
                    article = {'title': title,
                            'year': pub.bib['year'] if 'year' in pub.bib else '',
                            'citationCount': pub.citedby if hasattr(pub, 'citedby') else '',
                            'url': articleURL}
                    articles.append(article)
            result = {'name': author.name,
                    'hIndex': author.hindex,
                    'citationCount': author.citedby,
                    'citesPerYear': author.cites_per_year,
                    'articles': articles}
            return result, 200, {'Access-Control-Allow-Origin': '*'}
        except StopIteration:
            return {'error': 'No Google Scholar profile found'}, 200, {'Access-Control-Allow-Origin': '*'}
        except CustomSearchError as err:
             return {'error': err.message }, err.code, {'Access-Control-Allow-Origin': '*'}

api.add_resource(Author, '/author')

if __name__ == '__main__':
    app.run(port='5002')
