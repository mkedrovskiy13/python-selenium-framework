from dataclasses import dataclass

@dataclass
class Config:
    browser: str
    timeout: int
    base_url: str
    page_load_strategy: str
    incognito: bool
    maximized: bool
