import scholarly

search_query = scholarly.search_author('sophie limou')
author = next(search_query).fill()
print(author)
for pub in author.publications:
    print(pub)