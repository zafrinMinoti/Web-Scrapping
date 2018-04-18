import requests
from bs4 import BeautifulSoup
import re

def get_movie_titles(req_obj_text, movie_rank):
    movies_list = []
    
    soup = BeautifulSoup(req_obj_text, "html.parser")
    lst = soup.select('b.big')
    for i in lst:
        title = i.get_text()
        if title[0].isdigit():
            movies_list.append(i.get_text())
            
    for movie in movies_list:
        rank = re.search('([0-9]+)\.\s(.+)', movie).group(1)
        title = re.search('([0-9]+)\.\s(.+)', movie).group(2)
        movie_rank[rank] = title
        
    return movie_rank


def main():
	top_movies = dict()
	root_url = "https://www.pastemagazine.com/articles/2017/12/the-50-best-movies-of-2017.html?p="
	for page in [1,2]:
	    r = requests.get(root_url+str(page))
	    top_movies = get_movie_titles(r.text, top_movies)

	return top_movies

if __name__ == "__main__":
	main()


