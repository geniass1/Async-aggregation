from aiohttp import web
from sender import send_request

URLS = []
app = web.Application()

app.add_routes([web.post('/', send_request)])
web.run_app(app, port=8080)


