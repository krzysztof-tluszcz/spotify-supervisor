from sanic import response

with open('serverside/website/index.html', 'r') as f:
    html_string = f.read()

class Router():
    
    def register_routes(self, server):
        server.add_route(self.test, '/')
        return

    async def test(self, request):
        return response.html(html_string)

    