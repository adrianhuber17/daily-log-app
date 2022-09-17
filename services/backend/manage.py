#manage.py

import sys,os
from flask.cli import FlaskGroup
from app import create_app, db
# from app.api.models

app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command('create_db_dev')
def create_db():
    os.system("createdb app_dev")
    db.create_all()
    db.session.commit()
    print("database creation completed")

@cli.command('reset_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
    print("database reset done!")

if __name__ == "__main__":
    cli()