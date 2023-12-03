from requests import get
from bs4 import BeautifulSoup
from extractor.wwr import extract_wwr_jobs

jobs = extract_wwr_jobs("python")
print(jobs)