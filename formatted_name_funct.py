
def get_formatted_name(first_name, last_name, middle=''):
    """Returns a neatly formatted name"""
    if middle:
        full_name = first_name + " " + middle + " " + last_name
    else:
        full_name = first_name + " " + last_name

    return full_name.title()


