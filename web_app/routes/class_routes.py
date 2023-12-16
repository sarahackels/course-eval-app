
# this is the "web_app/routes/stocks_routes.py" file ...

from flask import Blueprint, request, render_template, redirect, flash

from app.search_class import sortdata2
from app.all_classes import unique_classes

class_routes = Blueprint("class_routes", __name__)

@class_routes.route("/class_search/form")
def classsearch_form():
    print("SEARCH FORM...")
    classesnames = unique_classes()
    return render_template("class_search.html",courses=classesnames )

@class_routes.route("/class_search/dashboard", methods=["GET", "POST"])
def classsearch_dashboard():
    print("SEARCH DASHBOARD...")

    if request.method == "POST":
        # for data sent via POST request, form inputs are in request.form:
        request_data = dict(request.form)
        print("FORM DATA:", request_data)
    else:
        # for data sent via GET request, url params are in request.args
        request_data = dict(request.args)
        print("URL PARAMS:", request_data)

    coursename = request_data.get("course") or "OPIM244"

    try:
        classesnames2 = unique_classes()
        if coursename not in classesnames2:
            raise ValueError("Class not found in the list of unique classes")
        
        df = sortdata2(name=coursename)
        
        flash("Searched for Class Ratings!", "success")

        return render_template("class_dashboard.html", name=coursename,data=df)
    
    except Exception as err:
        print('OOPS', err)

        flash("Please check your class name and try again!", "danger")
        return redirect("/class_search/form")