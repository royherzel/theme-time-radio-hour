from archive.models import db
from sqlalchemy.exc import IntegrityError


class Mixin():

    def create(resource):
        db.session.add(resource)
        status = 'add'
        try:
            db.session.commit()

        except IntegrityError as err:
            db.session.rollback()
            print("rollback: {}, {}".format(err.orig.diag.message_primary, err.orig.diag.message_detail))
            status = 'rollback'

        db.session.commit()
        return status

    def update(resource):
        db.session.commit()

    def delete(resource):
        db.session.delete(resource)
        db.session.commit()

    def merge(resource):
        db.session.merge(resource)
        db.session.commit()