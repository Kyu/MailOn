import email
import imaplib


def get_mail(imap_settings: dict, username: str, password: str, limit=10) -> dict:
    # Port and address config
    addr = imap_settings['host']
    port = imap_settings['port']

    # Get an imap mailbox through ssl and login
    mailbox = imaplib.IMAP4_SSL(addr, port)
    mailbox.login(username, password)
    mailbox.select(readonly=True)  # Not tested with this param but should work

    # This gets all messages from inbox and returns a list of b'int' representing the number of each Message in inbox
    # Do this without retrieving all messages every time?
    message_numbers = mailbox.search(None, 'ALL')
    messages = message_numbers[1][0].split()

    # Limit messages to last `limit` in list
    start = len(messages) - limit
    messages = messages[start:]

    mail = dict()
    for num in messages:
        # Get each message by ID from mailbox. Idk what RFC822 does, stackoverflow had it and it works
        data = mailbox.fetch(num, '(RFC822)')

        # Add number: Message representation of each retrieved Message to `mail` dict
        mail[num.decode('utf-8')] = email.message_from_bytes(data[1][0][1])

    return mail
