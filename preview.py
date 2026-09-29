"""Serve website/public locally the way the host does: /help finds
help.html, /i/ finds i/index.html, and a miss gets 404.html.

    python website/preview.py          -> http://localhost:8787
"""
import http.server
import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public")
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8787


class CleanUrlHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def send_head(self):
        path = self.translate_path(self.path)
        if not os.path.exists(path) and os.path.isfile(path + ".html"):
            self.path = self.path.split("?")[0].split("#")[0] + ".html"
        return super().send_head()

    def send_error(self, code, message=None, explain=None):
        not_found = os.path.join(ROOT, "404.html")
        if code != 404 or not os.path.isfile(not_found):
            return super().send_error(code, message, explain)
        with open(not_found, "rb") as page:
            body = page.read()
        self.send_response(404)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)


if __name__ == "__main__":
    print("Letter Bluff site preview: http://localhost:%d" % PORT)
    http.server.ThreadingHTTPServer(("127.0.0.1", PORT), CleanUrlHandler).serve_forever()
