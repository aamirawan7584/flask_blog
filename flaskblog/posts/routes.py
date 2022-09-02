from flask import Blueprint,redirect,render_template,url_for,request,flash,abort
from flask_login import login_required,current_user
from flaskblog import db
from flaskblog.posts.forms import CreatePostForm
from flaskblog.models import Post

posts = Blueprint('posts',__name__)


@posts.route("/post/new", methods=["GET", "POST"])
@login_required
def create_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data, content=form.post_content.data, author=current_user
        )
        db.session.add(post)
        db.session.commit()
        flash("Your post has been created!", "success")
        return redirect(url_for("main.home"))
    return render_template(
        "create_post.html", title="New Post", form=form, legend="New Post"
    )


@posts.route("/post/<int:post_id>")
@login_required
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("post.html", title=post.title, post=post)


@posts.route("/post/<int:post_id>/update", methods=["GET", "POST"])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = CreatePostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.post_content.data
        db.session.commit()
        flash("Post Has been updated!", "success")
        return redirect(url_for("main.home"))
    elif request.method == "GET":
        form.title.data = post.title
        form.post_content.data = post.content
    return render_template(
        "create_post.html", title="Update Post", form=form, legend="Update Post"
    )


@posts.route("/post/<int:post_id>/delete", methods=["POST"])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)

    db.session.delete(post)
    db.session.commit()
    flash("Post Has Been Deleted!", "success")
    return redirect(url_for("main.home"))





    


