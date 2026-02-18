from pyscript import display, document
#needed consultation from AI to figure out how to make the button coordinate with the list

Boys = ["Gino Ramos", "Dwight Ramos", "Gurnoor Sidhu", "Lebron James", "Shohei Ohtani", "Lionel Messi", "Cristiano Ronaldo", "Oscar Barrientos", "Josua Ortiz", "Kylian Mbappe"]

Girls = ["Caitlin Clark", "Serena Williams", "Alex Eala", "Sam Kerr", "Gina Benedicta Ramos", "Bella Belen", "Detdet Pepito", "Bianca Bustamante", "Shevanna Laput"]
def show_boys(e):

    display(f'Boys: {str(Boys)}', target="output")


def show_girls(e):    
    display(f'Girls: {str(Girls)}', target="output")