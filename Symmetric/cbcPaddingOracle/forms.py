from wtforms import Form, StringField, validators

class RegisterForm(Form):
    Name = StringField("Name", [validators.DataRequired()])
