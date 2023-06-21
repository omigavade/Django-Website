from django.shortcuts import render,redirect
from website.models import Contact,Demo
from django.contrib import messages
from django.core.mail import send_mail
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import datetime
from pytz import timezone
from ics import Calendar, Event, Organizer




def index(request):
    return render(request, 'website/index.html')

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        cname = request.POST['cname']
        email = request.POST['email']
        phone = request.POST['phone']
        product = request.POST['product']
        message = request.POST['message']

        if len(fname) < 2 or len(email) < 3 or len(phone) < 10 or len(message) < 10:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(fname=fname, lname=lname, cname=cname, email=email, phone=phone, product=product, message=message)
            contact.save()
            subject = 'Thank you for reaching out to Pratima.AI'
            message = f'Dear {fname},\n\nThank you for contacting Pratima.AI! We appreciate your interest in our chatbot services and would be delighted to assist you with your query. We value your time and will make every effort to provide you with a prompt and comprehensive response.\n\nOur dedicated team of experts has received your message and will carefully review the details you provided. We understand that your question or concern is important, and we want to assure you that we are committed to delivering a satisfactory resolution.\n\nAt Pratima.AI, we strive to provide cutting-edge AI-powered chatbot solutions that cater to the unique needs of our clients. Our team combines technical expertise, industry knowledge, and a passion for innovation to create chatbot experiences that enhance customer engagement and streamline business processes.\n\nPlease note that we aim to respond to all inquiries within 24-48 hours, excluding weekends and holidays. If your query requires immediate attention, we kindly request your patience as we expedite our response.\n\nIn the meantime, I encourage you to explore our website at www.pratimaai.com to learn more about our chatbot offerings, case studies, and success stories. We are confident that our solutions can empower your business and drive growth.\n\nOnce again, thank you for considering Pratima.AI as your chatbot partner. We look forward to addressing your query and providing you with the information you need. Should you have any additional questions or require further assistance, please dont hesitate to reach out to us.\n\nBest regards,\n\nAbhishek Patil\nCustomer Support Representative\nPratima.AI'
            email_from ='contact.pratimaai@gmail.com'
            rec_list = [email,]
            send_mail(subject,message,email_from,rec_list)

            messages.success(request, 'Form submitted successfully.')
            return redirect('contact')

    return render(request, 'website/contact.html')    

def products(request):
    return render(request, 'website/products.html')

def privacypolicy(request):
    return render(request, 'website/privacypolicy.html')

def terms(request):
    return render(request, 'website/terms.html')



def demo(request):
    if request.method == 'POST':
        # Retrieve form data
        fname = request.POST['fname']
        lname = request.POST['lname']
        cname = request.POST['cname']
        email = request.POST['email']
        phone = request.POST['phone']
        product = request.POST['product']
        demo_date = request.POST['demo_date']
        demo_time = request.POST['demo_time']
        message = request.POST['message']

        if len(fname) < 2 or len(email) < 3 or len(phone) < 10 or len(message) < 10:
            messages.error(request, "Please fill the form correctly")
        else:
            subject = f'Thank you for booking a demo of {product}'
            message_text = f'Dear {fname},\n\nThank you for booking a demo of Pratima.AI Chatbot! We appreciate your interest in our product and look forward to showcasing its capabilities to you. We are excited to demonstrate how our advanced AI-powered chatbot can revolutionize your business operations and enhance customer experiences.\n\nOur team has received your demo request for the following date and time:\n\nDate: {demo_date}\nTime: {demo_time}\n\nOne of our representatives will reach out to you shortly to finalize the preferred platform and provide further details.\n\nDuring the demo, we will provide an in-depth overview of Pratima.AI Chatbot, its features, and how it can be tailored to meet your specific requirements. We will also be happy to answer any questions you may have and address any concerns related to the implementation and integration of the chatbot into your existing systems.\n\nAt Pratima.AI, we are committed to delivering top-notch chatbot solutions that drive customer engagement, improve operational efficiency, and generate tangible results for your business. Our team of experts will work closely with you to understand your unique needs and provide tailored recommendations to ensure a successful implementation.\n\nMeanwhile, we invite you to explore our website at www.pratimaai.com to learn more about our chatbot offerings, success stories, and industry-specific solutions. We believe that Pratima.AI Chatbot has the potential to transform the way you interact with your customers and elevate your business to new heights.\n\nOnce again, thank you for choosing Pratima.AI as your chatbot partner. We are confident that our demo will demonstrate the value and potential of our chatbot solution for your organization. If you have any additional questions or need further assistance, please feel free to reach out to us at any time.\n\nWe look forward to speaking with you soon!\n\nBest regards,\n\nAbhishek Patil\nCustomer Support Representative\nPratima.AI'

            # Combine date and time into a single string
            datetime_str = f'{demo_date} {demo_time}'

            # Create the datetime object in the specified timezone
            tz = timezone('Asia/Kolkata')  # Replace with the desired timezone
            demo_datetime = datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M').replace(tzinfo=tz)

            # Create the calendar event
            event = Event()
            event.name = 'Pratima.AI Chatbot Demo'
            event.begin = demo_datetime
            event.end = demo_datetime + datetime.timedelta(hours=1)  # Set the demo duration (1 hour in this example)
            event.description = f'Pratima.AI Chatbot Demo for {product}'
            event.location = 'Online Demo'  # Update with your desired location

            # Create the organizer
            organizer = Organizer(
                common_name='Abhishek Patil',
                email='contact.pratimaai@gmail.com'
            )
            event.organizer = organizer

            # Create the calendar and add the event
            cal = Calendar()
            cal.events.add(event)

            # Generate the calendar invitation content
            cal_content = str(cal)

            # Create the email message
            email_message = EmailMultiAlternatives(subject, message_text, 'goldenproject555@gmail.com', [email])
            email_message.attach_alternative(message_text, "text/plain")
            email_message.attach("invitation.ics", cal_content, "text/calendar")

            # Send the email
            email_message.send()

            messages.success(request, 'Demo booking submitted successfully.')
            return redirect('demo')

    return render(request, 'website/demo.html')

    return render(request, 'website/demo.html')

def services(request):
    return render(request, 'website/services.html')


def virtualbuddy(request):
    return render(request, 'website/virtualbuddy.html')

def socialmediabot(request):
    return render(request, 'website/socialmediabot.html')

def textbot(request):
    return render(request, 'website/textbot.html')

def voicebot(request):
    return render(request, 'website/voicebot.html')


def telegrambot(request):
    return render(request, 'website/telegrambot.html')


def whatsappbot(request):
    return render(request, 'website/whatsappbot.html')



def smsbot(request):
    return render(request, 'website/smsbot.html')


def emailbot(request):
    return render(request, 'website/emailbot.html')


def newsbot(request):
    return render(request, 'website/newsbot.html')


