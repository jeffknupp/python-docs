import sys
import os
import glob

import markdown
from jinja2 import Environment, FileSystemLoader

def main():
    environment = Environment(loader=FileSystemLoader('templates'))
    m = markdown.Markdown(extensions=['fenced_code'])
    markdown_text = ''
    for directory in ['dictionary']:
        with open(os.path.join(directory, 'index.md'), 'r') as infile:
            markdown_text += infile.read()

    for path in glob.glob('dictionary/**.md'):
        if 'index' in path:
            continue
        if not os.path.isdir(path):
            with open(path, 'r') as infile:
                markdown_text += '\n-----------------\n'
                markdown_text += infile.read()

        with open(os.path.join(directory, 'index.html'), 'w') as output_file:
            content = m.convert(markdown_text)
            template = environment.get_template("list.html")
            output_file.write(template.render(content=content))

if __name__ == '__main__':
    main()
