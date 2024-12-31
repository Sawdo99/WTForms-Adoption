from flask import Flask, render_template, redirect, url_for, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, Pet
from forms import AddPetForm, EditPetForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
toolbar = DebugToolbarExtension(app)

# Create database
with app.app_context():
    db.create_all()


# Routes -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@app.route('/')
def list_pets():
    """List all pets on the homepage."""
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Handle add-pet form."""
    form = AddPetForm()
    if form.validate_on_submit():
        pet = Pet(
            name=form.name.data,
            species=form.species.data,
            photo_url=form.photo_url.data,
            age=form.age.data,
            notes=form.notes.data,
        )
        db.session.add(pet)
        db.session.commit()
        return redirect(url_for('list_pets'))
    return render_template('add_pet.html', form=form)

@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    """Show pet detail and handle edit form."""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect(url_for('list_pets'))

    return render_template('pet_detail.html', pet=pet, form=form)

