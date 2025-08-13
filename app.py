from flask import Flask, render_template, flash, redirect, url_for
from forms import LeaveApplicationForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key_here"

@app.route("/")
def home():
    return render_template("layout/home.html")

@app.route("/leave", methods=["GET", "POST"])
def leave():
    form = LeaveApplicationForm()
    if form.validate_on_submit():
        duration = (form.end_date.data - form.start_date.data).days + 1
        flash(f"Leave application submitted for {duration} days. Have a nice break!", "success")
        return redirect(url_for("home"))
    return render_template("layout/leave.html", form=form)

if __name__ == "__main__":
    app.run(debug=False)

