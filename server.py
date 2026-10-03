"""Pornește site-ul NORD pe calculatorul tău, folosind doar Python standard."""

from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import os
import webbrowser


HOST = "127.0.0.1"
PORT = 8000
SITE_DIR = Path(__file__).resolve().parent


class SiteHandler(SimpleHTTPRequestHandler):
    """Servește fișierele site-ului din directorul acestui script."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(SITE_DIR), **kwargs)

    def end_headers(self):
        # Evită păstrarea în cache în timpul editării fișierelor locale.
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


if __name__ == "__main__":
    os.chdir(SITE_DIR)
    url = f"http://{HOST}:{PORT}/"
    server = ThreadingHTTPServer((HOST, PORT), SiteHandler)
    print(f"Site-ul NORD este disponibil la {url}")
    print("Oprește serverul cu Ctrl+C.")
    try:
        webbrowser.open(url)
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServerul NORD a fost oprit.")
    finally:
        server.server_close()