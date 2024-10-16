from flask import Flask, request, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "mysecretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Form class
class NameForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message="Your name is required")])
    email = StringField('Email', validators=[DataRequired(message="Enter your email address")])
    submit = SubmitField('Submit')

# Define a User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

@app.route('/', methods=['GET', 'POST'])
def home():
    form = NameForm()
    if form.validate_on_submit():
        # Check if the user already exists
        if User.query.filter_by(username=form.name.data).first():
            flash('Username already exists!', 'error')
        elif User.query.filter_by(email=form.email.data).first():
            flash('Email already exists!', 'error')
        else:
            # Create new user and save to the database
            user = User(username=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
            flash('User added successfully!', 'success')
        return redirect(url_for('home'))
    
    users = User.query.all()
    return render_template('index.html', form=form, users=users)


@app.route('/update/<int:user_id>', methods=['GET', 'POST'])
def update(user_id):
    user = User.query.get_or_404(user_id)  # Fetch the user by ID or return 404 if not found
    form = NameForm()
    
    if form.validate_on_submit():
        user.username = form.name.data  # Update the username
        user.email = form.email.data  # Update the email
        db.session.commit()
        flash('User updated successfully!', 'success')
        return redirect(url_for('home'))
    
    # Pre-populate the form with existing user data
    form.name.data = user.username
    form.email.data = user.email
    return render_template('update.html', form=form, user=user)

@app.route('/delete/<int:user_id>', methods=['POST'])
def delete(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully!', 'success')
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
