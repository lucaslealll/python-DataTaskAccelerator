"""
dta.messenger
~~~~~~~~~~~~~
"""
import email
import smtplib

DEFAULT_SMTP_PORT = "587"
DEFAUTL_SMTP_HOST = "smtp.gmail.com"


def send_email(
    receiver,
    sender_email,
    sender_auth,
    abstract="",
    content="",
    subject="",
    smtp_port="587",
    smtp_host="smtp.gmail.com",
):
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
    >>> send_email(client=CLIENT,project=PROJECT,script=SCRIPT,date=JOBDATE,abstract=str(repr(Exception)),error_log=str(format_exc()))
    """
    msg = email.message.Message()
    msg["Abstract"] = abstract
    msg["Subject"] = subject
    msg.add_header("Content-Type", "text/html")
    msg.set_payload(content)

    sender_email = smtplib.SMTP(f"{smtp_host}:{smtp_port}")
    sender_email.starttls()

    # Login Credentials for sending the mail
    sender_email.login(sender_email, sender_auth)
    sender_email.sendmail(
        sender_email,
        receiver,
        msg.as_string().encode("utf-8"),
    )
    return None


def send_alert_email(
    client,
    project,
    script,
    datetime,
    error_log,
    receiver,
    sender_email,
    sender_auth,
    content="",
    abstract="",
    subject="",
    smtp_port="587",
    smtp_host="smtp.gmail.com",
):
    """Send an alert email if the ETL script goes wrong.

    Parameters
    ----------
    `client` : Client name
    `project` : Project
    `abstract` : Type of error
    `datetime` : Date and hour that occurs
    `error_log` : Error log output

    Examples
    --------
    >>> send_alert_email(client=CLIENT,project=PROJECT,script=SCRIPT,date=JOBDATE,abstract=str(repr(Exception)),error_log=str(format_exc()))
    """
    subject = f"Error - {client}, {project}, {script}"
    content = f"""
        <b>Script `{script}` execution error for client {client}, project {project}</b>
        <p>{datetime}</p>
        <h4>Error log below:</h4>
        <code>[{script}] {abstract}</code>
        <br>
        <br>
        <code>{error_log}</code>
    """
    msg = email.message.Message()
    msg["Subject"] = subject
    msg.add_header("Content-Type", "text/html")
    msg.set_payload(content)

    sender_email = smtplib.SMTP(f"{smtp_host}:{smtp_port}")
    sender_email.starttls()

    # Login Credentials for sending the mail
    sender_email.login(sender_email, sender_auth)
    sender_email.sendmail(
        sender_email,
        receiver,
        msg.as_string().encode("utf-8"),
    )
    return None
