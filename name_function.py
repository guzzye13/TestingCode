def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = first + ' ' + middle + ' ' + last  # takes in a first, last and middle name
    else:
        full_name = first + ' ' + last
    return full_name.title()  # returns a neatly formatted full name
