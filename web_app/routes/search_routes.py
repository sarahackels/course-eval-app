
# this is the "web_app/routes/stocks_routes.py" file ...

from flask import Blueprint, request, render_template, redirect, flash

from app.search_prof import sortdata
from app.all_professors import unique_instructors
from app.search_prof import getmean

search_routes = Blueprint("search_routes", __name__)

@search_routes.route("/search/form")
def search_form():
    print("SEARCH FORM...")
    profnames = unique_instructors()
    return render_template("search_form.html", professors=profnames)

@search_routes.route("/search/dashboard", methods=["GET", "POST"])
def search_dashboard():
    print("SEARCH DASHBOARD...")

    if request.method == "POST":
        # for data sent via POST request, form inputs are in request.form:
        request_data = dict(request.form)
        print("FORM DATA:", request_data)
    else:
        # for data sent via GET request, url params are in request.args
        request_data = dict(request.args)
        print("URL PARAMS:", request_data)

    profname = request_data.get("lastname") or "Michael Rossetti"

    try:
        profnames2 = unique_instructors()
        if profname not in profnames2:
            raise ValueError("Professor not found in the list of unique professors")

        df = sortdata(name=profname)
        profstats = getmean(df)
        
        flash("Searched for Professor Ratings!", "success")

        return render_template("search_dashboard.html", name=profname,data=df, stats=profstats)
    except Exception as err:
        print('OOPS', err)

        flash("Please check your Professor Name and try again!", "danger")
        return redirect("/search/form")
