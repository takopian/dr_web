from aiohttp import web

router = web.RouteTableDef()


@router.view('/')
class BaseView(web.View):
    async def get(self):
        print("GET /")
        return web.Response(text="success")
