from flask import Blueprint, request, flash, render_template
from flask_login import login_required, current_user
from . import db


views = Blueprint('views', __name__)


@views.route('/', methods=['GET','POST'])
@login_required
def pt100():
    return render_template("pt100.html", user=current_user)

@views.route('/pt100', methods=['GET','POST'])
@login_required
def pt():
    return render_template("pt100.html", user=current_user)


@views.route('/upevents', methods=['GET','POST'])
@login_required
def upevents():
    return render_template("upevents.html", user=current_user)


@views.route('/about', methods=['GET','POST'])
@login_required
def about():
    return render_template("about.html", user=current_user)


@views.route('/register', methods=['GET','POST'])
@login_required
def register():
    return render_template("register.html", user=current_user)


@views.route('/curated0', methods=['GET','POST'])
@login_required
def curated():
    return render_template("curated0.html", user=current_user)

@views.route('/curated1', methods=['GET','POST'])
@login_required
def curated1():
    return render_template("curated1.html", user=current_user)

@views.route('/curated2', methods=['GET','POST'])
@login_required
def curated2():
    return render_template("curated2.html", user=current_user)




@views.route('/curated3', methods=['GET','POST'])
@login_required
def curated3():
    return render_template("curated3.html", user=current_user)


@views.route('/periodt', methods=['GET','POST'])
@login_required
def period():
    return render_template("periodt.html", user=current_user)


@views.route('/epfor', methods=['GET','POST'])
@login_required
def epfor():
    return render_template("epfor.html", user=current_user)


@views.route('/map1', methods=['GET','POST'])
@login_required
def map1():
    return render_template("map1.html", user=current_user)

@views.route('/game', methods=['GET','POST'])
@login_required
def game():
    return render_template("game.html", user=current_user)

@views.route('/rthank', methods=['GET'])
@login_required
def rthank():
    return render_template("rthank.html", user=current_user)

@views.route('/redeem1', methods=['GET','POST'])
@login_required
def redeem1():
    return render_template("redeem1.html", user=current_user)

@views.route('/discount-page', methods=['GET','POST'])
@login_required
def discount_page():
    return render_template("discount-page.html", user=current_user)






