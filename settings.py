# SMTP Settings builder/getter functions
# Every func should return a dict with attrs 'host' and 'port'


def outlook_defaults(live=False) -> dict:
    host = "smtp-mail.outlook.com" if not live else "smtp.live.com"
    return dict(host=host, port=587)


def gmail_defaults(tls=False) -> dict:
    host = "smpt.google.com"
    port = 587 if not tls else 2
    return dict(host=host, port=587)


def custom_settings(host, port, ssl=False, tls=False) -> dict:
    return dict(host=host, port=port, ssl=ssl, tls=tls)

# etc Yahoo, iCloud, Opera, Aol, Cox, Zoho, Proton, Mail.com
