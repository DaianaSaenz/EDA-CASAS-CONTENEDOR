import requests

def obtenerPrecioM2PorDistritoMadrid(zona):
    url = f"https://www.fotocasa.es/indice-precio-vivienda/madrid-capital/{zona}"
    headers = {
        "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        "accept-encoding": 'gzip, deflate, br',
        "accept-language": 'es-ES,es;q=0.9',
        "cache-control": 'max-age=0',
        "dnt":"1",
        "sec-ch-ua": '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    }
    return requests.get(url, headers=headers)

def obtenerInfoPrecioSueloPorDistritoMadrid(zona):
    url = f"https://www.fotocasa.es/es/comprar/terrenos/madrid-capital/{zona}/l"
    headers = {
        "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        "accept-encoding": 'gzip, deflate, br',
        "accept-language": 'es-ES,es;q=0.9',
        "cache-control": 'max-age=0',
        "dnt":"1",
        "sec-ch-ua": '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    }
    return requests.get(url, headers=headers)

def getHttp(url):
    return requests.get(url)