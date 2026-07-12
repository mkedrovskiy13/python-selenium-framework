from abc import ABC

class BaseForm(ABC):

    def __init__(self):
        self.unique_element = None

    def is_opened(self):
        return self.unique_element.is_present() is not None
