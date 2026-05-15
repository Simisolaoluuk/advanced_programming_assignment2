from flask import Flask, render_template, abort
from models import db, Company, Status
import os

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get(
        "SECRET_KEY", "dev-secret-key-change-me"
    )
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "DATABASE_URL", "sqlite:///companies.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route("/")
    def index():
        total_companies = Company.query.count()
        total_statuses = Status.query.count()
        return render_template("index.html",
                               total_companies=total_companies,
                               total_statuses=total_statuses)

    @app.route("/companies")
    def companies():
        all_companies = Company.query.limit(200).all()
        return render_template("companies.html", companies=all_companies)

    @app.route("/companies/<int:company_id>")
    def company_detail(company_id):
        company = Company.query.get(company_id)
        if company is None:
            abort(404)
        return render_template("company_detail.html", company=company)

    @app.route("/statuses")
    def statuses():
        all_statuses = Status.query.all()
        return render_template("statuses.html", statuses=all_statuses)

    @app.errorhandler(404)
    def not_found(e):
        return render_template("error.html", message="Page not found"), 404

    @app.errorhandler(500)
    def server_error(e):
        return render_template("error.html", message="Server error"), 500

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
