from __future__ import annotations
from abc import ABC, abstractmethod


class Document:
    def __init__(self) -> None:
        self.state = DraftState(self)

    def render(self):
        self.state.render()

    def publish(self):
        self.state.publish()

    def change_state(self, state: State):
        self.state = state
    
    def owner_is_admin(self):
        return True
    
    def owner_is_author(self):
        return False


class State(ABC):

    def __init__(self, document: Document) -> None:
        self.document = document

        super().__init__()

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def publish(self):
        pass


class DraftState(State):
    def render(self):
        if self.document.owner_is_admin() or self.document.owner_is_author():
            print('Showing document content [Draft state]')
        else:
            print("Is not possible to show the document's content")

    def publish(self):
        self.document.change_state(ModerationState(self.document))
        print('Document successfully move to moderation state')


class ModerationState(State):
    def render(self):
        if self.document.owner_is_admin() or self.document.owner_is_author():
            print('Showing document content [Moderation state]')
        else:
            print("Is not possible to show the document's content")

    def publish(self):
        self.document.change_state(PublishedState(self.document))
        print('Document successfully move to published state')



class PublishedState(State):
    def render(self):
        print('Showing document content to the world')

    def publish(self):
        print('The document was already published')


if __name__ == '__main__':
    document = Document()

    document.render()
    document.publish()

    document.render()
    document.publish()

    document.render()
    document.publish()
