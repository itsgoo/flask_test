from flask import Flask 
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

#  Create application
app = Flask(__name__) 
app.config.from_object(Configuration)

# connect ORM for DB
db = SQLAlchemy(app)


# Make migrations
migrate = Migrate(app, db)

# Create command for migrations
manager = Manager(app)
manager.add_command('db', MigrateCommand)




