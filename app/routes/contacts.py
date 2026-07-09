import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from app.data.contacts import CONTACTS

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# CONFIGURATION (Ideally, move these to environment variables later)
GMAIL_USER = "anirudhsuniltiwari@gmail.com"        # Your actual Gmail address
GMAIL_PASSWORD = "xxxx xxxx xxxx xxxx"    # The 16-digit App Password you generated
RECEIVER_EMAIL = "anirudhsuniltiwari@gmail.com"    # Where you want to receive the notifications

@router.get("/contact")
def contact(request: Request):
    return templates.TemplateResponse(
        request= request,
        name="contact.html",
        context={"contacts": CONTACTS}
    )

@router.post("/contact")
async def handle_contact_form(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    message: str = Form(...)
):
    try:
        # 1. Setup the MIME email structure
        msg = MIMEMultipart()
        msg['From'] = GMAIL_USER
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = f"Portfolio Contact: Message from {name}"

        # 2. Design the email body
        body = f"You received a new portfolio message:\n\nName: {name}\nEmail: {email}\n\nMessage:\n{message}"
        msg.attach(MIMEText(body, 'plain'))

        # 3. Connect to Gmail's SMTP Server and send
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls() # Secure the connection
            server.login(GMAIL_USER, GMAIL_PASSWORD)
            server.send_message(msg)

        # Redirect back to contact page (you could also redirect to a "Success" page)
        return RedirectResponse(url="/contact?status=success", status_code=303)

    except Exception as e:
        print(f"Error sending email: {e}")
        return RedirectResponse(url="/contact?status=error", status_code=303)