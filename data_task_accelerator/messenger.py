"""
dta.messenger
~~~~~~~~~~~~~
"""
import email
import smtplib

DEFAULT_SMTP_PORT = "587"
DEFAUTL_SMTP_HOST = "smtp.gmail.com"


def send_email(
    from_addr: str,
    from_psswd: str,
    to_addr: str | list,
    msg_body: str = "",
    msg_subject: str = "",
    smtp_host: str = DEFAUTL_SMTP_HOST,
    smtp_port: str = DEFAULT_SMTP_PORT,
) -> None:
    """Send an email if the .

    Parameters
    ----------
    `abstract` : abstract
    `content` : message content
    `receiver` : email or list of emails that will receive the message
    `sender_auth` : sender authentication token
    `sender` : sender
    `subject` : subject

    By default:
        - `smtp_port` : "587"
        - `smtp_host` : "smtp.gmail.com"

    Examples
    --------
    >>> send_email(
    from_addr="jack_saur@gmail.com",
    from_psswd="dshrnliru83no10d",
    to_addr="daniels_raptor@gmail.com",
    msg_subject="Lorem",
    msg_body="Lorem ipsum dolor sit amet...",
    )
    """
    msg = email.message.Message()
    # msg["Abstract"] = abstract
    msg["Subject"] = msg_subject
    msg.add_header("Content-Type", "text/html")
    msg.set_payload(msg_body)

    messenger = smtplib.SMTP(f"{smtp_host}:{smtp_port}")
    messenger.starttls()

    # Login Credentials for sending the mail
    messenger.login(from_addr, from_psswd)
    messenger.sendmail(
        from_addr,
        to_addr,
        msg.as_string().encode("utf-8"),
    )
    return None
