def greeting(name, language):
    """Simple function to greet user in different languages"""
    # check the supplied language against the existing options
    match language:
        case "English":
            return "Hello {}!".format(name)
        case "Norwegian":
            return "Hei {}!".format(name)
        # default case
        case _:
            return "I don't speak your language!".format(name)