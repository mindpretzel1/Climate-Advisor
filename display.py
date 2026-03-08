def generate_intro(impact_level):

    if impact_level == "low":
        return "Your lifestyle already has a relatively low climate impact. " \
               "Here are a few small ways you could reduce it further:"
    elif impact_level == "moderate":
        return "Your climate impact is moderate. " \
               "Here are a few practical ways you could reduce it:"
    else:
        return "Your climate impact is relatively high. " \
               "The following changes could significantly reduce your carbon footprint:"  