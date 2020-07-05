from flask import render_template, request, Blueprint

core = Blueprint('core', __name__)


@core.route("/", methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@core.route("/about")
def about():
    return render_template('about.html')


@core.route('/search', methods=['GET', 'POST'])
def search():
    search_str = request.args.get('globalsearch')
    return render_template('search.html', search_str=search_str)
