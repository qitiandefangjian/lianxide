from flask import Blueprint,render_template, redirect, url_for, flash
from flask_login import login_user,logout_user,login_required
#from jobplus.models import User
#from jobplus.forms import LoginForm

front = Blueprint('front', __name__)


@front.route('/')
def index():
    
    return render_template('index.html',a=a)

#@front.route('/login',methods=['GET','POST'])
#def login():
#    form = LoginForm()
 #   if form.validate_on_submit():
 #       user = User.query.filter_by(email=form.password.data)
 #       if user != None and user.verify_password(form.password.data):
 #           login_user(user,form.remember_me.data)
 #           redirect(url_for('front.index'))
 #       flash('Sorry,帐号或者密码错误')
 #   return render_template('front/login.html',form=form)

#@front.route('/logout')
#@login_required
#def logout():
 #   logout_user()
 #   flash('退出登录，欢迎你的下次光临')
  #  return redirect(url_for('front.index'))


