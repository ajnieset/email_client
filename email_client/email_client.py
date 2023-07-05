from abc import ABC, abstractmethod

class EmailClient(ABC):
    @abstractmethod
    def send(to_email: str):
        pass