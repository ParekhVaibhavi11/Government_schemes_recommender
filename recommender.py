import json


# Load schemes dataset
def load_schemes():
    with open("schemes.json", "r", encoding="utf-8") as file:
        return json.load(file)


# Eligibility checking
def check_eligibility(user, scheme):

    # Age check
    if not (scheme["min_age"] <= user["age"] <= scheme["max_age"]):
        return False

    # Gender check
    if scheme["gender"] != "any" and scheme["gender"] != user["gender"]:
        return False

    # Income check
    if user["income"] > scheme["income_max"]:
        return False

    # Category check
    if "all" not in scheme["category"] and \
       user["category"] not in scheme["category"]:
        return False

    # Student check
    if scheme["student"] != "any" and \
       scheme["student"] != user["student"]:
        return False

    # Farmer check
    if scheme["farmer"] != "any" and \
       scheme["farmer"] != user["farmer"]:
        return False

    # Disability check
    if scheme["disability"] != "any" and \
       scheme["disability"] != user["disability"]:
        return False

    return True


# Recommendation function
def recommend_schemes(user):

    schemes = load_schemes()
    eligible_schemes = []

    for scheme in schemes:
        if check_eligibility(user, scheme):
            eligible_schemes.append(scheme)

    return eligible_schemes
