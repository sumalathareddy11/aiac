# simulated_scanner.py
"""
Simulated Network Scanner (SAFE)
--------------------------------
- This script DOES NOT perform any network activity.
- It generates realistic-looking scan results for given targets,
  suitable for reports, demos, or testing parsers.
- Use only for authorized classroom/demo output.
"""

import random
import time
import json
from datetime import datetime

COMMON_SERVICES = [
    (22, "ssh", "OpenSSH 8.9p1"),
    (80, "http", "Apache/2.4.54 (Ubuntu)"),
    (443, "https", "nginx/1.20.1 (TLS 1.2)"),
    (3306, "mysql", "MySQL 5.7"),
    (53, "dns", "BIND 9.16"),
    (139, "netbios-ssn", ""),
    (445, "microsoft-ds", ""),
    (8080, "http-proxy", "Apache Tomcat/9.0"),
]

def simulate_host_scan(host: str, seed: int = None):
    """Return a simulated scan result dict for a single host."""
    if seed is not None:
        rnd = random.Random(seed)
    else:
        rnd = random.Random(host + str(time.time()))

    # Decide if host is up
    up = rnd.random() > 0.05  # 95% chance host is up in simulation
    results = {
        "target": host,
        "timestamp": datetime.now().isoformat(),
        "up": up,
        "ports": []
    }
    if not up:
        return results

    # Choose a subset of services to mark as open/closed/filtered
    service_count = rnd.randint(2, 6)
    services = rnd.sample(COMMON_SERVICES, k=service_count)
    for port, proto_name, banner in services:
        # state probabilities: open (60%), closed (25%), filtered (15%)
        r = rnd.random()
        if r < 0.60:
            state = "open"
        elif r < 0.85:
            state = "closed"
        else:
            state = "filtered"

        # optionally include a banner with some probability when open
        banner_text = banner if (state == "open" and rnd.random() > 0.3) else ""
        # fake ttl/response time info
        rtt = round(rnd.uniform(0.3, 20.0), 2) if state == "open" else None

        results["ports"].append({
            "port": port,
            "protocol": "tcp",
            "service": proto_name,
            "state": state,
            "banner": banner_text,
            "rtt_ms": rtt
        })

    # Add a short summary
    open_ports = sum(1 for p in results["ports"] if p["state"] == "open")
    results["summary"] = {
        "open_ports": open_ports,
        "total_ports_checked": len(results["ports"])
    }
    return results


def run_simulation():
    print("=== Simulated Network Scanner (SAFE) ===")
    print("Enter targets separated by commas (example: 192.168.0.10, localhost, example.com)")
    targets_input = input("Targets: ").strip()
    if not targets_input:
        print("No targets provided. Exiting.")
        return
    targets = [t.strip() for t in targets_input.split(",") if t.strip()]

    all_results = []
    for t in targets:
        print(f"\nSimulating scan for: {t}")
        # Add a tiny delay for realism
        time.sleep(0.7)
        res = simulate_host_scan(t)
        all_results.append(res)
        # Pretty print summary line
        if not res["up"]:
            print(f"  {t} appears down (simulated).")
            continue
        print(f"  {t} - up - {res['summary']['open_ports']} open / {res['summary']['total_ports_checked']} checked")
        for p in sorted(res["ports"], key=lambda x: x["port"]):
            state = p["state"]
            svc = p["service"]
            banner = f" ({p['banner']})" if p.get("banner") else ""
            rtt = f" rtt={p['rtt_ms']}ms" if p.get("rtt_ms") else ""
            print(f"    TCP {p['port']:5d} {state:8s} {svc:12s}{banner}{rtt}")

    # Save results to JSON file for later parsing
    outfile = f"simulated_scan_{int(time.time())}.json"
    with open(outfile, "w", encoding="utf-8") as f:
        json.dump({"scan_time": datetime.now().isoformat(), "results": all_results}, f, indent=2)
    print(f"\nSimulated full results saved to: {outfile}")

if __name__ == "__main__":
    run_simulation()