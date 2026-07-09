from pydantic import BaseModel, HttpUrl
from typing import Optional


class Contact(BaseModel):
    social_media: str
    link: str

CONTACTS : list[Contact] = [
    Contact(
        social_media="GitHub",
        link="https://github.com/anirudh-s1308"
    ),
    Contact(
        social_media="LinkedIn",
        link="https://linkedin.com/in/anirudh-s1308"
    ),
    Contact(
        social_media="Twitter",
        link="https://x.com/Anirudh_1308"
    ),
    Contact(
        social_media="Email",
        link="anirudhsuniltiwari@gmail.com")
]