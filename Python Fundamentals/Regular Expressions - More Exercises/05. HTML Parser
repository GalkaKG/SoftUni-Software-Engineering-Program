import re

line = input()

pattern_title = r'<title>([A-Za-z0-9\s]+)</title>'
title = ''.join(re.findall(pattern_title, line))

body_content = re.findall(r'<body>.+</body>', line)
pattern_content = re.findall(r'>([^><]*)', ''.join(body_content))
content = ''
for match in pattern_content:
    content += match
content = content.replace('\\n', '')
print(f'Title: {title}')
print(f'Content: {content}')
