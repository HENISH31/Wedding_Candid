import os

file_path = 'public/global.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace wrong escapes
content = content.replace('\\`', '`')
content = content.replace('\\${', '${')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
