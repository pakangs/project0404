from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class ShopForm(FlaskForm):
    name = StringField("가게명", validators=[DataRequired("가게명은 필수 입력 항목입니다.")])
    owner = StringField("소유주", validators=[DataRequired("소유주는 필수 입력 항목입니다.")])
    user_id = StringField("작성자", validators=[DataRequired("로그인 후 작성해주세요.")])
    file_path = StringField("첨부파일")

class ProductForm(FlaskForm):
    name = StringField("상품명", validators=[DataRequired("상품명은 필수 입력 항목입니다.")])
    cost = StringField("가격", validators=[DataRequired("가격은 필수 입력 항목입니다")])
    user_id = StringField("작성자", validators=[DataRequired("로그인 후 작성해주세요.")])

class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired("사용자이름은 필수 입력 항목입니다."), Length(min=3, max=20)])
    password1 = PasswordField('비밀번호', validators=[DataRequired("비밀번호는 필수 입력 항목입니다."), EqualTo("password2", "비밀번호가 일치하지않음")])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired("비밀번호확인은 필수 입력 사항입니다.")])
    email = EmailField('이메일', validators=[DataRequired("이메일은 필수 입력 항목입니다."), Email()])


class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired("사용자이름은 필수 입력 항목입니다."), Length(min=3, max=20)])
    password = PasswordField('비밀번호', validators=[DataRequired("비밀번호는 필수 입력 항목입니다.")])