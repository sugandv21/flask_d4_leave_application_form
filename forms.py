from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from datetime import date

class LeaveApplicationForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    department = StringField("Department", validators=[DataRequired()])
    reason = TextAreaField("Reason", validators=[DataRequired()])
    start_date = DateField("Start Date", format='%Y-%m-%d', validators=[DataRequired()])
    end_date = DateField("End Date", format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField("Apply")

    def validate_end_date(self, field):
        if self.start_date.data and field.data:
            if field.data < self.start_date.data:
                raise ValidationError("End date cannot be earlier than start date.")
