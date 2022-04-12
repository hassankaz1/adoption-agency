from hashlib import algorithms_available
from xmlrpc.client import Boolean
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, URLField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange


class AddPet(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species Name", choices=[(
        'cat', 'cat'), ('dog', 'dog'), ('porcupine', 'porcupine')], validators=[InputRequired()])
    photo_url = URLField("Photo", validators=[Optional()])
    age = IntegerField("Age", validators=[
                       Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes", validators=[Optional()])


class EditPet(FlaskForm):
    """Form for editing pet."""

    photo_url = URLField("Photo", validators=[Optional()])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Availability")
