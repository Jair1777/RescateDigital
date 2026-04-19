import os, re
templates_dir = 'templates'
trans_re = re.compile(r'{%\s*trans\s+[\'"](.*?)[\'"]\s*%}')
blocktrans_re = re.compile(r'{%\s*blocktrans\s*%}(.*?){%\s*endblocktrans\s*%}', re.DOTALL)
blocktrans_with_re = re.compile(r'{%\s*blocktrans.*?%}(.*?){%\s*endblocktrans\s*%}', re.DOTALL)

strings = set()
for root, dirs, files in os.walk(templates_dir):
    for f in files:
        if f.endswith('.html'):
            with open(os.path.join(root, f), 'r', encoding='utf-8') as file:
                content = file.read()
                strings.update(trans_re.findall(content))
                strings.update(m.strip() for m in blocktrans_re.findall(content))
                strings.update(m.strip() for m in blocktrans_with_re.findall(content))

from build_translations import translations_en
missing = [s for s in strings if s not in translations_en]
for m in missing:
    print(repr(m))
