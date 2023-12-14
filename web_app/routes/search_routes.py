
# this is the "web_app/routes/stocks_routes.py" file ...

from flask import Blueprint, request, render_template, redirect, flash

from app.search_prof import sortdata

search_routes = Blueprint("search_routes", __name__)

@search_routes.route("/search/form")
def search_form():
    print("SEARCH FORM...")
    return render_template("search_form.html")

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

    name = request_data.get("lastname") or "Rossetti"

    try:
        #df = sortdata(name)
        
        flash("Searched for Professor Ratings!", "success")

        return render_template("search_dashboard.html", name=name)
    except Exception as err:
        print('OOPS', err)

        flash("Please check your Professor Name and try again!", "danger")
        return redirect("/search/form")

#
# API ROUTES
#
'''
@stocks_routes.route("/api/stocks.json")
def stocks_api():
    print("STOCKS DATA (API)...")

    # for data supplied via GET request, url params are in request.args:
    url_params = dict(request.args)
    print("URL PARAMS:", url_params)
    symbol = url_params.get("symbol") or "NFLX"

    try:
        df = fetch_stocks_data(symbol=symbol)
        data = df.to_dict("records")
        return {"symbol": symbol, "data": data }
    except Exception as err:
        print('OOPS', err)
        return {"message":"Market Data Error. Please try again."}, 404

'''
