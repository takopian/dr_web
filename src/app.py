from aiohttp import web
from api import router


def create_app():
    app = web.Application()
    app.add_routes(router)
    print("app created")
    return app


if __name__ == '__main__':
    web.run_app(create_app(), host='127.0.0.1', port=3000)
    print("RUNNING")
