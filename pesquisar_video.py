from youtube_search import YoutubeSearch

# Função para buscar vídeos do YouTube com base em um termo de pesquisa
def search_videos(search_query, max_results=10):
    results = YoutubeSearch(search_query, max_results=max_results).to_dict()
    video_links = ["https://www.youtube.com" + result['url_suffix'] for result in results]
    return video_links

# Termo de pesquisa
search_query = 'futebol'  # Substitua pelo termo desejado

# Busca vídeos com base no termo de pesquisa
videos = search_videos(search_query)

# Imprime os links dos vídeos encontrados
for video in videos:
    print(video)
