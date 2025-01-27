import re

url = input("Twitter URL: ").strip()

# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)

# matches = re.search(r"^(https?://)?(www\.)?twitter\.com/(.+)$", url)

# if matches:
#     print(f"Username: {matches.group(3)}")

if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username: {matches.group(1)}") 