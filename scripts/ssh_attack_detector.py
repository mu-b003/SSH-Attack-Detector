import re

log_file = "auth.log"

failed = 0
success = 0
ips = {}

with open(log_file, "r", errors="ignore") as file:
    for line in file:

        if "Failed password" in line:
            failed += 1

            match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)

            if match:
                ip = match.group(1)

                if ip not in ips:
                    ips[ip] = 0

                ips[ip] += 1

        elif "Accepted password" in line:
            success += 1

print("=" * 40)
print("SSH Attack Detection Report")
print("=" * 40)

print(f"Failed Logins : {failed}")
print(f"Successful Logins : {success}")

print("\nSource IPs:")

for ip, count in ips.items():
    print(f"{ip} -> {count} attempts")
