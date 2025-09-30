import os
import sys
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text
from rich import box
class nano:
    content = [""]
    current_line = 0
    filename = input()
    def load_file(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read().splitlines()

    def create_layout(content, current_line):
        layout = Layout()

        layout.split(
            Layout(name='header', size=3),
            Layout(name='main', size=3)
        )
        head_text = Text("Gnu nano 0.1v - {self.filename}", justify='center')
        layout['head'].update(
            Panel(head_text)
        )

        main_content = []
        for i, line in enumerate(content):
            if i == current_line:
                text = Text(f"> {line}")
                text.stylize(0,len(line)+2)
            else:
                text = f"{line}"
            main_content.append(text)
        layout['main'].update(
            Panel.fit(
                "\n".join(str(c) for c in main_content), 
                title='Main content'
            )
        )
