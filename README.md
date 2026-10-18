# br-python-app

Demo Python app that installs Aikido-patched PyPI builds. Direct dependencies are pinned to `+aikido.N` versions from `https://pypi-staging.aikido.io/1f8edf5e23989a796bf/simple/`, with everything else resolved from PyPI.

```bash
uv sync
uv run python main.py
```

| Package | Installed |
| --- | --- |
| aiohttp | 3.14.1+aikido.3 |
| aiomysql | 0.2.0+aikido.3 |
| asteval | 1.0.5+aikido.2 |
| authlib | 1.7.0+aikido.2 |
| azure-core | 1.35.0+aikido.5 |
| black | 26.1.0+aikido.2 |
| brotli | 1.1.0+aikido.6 |
| cairosvg | 2.7.1+aikido.6 |
| certifi | 2023.11.17+aikido.2 |
| cryptography | 49.0.0+aikido.3 |
| django | 4.1.13+aikido.5 |
| djangorestframework | 3.14.0+aikido.1 |
| ecdsa | 0.19.1+aikido.5 |
| fastmcp | 2.13.0.2+aikido.3 |
| filelock | 3.20.2+aikido.2 |
| flask | 3.1.2+aikido.3 |
| flask-cors | 3.0.10+aikido.2 |
| gitpython | 3.1.58+aikido.3 |
| gunicorn | 21.2.0+aikido.2 |
| h11 | 0.14.0+aikido.2 |
| h2 | 4.2.0+aikido.2 |
| httplib2 | 0.31.2+aikido.2 |
| idna | 3.14+aikido.1 |
| jaraco.context | 5.3.0+aikido.7 |
| jinja2 | 3.1.5+aikido.2 |
| joserfc | 1.6.7+aikido.1 |
| jwcrypto | 1.4+aikido.2 |
| langchain-anthropic | 1.4.3+aikido.2 |
| langchain-core | 1.3.2+aikido.2 |
| langchain-text-splitters | 1.1.1+aikido.3 |
| langgraph-checkpoint | 4.1.0+aikido.2 |
| langsmith | 0.8.15+aikido.1 |
| lxml | 6.0.4+aikido.5 |
| markdown | 3.4.4+aikido.1 |
| marshmallow | 3.21.3+aikido.1 |
| mcp | 1.27.0+aikido.1 |
| multipart | 1.2.1+aikido.2 |
| nltk | 3.9.2+aikido.8 |
| numexpr | 2.8.4+aikido.4 |
| orjson | 3.11.5+aikido.4 |
| pdfminer.six | 20240706+aikido.2 |
| pillow | 12.2.0+aikido.7 |
| protobuf | 6.31.1+aikido.5 |
| pyasn1 | 0.6.3+aikido.3 |
| pydantic-ai-slim | 1.91.0+aikido.2 |
| pydantic-settings | 2.14.0+aikido.1 |
| pyjwt | 2.13.0+aikido.1 |
| pymongo | 4.6.0+aikido.4 |
| pymysql | 1.1.0+aikido.2 |
| pynacl | 1.5.0+aikido.7 |
| pypdf | 6.18.1+aikido.3 |
| pypdf2 | 3.0.1+aikido.2 |
| pytest | 9.0.2+aikido.3 |
| python-dotenv | 1.2.1+aikido.3 |
| python-engineio | 4.13.1+aikido.1 |
| python-multipart | 0.0.29+aikido.3 |
| python-socketio | 5.16.1+aikido.1 |
| requests | 2.32.5+aikido.3 |
| soupsieve | 2.8.3+aikido.1 |
| sqlparse | 0.5.5+aikido.1 |
| starlette | 1.3.0+aikido.1 |
| strawberry-graphql | 0.323.2+aikido.1 |
| telnyx | 4.88.1+aikido.2 |
| tornado | 6.5.1+aikido.5 |
| ujson | 5.12.1+aikido.3 |
| urllib3 | 2.7.0+aikido.1 |
| werkzeug | 3.1.3+aikido.4 |
| yt-dlp | 2025.10.22+aikido.2 |
| zipp | 3.17.0+aikido.2 |
