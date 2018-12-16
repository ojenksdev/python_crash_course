def car_info(manufacturer, model, **features):
    """Building a car dictionary to store various cars and their features"""
    car_profile = {}
    car_profile["manufacturer"] = manufacturer
    car_profile["model"] = model
    for k, v in features.items():
        car_profile[k] = v
    return car_profile


toyota = car_info("toyota", "camry",
                  year=2014,
                  color="black",
                  navigation="yes",
                  rear_camera="yes",
                  price=21000)

print(toyota)
                  
