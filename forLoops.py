import requests 

websites = [
    "google.com",
    "https://facebook.com",
    "apple.com",
    "https://tiktok.com",
    "microsoft.com"
  ]

for website in websites:
  if not website.startswith("https://"):
    website = f"https://{website}"
  print(website)