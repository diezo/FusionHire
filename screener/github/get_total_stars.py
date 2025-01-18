import requests
from requests import Response
from bs4 import BeautifulSoup, ResultSet, Tag
import re

USER_AGENT: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"


def get_total_stars(username: str) -> int:
    """
    Get the total stars of a GitHub user.
    """

    # Preprocess Username
    username: str = username.strip().lower()

    # Invalid Username?
    if username == "": return 0

    page: int = 1
    count: int = 0

    while True:
        response: Response = requests.get(
            url=f"https://github.com/{username}?tab=repositories&page={page}",
            headers={
                "user-agent": USER_AGENT,
                "accept": "text/html, application/xhtml+xml",
                "accept-language": "en-US,en;q=0.9",
                "priority": "u=1, i",
                "sec-ch-ua": "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\", \"Brave\";v=\"132\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "sec-gpc": "1",
                "turbo-frame": "user-profile-frame",
                "cookie": "",
                "Referer": f"https://github.com/{username}?tab=overview",
                "Referrer-Policy": "strict-origin-when-cross-origin"
            }
        )

        # Did Request Failed?
        if not response.ok:
            return 0

        # No More Pages?
        if response.text.find("blankslate-container") != -1:
            break

        # Load Beautiful Soup
        soup: BeautifulSoup = BeautifulSoup(response.text, "html.parser")

        # Filter Star Containers
        star_containers: ResultSet[Tag] = soup.find_all("a", href=re.compile(r"^\/.+\/.+\/stargazers$"))

        # Increment Count By Stars
        for container in star_containers:
            try: count += int(container.get_text().strip().replace(",", ""))
            except ValueError: ...

        page += 1  # Next Page

    return count
