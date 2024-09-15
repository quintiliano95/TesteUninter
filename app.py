import random
import requests
from flask import Flask, render_template, url_for

app = Flask(__name__)

NASA_API_URL = "https://images-assets.nasa.gov/recent.json"


def fetch_albums():
    response = requests.get(NASA_API_URL)
    data = response.json()
    return data['collection']['items'][:100]  # Limitar aos primeiros 100 álbuns


@app.route('/')
def home():
    albums = fetch_albums()
    selected_albums = random.sample(albums, 16)  # Seleciona 16 álbuns aleatórios

    # Cria uma lista formatada com os dados relevantes para a página inicial
    albums_data = []
    for album in selected_albums:
        title = album['data'][0]['title']
        date_created = album['data'][0]['date_created']
        preview_image = album['links'][0]['href'] if 'links' in album else None
        album_id = album['data'][0]['nasa_id']

        # Formata a data para o padrão brasileiro (dd/mm/aaaa)
        date_created = date_created.split("T")[0]  # Mantém apenas a parte da data
        date_created = "-".join(reversed(date_created.split("-")))  # Converte para dd-mm-yyyy

        albums_data.append({
            'title': title,
            'date_created': date_created,
            'preview_image': preview_image,
            'album_id': album_id
        })

    return render_template('home.html', albums=albums_data)


@app.route('/album/<album_id>')
def album_details(album_id):
    album_url = f"https://images-api.nasa.gov/asset/{album_id}"
    response = requests.get(album_url)
    album_files = response.json()['collection']['items']

    files_data = []
    for item in album_files:
        media_type = item['data'][0]['media_type']
        file_url = item['href']

        files_data.append({
            'media_type': media_type,
            'file_url': file_url
        })

    return render_template('album.html', files=files_data)


if __name__ == '__main__':
    app.run(debug=True)
