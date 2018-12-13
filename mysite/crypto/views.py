from django.shortcuts import render


def index(request):
    import requests
    import json
    #  putting the link of api we got from the website into a api_request variable
    #  Grab Crypto News:
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)

    #  Grab Crypto Price Data
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD")
    price = json.loads(price_request.content)

    return render(request, 'home.html', {'api': api, 'price': price})


def prices(request):
    if request.method == 'POST':
        import requests
        import json

        quote = request.POST['quote']
        quote = quote.upper()

        search_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
        search = json.loads(search_request.content)

        return render(request, 'prices.html', {'quote': quote, 'search': search})

    else:
        notfound = "Enter a crypto   symbol to search in the form above..."
        return render(request, 'prices.html', {'notfound': notfound})
