from flask import Flask, render_template, request
from travel_planner import generate_plan

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/plan", methods=["POST"])
def plan():
    try:
        destinations = [
            place.strip().title()
            for place in request.form["destinations"].split(",")
            if place.strip()
        ]

        destination_count = int(request.form["destination_count"])
        days = int(request.form["days"])
        travellers = int(request.form["travellers"])
        budget_choice = request.form["budget"]
        travel_date = request.form["date"]

        if len(destinations) != destination_count:
            return render_template(
                "index.html",
                error="Please enter exactly the number of destinations selected."
            )

        if days < 1 or travellers < 1:
            return render_template(
                "index.html",
                error="Days and travellers must be at least 1."
            )

        budget_values = {
            "Budget": 1500,
            "Mid-range": 3000,
            "Luxury": 6000
        }

        budget = budget_values[budget_choice]

        result = generate_plan(
            destinations,
            days,
            travellers,
            budget,
            travel_date
        )

        if result is None:
            return render_template(
                "index.html",
                error="Available destinations: Ooty, Goa and Munnar."
            )

        return render_template("result.html", result=result)

    except (ValueError, KeyError):
        return render_template(
            "index.html",
            error="Please enter valid details in all fields."
        )


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000, debug=True)