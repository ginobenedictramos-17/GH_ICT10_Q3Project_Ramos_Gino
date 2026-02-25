from pyscript import display, document
#needed consultation from AI to figure out how to make the button in html coordinate with the list

Boys = ["Abayon", "Barrientos", "Coeli", "David", "Ibay", "Mamauag", "Ramos", "Sidhu"]

Girls = ["Antes", "Casal", "Dela Cruz, F", "Dellejero", "Fukuda", "Gozum", "Lozano", "Villamayor", "Tiu"]
def show_boys(e):

    display(f'Boys: {str(Boys)}', target="output")


def show_girls(e):    
    display(f'Girls: {str(Girls)}', target="output")
