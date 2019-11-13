import twitter
from parameters import parameters


def get_tweets(api, screen_name, count_to_retrieve=50):
    """
    Obtiene los tweets de un usuario especifico
    :param api: El objeto API de Twitter-Python con las keys ya seteadas
    :param screen_name: Nombre del usuario del tipo @<nombre> a buscar
    :param count_to_retrieve: Cantidad de tweets a obtener (maximo 200)
    :return: None
    """
    count_to_retrieve = min(count_to_retrieve, 200)  # No puede ser mayor a 200
    print("Obteniendo Tweets de {}".format(screen_name))
    timeline = api.GetUserTimeline(screen_name=screen_name, count=count_to_retrieve)

    # Los muestro en consola
    for tweet in timeline:
        print(tweet)


def get_hashtag(api, hashtag, count_to_retrieve=50, since=None, until=None):
    """
    Obtiene los tweets que corresponden al termino de busqueda por hashtag
    :param api: El objeto API de Twitter-Python con las keys ya seteadas
    :param hashtag: Hashtag a buscar
    :param count_to_retrieve: (Opcional) Cantidad de tweets a obtener (maximo 100)
    :param since: (Opcional) Fecha desde la que se quiere filtar (en formato YYYY-MM-DD)
    :param unti: (Opcional) Fecha hasta la que se quiere filtar (en formato YYYY-MM-DD)
    :return: None
    """
    if not len(hashtag) or hashtag[0] != "#":
        print("No es un hashtag valido")
        return

    count_to_retrieve = min(count_to_retrieve, 100)  # No puede ser mayor a 100
    print("Obteniendo Tweets con hashtag {}".format(hashtag))
    timeline = api.GetSearch(term=hashtag, count=count_to_retrieve, since=since, until=until)

    # Los muestro en consola
    for tweet in timeline:
        print(tweet)


def main():
    api = twitter.Api(consumer_key=parameters["consumer_key"],
                      consumer_secret=parameters["consumer_secret"],
                      access_token_key=parameters["access_token_key"],
                      access_token_secret=parameters["access_token_secret"])

    # Ejemplo de extraccion de tweets de un usuario
    user = parameters["USER"]
    if user:
        get_tweets(api=api, screen_name=user)

    # Ejemplo de extraccion de tweets de un hashtag
    hashtag = parameters["hashtag"]
    if hashtag:
        get_hashtag(api=api, hashtag=hashtag)


if __name__ == '__main__':
    main()