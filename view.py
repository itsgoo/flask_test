from app import app
from flask import render_template
from models import Post, Tag

@app.route('/')
def index():
	name = 'Gellio'

	last_time = 0
	all_posts = Post.query.all()
	for post in all_posts:
		if last_time != 0:
			if post.created > last_time:
				last_time = post.created
				last_post = post
		else:
			last_time = post.created
			last_post = post


	context = {
	'n': name,
	'last_post': last_post,
	'last_time': last_time,
	}
	return render_template('index.html', context=context)