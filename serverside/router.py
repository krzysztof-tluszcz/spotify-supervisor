from sanic import response

class Router():
    
    def register_routes(self, server):
        server.add_route(self.test, '/')
        return

    async def test(self, request):
        return response.html("<h1>YEH</h1>")

    