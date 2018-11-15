from flask import Flask, request
from flask_restful import Resource, Api
from scholarly import search_author


app = Flask(__name__)
api = Api(app)


class Author(Resource):
    def get(self):
        try:
            author_name = request.args.get('name')
            search_query = search_author(author_name)
            author = next(search_query).fill()
            articles = [{'title': pub.bib['title'],
                        'year': pub.bib['year'] if 'year' in pub.bib else '',
                        'citationCount': pub.citedby if hasattr(pub, 'citedby') else ''}
                        for pub in author.publications]
            result = {'name': author.name,
                    'hIndex': author.hindex,
                    'citationCount': author.citedby,
                    'citesPerYear': author.cites_per_year,
                    'articles': articles}
            return result, 200, {'Access-Control-Allow-Origin': '*'}
        except StopIteration:
            return {'error': 'No Google Scholar profile found'}, 200, {'Access-Control-Allow-Origin': '*'}

api.add_resource(Author, '/author')

if __name__ == '__main__':
    app.run(port='5002')
