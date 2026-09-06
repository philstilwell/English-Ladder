"""Wait for Cloudflare's existing GitHub integration to publish committed lessons."""
import json
import subprocess
import sys
import time
from pathlib import Path


def fetch_json(url):
    result = subprocess.run(
        ['curl', '--fail', '--silent', '--show-error', '--max-time', '30',
         '--user-agent', 'English-family-deploy-check', url],
        capture_output=True, text=True, check=True,
    )
    return json.loads(result.stdout)


def main():
    origin = sys.argv[1].rstrip('/')
    expected = json.loads(Path('.cf-site/deployment.json').read_text())
    deadline = time.monotonic() + 12 * 60
    while time.monotonic() < deadline:
        try:
            live = fetch_json(f'{origin}/deployment.json?verify={int(time.time())}')
            if live.get('files') == expected['files']:
                print('Cloudflare publishes the complete committed asset manifest.')
                return
            print('Waiting for Cloudflare to publish the latest checked files...', flush=True)
        except (subprocess.CalledProcessError, ValueError):
            print('Cloudflare deployment is not ready yet.', flush=True)
        time.sleep(20)
    raise SystemExit('Cloudflare did not publish the committed files within 12 minutes. Check the Worker build log; GitHub source was saved.')


if __name__ == '__main__':
    main()
