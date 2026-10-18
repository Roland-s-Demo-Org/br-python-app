# br-python-app

Demo Python app for Aikido libraries. Every direct dependency is pinned to an upstream version that has an Aikido patched build in `as_root_io_cve_info` (`distro = pypi`). The lockfile installs those upstream versions, so a scan can show the Aikido fix as available.

Counts are distinct advisories on the latest `+aikido.N` build of that exact version.

| Package | Installed | Aikido fix | Critical | High | Medium | Low |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| aiohttp | 3.12.15 | 3.12.15+aikido.8 | 0 | 2 | 14 | 13 |
| GitPython | 3.1.46 | 3.1.46+aikido.10 | 0 | 19 | 2 | 0 |
| pillow | 12.1.0 | 12.1.0+aikido.13 | 0 | 13 | 5 | 0 |
| pypdf | 6.10.1 | 6.10.1+aikido.10 | 0 | 2 | 14 | 0 |
| tornado | 6.2 | 6.2+aikido.9 | 0 | 6 | 6 | 0 |
| Authlib | 1.6.6 | 1.6.6+aikido.8 | 1 | 3 | 4 | 0 |
| urllib3 | 2.4.0 | 2.4.0+aikido.7 | 0 | 4 | 2 | 0 |
| cryptography | 46.0.3 | 46.0.3+aikido.8 | 0 | 4 | 1 | 1 |
| django | 4.1.13 | 4.1.13+aikido.4 | 1 | 2 | 2 | 0 |
| pyasn1 | 0.6.1 | 0.6.1+aikido.6 | 0 | 5 | 0 | 0 |
| starlette | 1.0.0 | 1.0.0+aikido.3 | 0 | 2 | 2 | 1 |
| flask-cors | 3.0.10 | 3.0.10+aikido.2 | 0 | 1 | 4 | 0 |
| PyJWT | 2.12.1 | 2.12.1+aikido.4 | 0 | 1 | 4 | 0 |
| Jinja2 | 3.1.2 | 3.1.2+aikido.8 | 0 | 0 | 5 | 0 |
| nltk | 3.9.2 | 3.9.2+aikido.8 | 1 | 2 | 1 | 0 |
| python-multipart | 0.0.26 | 0.0.26+aikido.5 | 0 | 2 | 0 | 2 |
| joserfc | 1.6.2 | 1.6.2+aikido.4 | 0 | 2 | 1 | 0 |
| sqlparse | 0.5.3 | 0.5.3+aikido.2 | 0 | 2 | 1 | 0 |
| Werkzeug | 3.1.3 | 3.1.3+aikido.4 | 0 | 0 | 3 | 0 |
| requests | 2.31.0 | 2.31.0+aikido.4 | 0 | 0 | 3 | 0 |
| gunicorn | 21.2.0 | 21.2.0+aikido.2 | 0 | 2 | 0 | 0 |
| protobuf | 4.25.5 | 4.25.5+aikido.11 | 0 | 2 | 0 | 0 |
| ujson | 5.10.0 | 5.10.0+aikido.6 | 0 | 2 | 0 | 0 |
| h11 | 0.14.0 | 0.14.0+aikido.2 | 1 | 0 | 0 | 0 |

```bash
uv sync
uv run python main.py
```
