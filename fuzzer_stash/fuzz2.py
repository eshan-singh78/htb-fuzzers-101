import requests


TARGET_IP = "http://10.10.11.68"
BASE_DOMAIN = "planning.htb"


WORDLIST = [
    "admin",
    "grafana",
    "dev",
    "test",
    "staging",
    "backup",
    "beta"
]

def fuzz_vhosts():
    for sub in WORDLIST:
        vhost = f"{sub}.{BASE_DOMAIN}"
        headers = {"Host": vhost}
        
        try:
            r = requests.get(TARGET_IP, headers=headers, timeout=3, allow_redirects=False)
            if r.status_code != 404:
                print(f"[+] {vhost} {r.status_code}")
        except requests.exceptions.RequestException:
            pass  # Ignore connection errors silently

if __name__ == "__main__":
    fuzz_vhosts()
