import re
from pathlib import Path

for lang in ('en', 'ko', 'es', 'vi', 'ar', 'fr'):
    path = Path(f'/Users/leejongyoung/Developer/egovframe-badge/docs/README.{lang}.md')
    text = path.read_text(encoding='utf-8')
    text = re.sub(r'(https://www\.egovframe\.go\.kr/?)"', r'https://www.egovframe.go.kr/"', text)
    path.write_text(text, encoding='utf-8')
    print(f'{lang}: fixed')
print('done')