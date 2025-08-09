import socket
import json
from concurrent.futures import ThreadPoolExecutor

TARGET = "10.10.11.74"
PORTS = range(1, 1025)


with open("services.json", "r") as f:
    SERVICE_MAP = json.load(f)

results = []

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.5)
        result = s.connect_ex((TARGET, port))
        if result == 0:
            banner = "No banner retrieved"
            try:
                if SERVICE_MAP.get(str(port), "").lower() == "http":
                    request = f"HEAD / HTTP/1.1\r\nHost: {TARGET}\r\n\r\n"
                    s.sendall(request.encode())
                else:
                    s.sendall(b"\r\n")
                banner = s.recv(2048).decode(errors="ignore").strip()
            except:
                pass

            service_name = SERVICE_MAP.get(str(port), "Unknown")
            results.append((port, service_name, banner))
        s.close()
    except:
        pass

def main():
    print(f"Starting port scan on {TARGET}...\n")
    with ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(scan_port, PORTS)

    print("\nScan Results:")
    print("-" * 50)
    for port, service, banner in sorted(results):
        print(f"Port: {port:<5} | Service: {service:<10} | Banner: {banner}")

if __name__ == "__main__":
    main()
