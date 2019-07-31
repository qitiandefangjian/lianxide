from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,ValidationError, PasswordField,BooleanField
from wtforms.validators import DataRequired,Email, Length,EqualTo,Required
from jobplus.models import User,db



class LoginForm(FlaskForm):
    email = StringField('邮箱地址',validators=[Required(),Email(),Length(3,30)])
    password = PasswordField('密码',validators=[Required(),Length(3,30)])
    remember_me = BooleanField('记住帐号')
    submit = SubmitField('提交')
    def validate_email(self,field):
        if field.data and not User.query.filter_by(email=field.data).first():
            return   ValidationError('邮箱未注册')
    def validate_password(self,field):
        user = User.query.filter_by(email=field.data).first()
        if fiele.data and not user.check_password(field.data):
            return   ValidationError('密码错误')

class RegisterForm(FlaskForm):
    name = StringField('用户名',validators=[Required(),Length(3,30)])
    email = StringField('邮箱地址',validators=[Required(),Email(),Length(3,30)])
    password = PasswordField('密码', validators=[Required(),Length(3,30)])
    repeat_password = PasswordField('重复密码', validators=[Required(),Length(3,30),EqualTo('password')])
    submit = SubmitField('提交')
    def validate_name(self,field):
        if field.data and User.query.filter_by(name=field.data).first():
            return ValidationError('帐号已经注册')
    def validate_email(self,field):
        if field.data and User.query.filter_by(email=field.data).first():
            return ValidationError('邮箱已经注册')
    def create_user(self):
        user = User(name=self.name,email=self.email,password=self.password)
        db.session.add(user)
        db.session.commit()
        return user


