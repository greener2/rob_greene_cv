from flask import Blueprint, render_template

bp = Blueprint("cv_site", __name__)


@bp.get("/")
def index():
    return render_template("base.html")


@bp.get("/about-me")
def about_me_partial():
    return render_template("partials/about-me.html")


@bp.get("/prof-exp")
def professional_exp_partial():
    return render_template("partials/prof-exp.html")
