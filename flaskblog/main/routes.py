from flask import Blueprint,redirect,render_template,url_for,request
from flaskblog.models import Post

main = Blueprint('main',__name__)

@main.route('/favicon.ico')
def favicon():
    return redirect(url_for('static' ,filename='favicon.ico'))

@main.route("/")
@main.route("/home")
def home():
    page_num = request.args.get("page", 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(
        page=page_num, per_page=5
    )
    return render_template("home.html", posts=posts)


@main.route("/about")
def about():
    return render_template("about.html", title="About")