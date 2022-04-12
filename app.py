from crypt import methods
import imp
from flask import Flask, redirect, render_template, request, flash, session
from models import db, connect_db, Pet
from forms import AddPet, EditPet

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)
db.create_all()


@app.route("/")
def home_page():
    """Home Page - Display Pets"""
    pets = Pet.query.all()
    return render_template("home.html", pets=pets)


@app.route("/add-pet", methods=["GET", "POST"])
def add_pet():
    """Show Form to add pet. Handle adding"""

    form = AddPet()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        pet = Pet(name=name, species=species,
                  photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        return redirect("/")

    else:
        return render_template("add-pet.html", form=form)


@app.route("/pets/<int:pet_id>", methods=["GET", "POST"])
def display_pet(pet_id):
    """Display Pet info and form to edit pet"""
    form = EditPet()
    pet = Pet.query.get_or_404(pet_id)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f"{pet.name} updated")
        return redirect("/")

    else:
        return render_template("petprofile.html", pet=pet, form=form)
