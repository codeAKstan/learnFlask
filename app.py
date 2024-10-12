from flask import Flask, request, render_template, url_for, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

class NameForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['POST', 'GET'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        flash(f"Hello, {form.name.data}!", 'success')
        return redirect(url_for('index'))
    return render_template('form_wtf.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)