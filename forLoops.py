from requests import get
'''
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
    results[website] = "working"
  else:
    results[website] = "not working"

print(results)
'''

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "python" #input("input a job to seartch:")

response = get(f"{base_url}{search_term}")

if response.status_code != 200:
  print("can't response website")
else:
  print(response.text)