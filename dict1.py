meal = {
    "entree": "salmon",
    "vegetable": "asparagus",
    "drink": "black label whisky"
    }

print(meal["drink"])

if "drink" in meal:
    print("YESSIR")
else: 
    print("Taking it light.")

meal["appetizer"] = "bacon"
meal["drink"] = "bulleit"
del meal["entree"]
