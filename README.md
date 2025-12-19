## How to Run the Demo

This prototype is a command-line application written in Python.  
It uses only in-memory data structures and does not require any external libraries.
### Run Instructions

Clone the repository and run the program from the command line:

python smart_cater.py

## How to Use ok During the Demo
During the demo, the keyword ok is used in two different situations to control the flow of the program.

First, when entering values for a selected filter (such as ingredients or categories), typing ok means that all values for this specific filter have been entered and the program should stop asking for more values.

Second, when choosing filter types, typing ok means that all desired filters have been selected and that the program can now execute the search using the provided filters.

By using ok in these two steps, the user can first define multiple values for each filter and then clearly indicate when the overall filtering process is finished before running the search.
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



