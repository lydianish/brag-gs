import scholarly
import time

start_time = time.time()
search_query = scholarly.search_author('orlando gutiérrez')
author = next(search_query).fill()
print((time.time() - start_time), 'seconds')
#print(author)
#for pub in author.publications:
#    print(pub)