import requests
from bs4 import BeautifulSoup
import re

# Dictionary to map emotions to IMDb URLs
URLS = {
    "Drama": 'https://www.imdb.com/search/title/?title_type=feature&genres=drama',
    "Action": 'https://www.imdb.com/search/title/?title_type=feature&genres=action',
    "Comedy": 'https://www.imdb.com/search/title/?title_type=feature&genres=comedy',
    "Horror": 'https://www.imdb.com/search/title/?title_type=feature&genres=horror',
    "Crime": 'https://www.imdb.com/search/title/?title_type=feature&genres=crime',
    "Romance": 'https://www.imdb.com/search/title/?title_type=feature&genres=romance',
    "Thriller": 'https://www.imdb.com/search/title/?title_type=feature&genres=thriller',
    "Sci-Fi": 'https://www.imdb.com/search/title/?title_type=feature&genres=sci-fi',
    "Fantasy": 'https://www.imdb.com/search/title/?title_type=feature&genres=fantasy',
    "Adventure": 'https://www.imdb.com/search/title/?title_type=feature&genres=adventure',
    "Animation": 'https://www.imdb.com/search/title/?title_type=feature&genres=animation',
    "Biography": 'https://www.imdb.com/search/title/?title_type=feature&genres=biography',
    "Family": 'https://www.imdb.com/search/title/?title_type=feature&genres=family',
    "Mystery": 'https://www.imdb.com/search/title/?title_type=feature&genres=mystery',
    "History": 'https://www.imdb.com/search/title/?title_type=feature&genres=history',
    "War": 'https://www.imdb.com/search/title/?title_type=feature&genres=war',
    "Western": 'https://www.imdb.com/search/title/?title_type=feature&genres=western',
}

def main(emotion):
    url = URLS.get(emotion)
    print("ok", url)
    if not url:
        print("Invalid emotion.")
        return []

    headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for HTTP errors
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

    soup = BeautifulSoup(response.text, "lxml")

    # Extract movie titles
    titles = [a.get_text() for a in soup.find_all('a', href=re.compile(r'/title/tt\d+/'))]
    return titles

# Driver Function
if __name__ == '__main__':
    emotion = input("Enter the emotion: ").strip()
    movie_titles = main(emotion)

    if not movie_titles:
        print("No titles found.")
    else:
        max_titles = 14 if emotion in ["Drama", "Action", "Comedy", "Horror", "Crime", "Romance", "Thriller", "Sci-Fi", "Fantasy", "Adventure", "Animation", "Biography", "Family", "Mystery", "History", "War", "Western"] else 12
        for title in movie_titles[:max_titles]:
            print(title)
