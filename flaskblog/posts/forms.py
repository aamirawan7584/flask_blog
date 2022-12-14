from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired

class CreatePostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    post_content = TextAreaField("Content", validators=[DataRequired()])
    submit = SubmitField("Post")
