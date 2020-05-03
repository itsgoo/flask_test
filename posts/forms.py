from wtforms import Form, StringField, TextAreaField, IntegerField, SelectField
from models import Post, Tag

# Create fields for web form
class PostForm(Form):
	"""docstring for PostForm"""

	title = StringField('Title')
	body = TextAreaField('Body')

class TagForm(Form):
	posts = Post.query.all()

	mass=[]
	for post in posts:
		post.title
		tuple_1 = post.title
		mass.append(tuple_1)
		tuple_1 = 0

	tag_name = StringField('Tag name')
	posts_for_tag = SelectField(u'posts_for_tag', choices=mass)
