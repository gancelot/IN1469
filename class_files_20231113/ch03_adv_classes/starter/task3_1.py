import colorama
import jinja2
import jinja2.exceptions
import requests

# import mocklab  # uncomment this line only if access to themoviedb.org is not available, otherwise leave commented out

from movie.movie import Movie

key = '23cf8b21d9a3bfd615076491d6bae442'
search_url = 'http://api.themoviedb.org/3/search/movie?api_key={key}&query={title}'
details_url = 'https://api.themoviedb.org/3/movie/{id}?api_key={key}'


def render_movie(movie):
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('./tmpl'))
    try:
        tmpl = env.get_template('movie.jinja')
        results = tmpl.render(movie=movie)

    except (jinja2.exceptions.TemplateNotFound, jinja2.exceptions.TemplateError) as err:
        results = f'Error rendering movie: {err}'

    return results


search = input('Enter a movie phrase: ')
results = requests.get(search_url.format(key=key, title=search)).json()
movie_list = results.get('results', [])
for idx, movie in enumerate(movie_list):
    print(colorama.Fore.RED, f"{idx + 1} - {movie.get('title', '(no title)')}")

detailed_item = input('Enter a movie number: ')
movie_id = movie_list[int(detailed_item) - 1].get('id')
detailed_results = requests.get(details_url.format(key=key, id=movie_id)).json()

movie = Movie(**detailed_results)
print(colorama.Fore.GREEN, render_movie(movie))
