import requests

url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos"
api_key = "wmDoTAJLPVThCo8asBkARRtcb9ECEv15sUjPTmPN"

def build_web_page(srcs):
    file = open('mars_photos.html', 'w')

    template_top = '''
    <html>
        <head>
        </head>
        <body>
            <ul>

    '''
    template_bottom = '''
     </uL>
        </body>
    </html>
    '''
    for src in srcs:
        template_top += (f'<li><img src={src}></li>')
    file.write(template_top + template_bottom)

params = {"api_key": api_key}
payload = {}
headers = {}
response = requests.request(
    "GET", url, headers=headers, params=params, data=payload)
latest_photos = list(dict(response.json())['latest_photos'])
img_srcs = []

if(len(latest_photos) > 25):
    latest_photos = latest_photos[0:25]

for photo in latest_photos:
    img_srcs.append(photo['img_src'])

build_web_page(img_srcs)
