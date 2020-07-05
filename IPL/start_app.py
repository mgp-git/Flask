from app import app, db
import os

db_path = app.config['SQLALCHEMY_DATABASE_URI'].lstrip('sqlite:')
if not os.path.isfile(db_path):
    db.create_all()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)