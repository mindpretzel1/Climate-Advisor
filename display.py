import matplotlib.pyplot as plt

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

#TODO: this chart is streamlit specific.
#Create front end display module seperately
#possibly called visuals, dont forget matplolib
#import too
def create_chart(percentage_breakdown): 

    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.size": 11
    })

    fig, ax = plt.subplots() #creating bar chart
    fig.patch.set_facecolor("#F5F5EF")
    ax.set_facecolor("#F5F5EF")

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    categories = list(percentage_breakdown.keys())
    values = list(percentage_breakdown.values())

    ax.bar(categories, values, color="#2E8B57")

    ax.set_ylabel("Percent of Climate Impact")
    ax.set_ylim(0, 30)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    return fig