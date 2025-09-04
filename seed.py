from app import create_app
from app.models import db, User, Category

app = create_app()

with app.app_context():
    db.create_all()

    if not User.query.first():
        print("Agregando usuarios...")
        users = [
            User(username='yoeny', email='yoeny@example.com'),
            User(username='ana', email='travel@example.com'),
            User(username='marcos', email='marcos@example.com')
        ]
        db.session.add_all(users)

    if not Category.query.first():
        print("Agregando categorías...")
        categories = [
            Category(name='Funcionalidad'),
            Category(name='Seguridad'),
            Category(name='Interfaz'),
            Category(name='Rendimiento')
        ]
        db.session.add_all(categories)

    db.session.commit()
    print("Base de datos poblada correctamente!")
