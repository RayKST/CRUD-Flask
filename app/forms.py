from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SubmitField
from wtforms.validators import DataRequired

class ProductForm(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired()])
    description = StringField('Product Description', validators=[DataRequired()])
    price = FloatField('Product Price', validators=[DataRequired()])
    category_id = IntegerField('Product Category ID', validators=[DataRequired()])
    submit = SubmitField('Create')