from abc import abstractmethod, ABC
from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)


EMAIL_WITH_ATTACHMENTS_EVENT = 'email_with_attachments'
PLAIN_EMAIL_EVENT = 'plain_email'


# Publisher class
class EventManager:
    events_and_listeners = []

    def subscribe(self, event_type, listener):
        self.events_and_listeners.append({event_type: listener})

    def unsubscribe(self, event_type, listener):
        self.events_and_listeners.remove({event_type: listener})

    def notify(self, event_type, data):
        current_listeners = filter(
            lambda event_and_listener: event_and_listener.get(event_type) is not None, self.events_and_listeners
        )

        for event_and_listener in current_listeners:
            event_and_listener[event_type].update(data)


@dataclass
class Postman:
    events = EventManager()
    
    def send_emails_with_attachments(self, recipients):
        print('🤹‍♂️ Sending email with attachment(s)')

        self.events.notify(EMAIL_WITH_ATTACHMENTS_EVENT, recipients)

    def send_plain_email(self, recipients):
        print('🤹‍♂️ Sending plain email')

        self.events.notify(PLAIN_EMAIL_EVENT, recipients)


# Subscriber class
class EventListener(ABC):
    @abstractmethod
    def update(self):
        pass


class LogginListener(EventListener):
    def update(self, recipients):
        logger.info(f'Send emails to {recipients}')
        print('👂️ Logging successfully')


class ScanFileListener(EventListener):
    def update(self, recipients):
        print(f'👂️ Scanning the file attached to the email. Recipients: {recipients}')


if __name__ == '__main__':
    postman = Postman()

    logger_listener = LogginListener()
    postman.events.subscribe(EMAIL_WITH_ATTACHMENTS_EVENT, logger_listener)
    postman.events.subscribe(PLAIN_EMAIL_EVENT, logger_listener)

    terminal_listener = ScanFileListener()
    postman.events.subscribe(EMAIL_WITH_ATTACHMENTS_EVENT, terminal_listener)

    # Concrete actions
    postman.send_emails_with_attachments(['ko@carmail.com'])
    print('-' * 30)
    postman.send_plain_email(['ko@carmail.com', 'yiu@carmail.com'])