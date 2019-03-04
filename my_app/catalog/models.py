import datetime
from my_app import db1


class Product(db1.Document):
    created_at = db1.DateTimeField(
        default=datetime.datetime.now, required=True
    )
    key = db1.StringField(max_length=255, required=True)
    name = db1.StringField(max_length=255, required=True)
    price = db1.DecimalField()

    def __repr__(self):
        return '<Product %r>' % self.id
