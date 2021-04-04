from flask import Flask, app, render_template, request
from flask_mail import Mail
from flask_mail import Message

app = Flask(__name__)

#Configurar
app.config['MAIL_SERVER']= 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'davidariascalderon04@gmail.com'
app.config['MAIL_PASSWORD'] = 'Da04vid*Ari'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def index():
    
    msg = Message('Hola', sender='davidariascalderon04@gmail.com', recipients=['davariasc@correo.udistrital.edu.co'])
    
    msg.html = render_template('email.html')
        
    mail.send(msg)
    
    return render_template('email.html')




@app.route('/mensaje')
def mensaje():
    param = request.args.get('vista','')
    if(param == '1'):
        return 'ish'
    else:
        return render_template('email.html')



if __name__ == '__main__':
    app.run(port = 3000 , debug=True)
