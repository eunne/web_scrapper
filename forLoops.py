from requests import get

websites = (
    "google.com",
    "https://facebook.com",
    "apple.com",
    "https://tiktok.com",
    "microsoft.com"
  )

results = {}

for website in websites:
  if not website.startswith("https://"):
    website = f"https://{website}"
  response = get(website)
  if response.status_code == 200:
    results[website] = "working"ㅔㅑ
  else:
    results[website] = "not working"

print(results)