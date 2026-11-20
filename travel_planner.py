import random

destinations = {
    "Ooty": {
        "attractions": [
            "Ooty Lake",
            "Botanical Garden",
            "Doddabetta Peak"
        ],
        "hotel": "Fortune Resort Ooty",
        "food": "South Indian Restaurant",
        "weather": "Cool and Pleasant"
    },

    "Goa": {
        "attractions": [
            "Baga Beach",
            "Calangute Beach",
            "Fort Aguada"
        ],
        "hotel": "Taj Exotica Goa",
        "food": "Goan Restaurant",
        "weather": "Warm and Sunny"
    },

    "Munnar": {
        "attractions": [
            "Tea Gardens",
            "Echo Point",
            "Mattupetty Dam"
        ],
        "hotel": "Ragamaya Resort",
        "food": "Kerala Restaurant",
        "weather": "Cool and Cloudy"
    }
}

activities = [
    "Sightseeing",
    "Photography",
    "Boating",
    "Shopping",
    "Nature Walk",
    "Trekking"
]


def generate_plan(places, days, travellers, budget, travel_date):

    for place in places:
        if place not in destinations:
            return None

    itinerary = []
    total_cost = 0

    for day in range(1, days + 1):

        place_name = places[(day - 1) % len(places)]
        place = destinations[place_name]

        daily_cost = budget * travellers
        total_cost += daily_cost

        itinerary.append({
            "day": day,
            "destination": place_name,
            "weather": place["weather"],
            "morning": random.choice(activities),
            "afternoon": random.choice(activities),
            "attraction": random.choice(place["attractions"]),
            "hotel": place["hotel"],
            "food": place["food"],
            "cost": daily_cost
        })

    return {
        "destinations": places,
        "days": days,
        "travellers": travellers,
        "travel_date": travel_date,
        "itinerary": itinerary,
        "total_cost": total_cost
    }