import asyncio
from importlib.metadata import version

import aiohttp
import authlib
import django
import flask_cors
import git
import gunicorn
import h11
import jinja2
import joserfc
import jwt
import multipart
import nltk
import pyasn1
import pypdf
import requests
import sqlparse
import starlette
import tornado
import ujson
import urllib3
import werkzeug
from PIL import Image
from cryptography.hazmat.primitives import hashes
from google.protobuf.internal import api_implementation
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route


def build_status() -> dict:
    digest = hashes.Hash(hashes.SHA256())
    digest.update(b"demo")
    template = jinja2.Environment().from_string("Hello {{ name }}")
    image = Image.new("RGB", (1, 1))

    return {
        "message": template.render(name="demo"),
        "aiohttp": aiohttp.__version__,
        "authlib": authlib.__version__,
        "cryptography": digest.finalize().hex()[:12],
        "django": django.get_version(),
        "flask_cors": flask_cors.__version__,
        "git": git.__version__,
        "gunicorn": gunicorn.__version__,
        "h11": str(h11.Connection(h11.CLIENT).our_state),
        "joserfc": joserfc.__version__,
        "jwt": jwt.__version__,
        "multipart": multipart.__version__,
        "nltk": nltk.__version__,
        "pillow": f"{image.mode} {version('pillow')}",
        "protobuf": api_implementation.Type(),
        "pyasn1": pyasn1.__version__,
        "pypdf": pypdf.__version__,
        "requests": requests.__version__,
        "sqlparse": sqlparse.__version__,
        "starlette": starlette.__version__,
        "tornado": tornado.version,
        "ujson": ujson.dumps({"ok": True}),
        "urllib3": urllib3.__version__,
        "werkzeug": f"{werkzeug.__name__} {version('werkzeug')}",
    }


async def homepage(_request: Request) -> JSONResponse:
    return JSONResponse(build_status())


app = Starlette(routes=[Route("/", homepage)])


async def _check() -> None:
    scope = {
        "type": "http",
        "http_version": "1.1",
        "method": "GET",
        "scheme": "http",
        "path": "/",
        "raw_path": b"/",
        "query_string": b"",
        "headers": [],
        "client": ("127.0.0.1", 0),
        "server": ("127.0.0.1", 80),
    }
    response = await homepage(Request(scope))
    print(response.status_code)
    print(response.body.decode())


def main() -> None:
    print("br-python-app demo loaded")
    asyncio.run(_check())


if __name__ == "__main__":
    main()
