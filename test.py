import scholarly
import time

try:
    #start_time = time.time()
    search_query = scholarly.search_author('rosine manishimwe')
    author = next(search_query).fill()
    #print((time.time() - start_time), 'seconds')
    print(author)
    #for pub in author.publications:
    #    print(pub)
except StopIteration:
    print('Author profile not found.')