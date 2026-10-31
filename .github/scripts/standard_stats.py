"""Refresh stats.json from SILEX's public Standard host page.

Reads the two numbers shown at the top of https://standard.iowire.com/host/silex
(Host Score and Reviews Completed) and rewrites stats.json only when they change.
Run by .github/workflows/standard-stats.yml; safe to run by hand too.
"""
import datetime
import json
import re
import sys
import urllib.request

URL = 'https://standard.iowire.com/host/silex'
OUT = 'stats.json'


def grab(html, label):
    m = re.search(
        r'hp2-meta__label">\s*' + re.escape(label) + r'\s*</span>\s*'
        r'<span class="hp2-meta__value">\s*([\d][\d.,]*)', html)
    return m.group(1).replace(',', '') if m else None


def main():
    req = urllib.request.Request(URL, headers={
        'User-Agent': 'silexsounds-stats/1.0 (+https://silexsounds.com)'})
    html = urllib.request.urlopen(req, timeout=30).read().decode('utf-8', 'replace')

    reviews = grab(html, 'Reviews Completed')
    score = grab(html, 'Host Score')
    if not reviews or not reviews.isdigit():
        sys.exit('Reviews Completed not found on the Standard page; stats.json left as is.')

    try:
        old = json.load(open(OUT))
    except (OSError, ValueError):
        old = {}

    new = {
        'reviews': int(reviews),
        'score': score or old.get('score', '9.9'),
    }
    if new['reviews'] == old.get('reviews') and new['score'] == old.get('score'):
        print('No change:', new)
        return
    new['updated'] = datetime.date.today().isoformat()
    with open(OUT, 'w') as f:
        json.dump(new, f, indent=2)
        f.write('\n')
    print('Updated:', new)


if __name__ == '__main__':
    main()
