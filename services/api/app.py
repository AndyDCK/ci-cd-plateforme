from prometheus_client import start_http_server, Summary
import time

# Définition des métriques
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

@REQUEST_TIME.time()
def process_request():
    """Simuler le traitement d'une requête"""
    time.sleep(2)

if __name__ == "__main__":
    start_http_server(8000)  # Expose les métriques sur le port 8000
    while True:
        process_request()