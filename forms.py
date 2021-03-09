"""Forms file used in route views to render secure HTML forms"""

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import InputRequired, AnyOf, URL, Optional, NumberRange

class AddPetForm(FlaskForm):
    """The form to add a new pet for adoption"""

    name = StringField("Pet name", validators=[InputRequired(message="Pet name cannot be blank")])
    species = StringField("Species", validators=[
        InputRequired(message="Species type cannot be blank"),
        AnyOf(values=("Cat", "Dog", "Porcupine"), message="I'm sorry, we only accept Cats, Dogs or Porcupines (capitalized) :(")
    ])
    photo_url = StringField("Photo URL", validators=[
        Optional(),
        URL(message="This is not a valid image URL")
    ])
    age = IntegerField("Age", validators=[
        Optional(),
        NumberRange(min=0, max=30, message="Pet age has to be between 0 and 30")
    ])
    notes = StringField("Notes")

class EditPetForm(FlaskForm):
    """The form to edit pets"""

    photo_url = StringField("Photo URL", validators=[
        Optional(),
        URL(message="This is not a valid image URL")
    ])
    notes = StringField("Notes")
    available = BooleanField("Available for adoption")