from flask import Flask, url_for, request
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

# string (default) accepts any text without a slash
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)} : {type(username).__name__}'

@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def show_post(post_id):
    # show the post with the given id, the id is an integer
    content = f'Post {post_id} : {type(post_id).__name__}' 
    if request.method == 'POST':
        return f'POST Method: {content}'
    else:
        return f'GET Method: {content}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath %s' % escape(subpath)

# The canonical URL for the projects endpoint has a trailing slash. 
# It’s similar to a folder in a file system. 
# If you access the URL without a trailing slash, 
# Flask redirects you to the canonical URL with the trailing slash.
@app.route('/projects/')
def projects():
    return 'The project page'

# The canonical URL for the about endpoint does not have a trailing slash. 
# It’s similar to the pathname of a file. Accessing the URL with a trailing 
# slash produces a 404 “Not Found” error. This helps keep URLs unique for 
# these resources, which helps search engines avoid indexing the same page twice.
@app.route('/about')
def about():
    return 'The about page'

# URL binding
# 1. Reversing is often more descriptive than hard-coding the URLs.
# 2. You can change your URLs in one go instead of needing to remember to manually change hard-coded URLs.
# 3. URL building handles escaping of special characters and Unicode data transparently.
# 4. The generated paths are always absolute, avoiding unexpected behavior of relative paths in browsers.
# 5. If your application is placed outside the URL root, for example, in /myapplication instead of /, url_for() properly handles that for you.
with app.test_request_context():
    print(url_for('index'))
    print(url_for('hello', next='/'))
    print(url_for('show_user_profile', username='Johnny Liu', param='test'))
