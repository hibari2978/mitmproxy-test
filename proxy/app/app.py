import json

from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    # authへのアクセスであれば、リクエストを送らず {name: admin}を返す
    if flow.request.pretty_url == "http://localhost:3500/auth":
        flow.response = http.Response.make(
            200,  # (optional) status code
            json.dumps({"name": "admin"}),  # (optional) content
            {"Content-Type": "text/json"},  # (optional) headers
        )
    
    # それ以外はhttp://backend:8000 へパス
    flow.request.host = "backend"
    flow.request.port = 8000
