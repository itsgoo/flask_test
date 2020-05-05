
from app import app
from app import db
from posts.blueprint import posts
from dashbord.blueprint import dashbord
import view


# create application (blueprint)
app.register_blueprint(posts, url_prefix='/blog')
app.register_blueprint(dashbord, url_prefix='/dashbord')

if __name__ == '__main__':
	app.run()