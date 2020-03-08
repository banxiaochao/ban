from wtforms import From,StringField,IntegerField

from wtfroms.validators import Length,NumberRange,DetaRequired

class SearchFrom(From):
    q = StringField(validators=[DetaRequired(),Length(min=1,max=30)])
    page = IntegerField(validators=[NumberRange(min=1,max=99)],default=1)