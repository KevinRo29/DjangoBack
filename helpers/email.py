from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives

def validateUser(data):
    context = {
        'username': data['username'],
        'email': data['email'],
        'password': data['password'],
        'token': data['tokenValidation']
    }
    template = get_template('ValidateUser.html')
    content = template.render(context)
    email = EmailMultiAlternatives(
        'Validate User',
        'Validate User',
        'kevinro0829@gmail.com',
        [data['email']]
    )
    email.attach_alternative(content, 'text/html')
    email.send()

def recoveryPassword(data):
    context = {
        'email': data['email'],
        'recuperationCode': data['recuperationCode']
    }
    template = get_template('RecoveryPassword.html')
    content = template.render(context)
    email = EmailMultiAlternatives(
        'Recovery Password',
        'Recovery Password',
        'kevinro0829@gmail.com',
        [data['email']]
    )
    email.attach_alternative(content, 'text/html')
    email.send()