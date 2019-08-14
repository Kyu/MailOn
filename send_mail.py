from email.message import Message
from repoze.sendmail.delivery import DirectMailDelivery
from repoze.sendmail.mailer import SMTPMailer
import transaction


# Function to send a Message object
def send_mail(message: Message, _from: str, to: list, smtp_settings: dict, username: str, password: str,
              tls: bool = False, ssl: bool = False, debug: bool = False) -> None:

    host = smtp_settings['host']
    port = smtp_settings['port']

    # Begin transaction. Idk fully how this lib works but it's needed
    transaction.manager.begin()

    try:
        # Create a new SMTP mailer using vars declared above.
        # TODO Debug should be True or False depending on if debug mode is on
        # Idea TO DO to Github Issue plugin

        mailer = SMTPMailer(hostname=host, port=port, username=username, password=password, ssl=ssl,
                            no_tls=not tls, debug_smtp=debug)

        # Need an object to deliver mail (for some reason)
        # TODO QueuedMailLDelvery support
        delivery = DirectMailDelivery(mailer)

        delivery.send(_from, to, message)

        # Commit transaction, this actually makes sure the thing is done
        transaction.manager.commit()
    # TODO Make Exception handling more specific
    except Exception as e:
        transaction.manager.abort()
        raise e
