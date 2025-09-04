from flask import Blueprint, render_template, request, redirect, url_for
from .models import db, Requirement, Category, User

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    requirements = Requirement.query.all()
    return render_template('index.html', requirements=requirements)

@bp.route('/create', methods=['GET', 'POST'])
def create_requirement():
    categories = Category.query.all()
    users = User.query.all()

    if request.method == 'POST':
        new_req = Requirement(
            title=request.form['title'],
            description=request.form['description'],
            priority=request.form['priority'],
            status='Pendiente',
            category_id=request.form.get('category_id'),
            user_id=request.form['user_id']
        )
        db.session.add(new_req)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('create.html', categories=categories, users=users)
