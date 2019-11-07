from flask import Flask, render_template, flash, redirect, url_for, request
from flask_wtf import FlaskForm
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, validators,RadioField
from wtforms.validators import InputRequired




app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'FLASKAPP'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/symptoms',methods=['GET', 'POST'])
def symptoms():
    form = MyForm()
    
    if  request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        fever = form.fever.data
        abdpain = form.abdpain.data
        vomit = form.vomit.data
        stool = form.stool.data
        muspain = form.muspain.data
        sweating = form.sweating.data
        chills = form.chills.data
        cough = form.cough.data


        cur = mysql.connection.cursor()

        cur.execute("INSERT INTO flaskusers(name, email, fever, abdpain, vomit, stool, muspain, sweating, chills, cough ) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (name, email, fever, abdpain, vomit, stool, muspain, sweating, chills, cough))

        mysql.connection.commit()

        cur.close()

        flash('You have successfully submitted the symptoms', 'success')
        return redirect(url_for('home'))
    return render_template('symptoms.html', form=form)    

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    conform = ConForm()
    if conform.validate_on_submit():
        flash("form submitted successfully","success")
    else:
        flash("form not submitted error","danger")
    
    return render_template('predict.html', conform=conform)    



class MyForm(FlaskForm):

    name = StringField('Username',[validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    fever = RadioField('Do you have fever ?', choices=[('yes','YES'),('no','NO')])
    abdpain = RadioField('Do have abdominal pain ?',choices=[('yes','YES'),('no','NO')])
    vomit = RadioField('Are you vomiting ?', choices=[('yes','YES'),('no','NO')])
    stool = RadioField('Do yo have blood in stool ?',choices=[('yes','YES'),('no','NO')])
    muspain = RadioField('Do yo have muscle pain ?',choices=[('yes','YES'),('no','NO')])
    sweating = RadioField('Are you suffering from profuse sweating ?', choices=[('yes','YES'),('no','NO')])
    chills = RadioField('Are suffering from shaking chills ?', choices=[('yes','YES'),('no','NO')])
    cough = RadioField('Do yo have cough ?', choices=[('yes','YES'),('no','NO')])

class ConForm(FlaskForm):

    country = StringField('Country Name ', [validators.Length(min=4, max=25)])


if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)

    # CREATE TABLE flaskusers(ID INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(30), email VARCHAR(30), fever VARCHAR(30), abdpain VARCHAR(30), vomit VARCHAR(30), stool VARCHAR(30), muspain VARCHAR(30), sweating VARCHAR(30), chills VARCHAR(30), cough VARCHAR(30));