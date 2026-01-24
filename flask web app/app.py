from flask import Flask,render_template,request,flash
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
from flask_mail import Mail, Message
app = Flask(__name__)

app.config['SECRET_KEY'] = "09012007"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///form.db'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'engineeringmeth09@gmail.com'
app.config['MAIL_PASSWORD'] = 'vnxw ssfn fwwm qlso'
db = SQLAlchemy(app)    

mail=Mail(app)

class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    date = db.Column(db.String(20))
    occupation = db.Column(db.String(50))

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        date = request.form["date"]
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        occupation = request.form["occupation"]

        form = Form(first_name=first_name, last_name=last_name, email=email, date=date_obj, occupation=occupation)
        db.session.add(form)
        db.session.commit()
        Message_body = f"Dear {first_name} {last_name},\n\nThank you for submitting your job application for the position of {occupation}.\n\nBest regards,\nCompany HR Team"

        message = Message(subject="Job Application Received",
                          sender=app.config['MAIL_USERNAME'],
                            recipients=[email],
                            body=Message_body)
        mail.send(message)


        flash(f"{first_name} ,Form submitted successfully!", "success")

    return render_template("index.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5001)



