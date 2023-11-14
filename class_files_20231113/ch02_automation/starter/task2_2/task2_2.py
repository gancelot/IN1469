"""
    Task 2-2 (Starter): Generate a PDF of the name, city, and state of the schools
    listed in the resources/baseball/Schools.csv file.
    Send this PDF as an email attachment to our "dev" SMTP server.

    Step 1. From a command window, start the SMTP server

            python -m smtpd -c DebuggingServer -n localhost:1025

            NOTE: if the smtpd server gives a deprecation warning, just ignore this!

    Step 2. Examine the get_data() function below.  It is already completed and
            should successfully return the data from the file.  At the bottom of this
            file, the function is called.  You can optionally print out the data
            if you wish to verify its structure.

    Step 3. Complete the generate_pdf() function.  You can alter and/or experiment with
            the TableStyle parameters as you see fit.  To finish this function, at
            the bottom of it:
            a) Add the TableStyle object to the Table (hint: call setStyle()).
            b) Append the Table object to the PDF doc_items to be rendered.
            c) Call the SimpleDocTemplate's build() method passing the doc_items to it.

    Step 4. Call the generate_pdf() function at the bottom, after the call to get_data()

    Step 5. Complete the send_email() function.
            a) Add Subject, From, and To entries to our email object. Assign them to
               our passed in values:
                    email_msg['Subject'] =
                    email_msg['From'] =
                    email_msg['To'] =

            b) Start your SMTP server at the location indicated 'Step 5b.'
               Send the message (hint: server.send_message(email_msg)
               End (quit) the server


    Step 6. Call the send_email() function at the bottom, after the call to generate_pdf().
            a) Pass into the function a (fictitious) sender and receiver email address
            b) Pass a subject
            c) Pass the name of our newly created PDF file

            That's it, test it out and troubleshoot as necessary!
"""
from pathlib import Path
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

from reportlab.lib.colors import Color, green, lavenderblush, dimgray
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


def get_data(filepath):
    data = [('Name', 'City', 'State')]
    with Path(filepath).open(encoding='utf-8') as f:
        f.readline()
        for line in f:
            fields = line.split(',')
            if len(fields) == 5:
                name, city, country = fields[1], fields[2], fields[3]
                data.append((name, city, country))

    return data


def generate_pdf(data, filename: str = 'schools.pdf'):
    doc_items = []

    doc = SimpleDocTemplate(filename, pagesize=letter, rightMargin=72,
                            leftMargin=72, topMargin=72, bottomMargin=72)

    table = Table(data, colWidths=(250, 200, 60))
    ts = TableStyle([('ALIGN', (0, 0), (-1, 0), 'CENTER'),
                     ('TEXTCOLOR', (0, 0), (-1, 0), green),
                     ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
                     ('GRID', (0, 0), (-1, -1), 1, dimgray),
                     ('BACKGROUND', (0, 0), (-1, 0), lavenderblush),
                     ('BACKGROUND', (0, 1), (-1, -1), Color(0.94, 0.92, 0.90))
                     ])

    table.setStyle(ts)
    doc_items.append(table)
    doc.build(doc_items)


def send_email(sender: str, receiver: str, subj: str, attachment_fn: str):
    email_msg = MIMEMultipart()

    # Step 5a. here
    email_msg['From'] = sender
    email_msg['To'] = receiver
    email_msg['Subject'] = subj

    try:
        attachment = Path(attachment_fn)
        part = MIMEApplication(attachment.read_text(), Name=attachment.name)
        part['Content-Disposition'] = f'attachment; filename="{attachment.name}"'
        email_msg.attach(part)

        # Step 5b. here also
        status = 'Email and attachment sent.'
        client = smtplib.SMTP('localhost', 1025)
        client.send_message(email_msg)
        client.quit()

    except Exception as err:
        status = f'Error--> {err}'

    return status


# Main code to test functions above
data = get_data('../../../resources/baseball/Schools.csv')
generate_pdf(data)
print(send_email(sender='rob@example.com',
                 receiver='john@yahoo.com',
                 subj='This is a sample email for Task2-2.',
                 attachment_fn='schools.pdf'))
