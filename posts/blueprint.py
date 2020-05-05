from flask import Blueprint
from flask import render_template

from models import Post, Tag
from .forms import PostForm, TagForm

from flask import request
from app import db

from flask import redirect
from flask import url_for

# create folder for this app templates and register app prefix
posts = Blueprint('posts', __name__, template_folder='templates') 



@posts.route('/create-post', methods=['POST', 'GET'])
def create_post():

	if  request.method == 'POST':
		title = request.form['title']
		body = request.form['body']

		try:
			post = Post(title=title, body=body)
			db.session.add(post)
			db.session.commit()

		except:
			print('Something was wrong.')

		return redirect(url_for('posts.index'))


	form = PostForm()
	active_create_post = 'active'
	context= {
	'form': form,
	'active_create_post': active_create_post,
	}
	return render_template('posts/create_post.html', context = context)




@posts.route('/create-tag', methods=['POST', 'GET'])
def create_tag():
	if request.method == 'POST':
		tag_name = request.form['tag_name']
		posts_for_tag = request.form['posts_for_tag']
		post_for_tag = Post.query.filter(Post.title == posts_for_tag)
		post_for_tag = post_for_tag.first()
		try:
			tag = Tag(tag_name = tag_name)
			db.session.add(tag)
			db.session.commit()

			new_tag = Tag.query.filter(Tag.tag_name == tag_name)
			new_tag = new_tag.first()
			new_tag.posts.append(post_for_tag)
			db.session.add(new_tag)
			db.session.commit()

		except:
			print('Something was wrong with create tag')

		return redirect(url_for('posts.index'))
		

	else:
		form = TagForm()
		active_create_tag = 'active'
		posts = Post.query.all()
		context = {
		'form': form,
		'active_create_tag': active_create_tag,
		'posts': posts,
		}

		return render_template('posts/create_tag.html', context = context)




@posts.route('/')
def index():
	
	q = request.args.get('q')


	page = request.args.get('page')
	if page and page.isdigit():
		page = int(page)
	else:
		page = 1

	if q:
		posts = Post.query.filter(Post.title.contains(q) | Post.body.contains(q)) #.all()
	else:
		posts = Post.query.order_by(Post.created.desc())


	pages = posts.paginate(page = page, per_page = 5)


	active_blog = 'active'
	context = {
	'posts': posts,
	'active_blog': active_blog,
	'pages': pages,
	}
	return render_template('posts/index.html', context = context)



@posts.route('/<slug>')
def post_detail(slug):
	post_data = Post.query.filter(Post.slug == slug).first()
	post_tags = post_data.tags.all()
	context = {
	'post_data': post_data,
	'post_tags': post_tags,
	}
	return render_template('posts/post_detail.html', context = context)



@posts.route('/tag/<slug>')
def tag_detail(slug):
	tag_data = Tag.query.filter(Tag.tag_slug == slug).first()
	tag_posts = tag_data.posts
	context = {
	'tag_data': tag_data,
	'tag_posts': tag_posts
	}
	return render_template('posts/tag_detail.html', context = context)




