from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = '12fdec04ddc118907ad5d5ce1c87ad05402fa19055f4302c1c5280f8de6f31f2'

# Configuración para Gmail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'mextlikallimprenta@gmail.com'  # tu correo de Gmail
app.config['MAIL_PASSWORD'] = 'kele hlth xevg swxn'  # ⚠️ contraseña de aplicación de Gmail

mail = Mail(app)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Obtener datos del formulario
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        if not all([name, email, subject, message]):
            flash('Por favor, completa todos los campos.', 'danger')
            return redirect(url_for('home'))

        try:
            # Configurar y enviar correo
            msg = Message(
                subject=f"Mensaje de contacto: {subject}",
                sender=app.config['MAIL_USERNAME'],
                recipients=['abnerck9@gmail.com'],  # cambia al correo destino real
                body=f"""Nombre: {name}
Email: {email}
Mensaje: {message}"""
            )
            msg.reply_to = email  # Para poder responder directamente al remitente
            mail.send(msg)
            flash('¡Mensaje enviado con éxito!', 'success')
        except Exception as e:
            flash(f'Error al enviar: {str(e)}', 'danger')

        return redirect(url_for('home'))

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
