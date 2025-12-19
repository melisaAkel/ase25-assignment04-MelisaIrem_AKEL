## How to Run the Demo

This prototype is a command-line application written in Python.  
It uses only in-memory data structures and does not require any external libraries.
### Run Instructions

Clone the repository and run the program from the command line:

python smart_cater.py

## How to Use ok During the Demo

During the demo, the keyword ok is used to indicate that the current input step is finished.

When entering filter values (such as ingredients or categories), typing ok tells the program that no more values will be added for that filter and that it should move on to the next step.

When selecting filter types, typing ok indicates that all desired filters have been added and that the search can be executed.

This allows the user to apply multiple filters and multiple values in a flexible way before running the search.
## Exit the Program

You can type exit at any time to terminate the program.
## Example Runs

### Example 1: Search by Ingredient

Choose a filter to add: name | ingredient | category  
Filter type: ingredient  
Enter ingredient values one by one. Type ok when finished.  
> onion  
> olive oil  
> ok  

ingredient filter added.

Filter type: ok

Search Results:  
- Zeytinyağli Yaprak Sarma  
  Ingredients: grape leaves, rice, onion, olive oil, herbs  
  Categories: vegan, traditional  

----------------------------------------

### Example 2: Search by Category

Filter type: category  
Enter category values one by one. Type ok when finished.  
> vegan  
> traditional  
> ok  

category filter added.

Filter type: ok

This returns all meals that are both vegan and traditional.

---

### Combined Filters – Working Example

Filter type: ingredient
Enter ingredient values one by one. Type ok when finished.
> onion  
> olive oil  
> ok  
ingredient filter added.

Filter type: category
Enter category values one by one. Type ok when finished.
> vegan  
> traditional  
> ok  
category filter added.

Filter type: ok

Search Results:
- Zeytinyağli Yaprak Sarma
  Ingredients: grape leaves, rice, onion, olive oil, herbs
  Categories: vegan, traditional

- İmam Bayildi
  Ingredients: eggplant, onion, tomato, olive oil, garlic
  Categories: vegan, traditional
----------------------------------------



