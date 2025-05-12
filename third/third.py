def greeting(name, language):
    """Simple function to greet user in different languages"""
    # check that inputs are strings
    if not type(name) is str:
        raise TypeError("name needs to be a string")
    if not type(language) is str:
        raise TypeError("language needs to be a string")
    # check the supplied language against the existing options
    match language:
        case "English":
            return "Hello {}!".format(name)
        case "Norwegian":
            return "Hei {}!".format(name)
        # default case
        case _:
            return "I don't speak your language!".format(name)