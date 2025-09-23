from html import escape


def build_link(link: str, display: str):
    return f'<a href="{link}">{display}</a>'


def build_pre(text: str):
    return f'<pre>{escape(text)}</pre>'
