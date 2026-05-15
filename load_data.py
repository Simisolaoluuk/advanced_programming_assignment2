from app import create_app
from models import db, Company, Status
import csv

app = create_app()

def load_statuses(path):
    with app.app_context():
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f, skipinitialspace=True)
            for row in reader:
                s = Status(status_name=row["status_name"])
                db.session.add(s)
            db.session.commit()

def load_companies(path):
    with app.app_context():
        status_lookup = {s.status_name: s.id for s in Status.query.all()}

        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f, skipinitialspace=True)
            for row in reader:
                status_id = status_lookup.get(row["CompanyStatus"])
                if not status_id:
                    continue

                c = Company(
                    name=row["CompanyName"],
                    number=row["CompanyNumber"],
                    postcode=row["RegAddress.PostCode"],
                    status_id=status_id
                )
                db.session.add(c)

            db.session.commit()

if __name__ == "__main__":
    load_statuses("data/statuses.csv")
    load_companies("data/companies_sample.csv")
