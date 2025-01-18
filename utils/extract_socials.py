import pymupdf
import re


def github_username(resume: str) -> str:
    """
    Extracts GitHub username from Resume.
    """

    links: list[str] = []

    with pymupdf.open(resume) as pdf:

        for i in range(pdf.page_count):
            [links.append(link["uri"]) for link in pdf.load_page(i).get_links() if "uri" in link]

    for link in links:
        match: re.Match = re.match(r"https://github.com/(?P<username>[\w-]+)/?", link)

        if match:
            try: return match.group("username")
            except IndexError: return ""
    
    return ""
