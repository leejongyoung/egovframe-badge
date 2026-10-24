import re
from pathlib import Path

LATEST = '5.0.7'
LABELS = {
    'en': 'eGovFrame',
    'ko': '전자정부표준프레임워크',
    'es': 'Marco Estándar de Gobierno Electrónico',
    'vi': 'Khung chuẩn Chính phủ điện tử',
    'ar': 'الإطار القياسي للحكومة الإلكترونية',
    'fr': "Cadre standard de l'administration électronique",
}
SUFFIX = {'en': '', 'ko': '-ko', 'es': '-es', 'vi': '-vi', 'ar': '-ar', 'fr': '-fr'}

for lang in ('en', 'ko', 'es', 'vi', 'ar', 'fr'):
    path = Path(f'/Users/leejongyoung/Developer/egovframe-badge/docs/README.{lang}.md')
    text = path.read_text(encoding='utf-8')
    suffix = SUFFIX[lang]
    text = re.sub(
        r'(\[!\[[^\]]*\]\(\.\./badges/[^/]+/flat' + re.escape(lang == 'en' and '' or f'-{lang}') + r'\.svg\)\]\()https://www\.egovframe\.go\.kr/\)',
        r'\1https://www.egovframe.go.kr/',
        text
    )
    path.write_text(text, encoding='utf-8')
    print(f'{lang}: fixed')
print('done')