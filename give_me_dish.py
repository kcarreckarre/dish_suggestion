import tkinter as tk
from tkinter import messagebox

# Dishes and their required ingredients
dishes = {
    "Pasta with Tomato Sauce": ["pasta", "tomato sauce", "garlic", "olive oil"],
    "Vegetable Stir Fry": ["broccoli", "carrot", "bell pepper", "soy sauce", "olive oil"],
    "Chicken Salad": ["chicken breast", "lettuce", "tomato", "cucumber", "olive oil"],
    "Grilled Cheese Sandwich": ["bread", "cheese", "butter"],
    "Omelette": ["eggs", "milk", "cheese", "salt", "pepper"],
    "Beef Tacos": ["ground beef", "taco shells", "lettuce", "tomato", "cheese"],
    "Vegetable Soup": ["carrot", "celery", "onion", "garlic", "vegetable broth"],
    "Spaghetti Carbonara": ["spaghetti", "egg", "bacon", "parmesan cheese"],
    "Pancakes": ["flour", "milk", "egg", "sugar", "baking powder"],
    "Fruit Salad": ["apple", "banana", "orange", "grape", "yogurt"]
}

# Function to suggest dishes based on available ingredients
def suggest_dish():
    available_ingredients = [ingredient.strip().lower() for ingredient in ingredients_entry.get().split(",")]
    suggested_dishes = []
    
    for dish, required_ingredients in dishes.items():
        matching_ingredients = [ingredient for ingredient in required_ingredients if ingredient in available_ingredients]
        missing_ingredients = [ingredient for ingredient in required_ingredients if ingredient not in available_ingredients]
        
        if matching_ingredients:
            if not missing_ingredients:
                suggested_dishes.append(f"{dish} (All ingredients available)")
            else:
                suggested_dishes.append(f"{dish} (Missing ingredients: {', '.join(missing_ingredients)})")
    
    if suggested_dishes:
        messagebox.showinfo("Suggested Dishes", "\n".join(suggested_dishes))
    else:
        messagebox.showinfo("No Matches", "No dishes can be made with the available ingredients.")

# Create the main application window
app = tk.Tk()
app.title("What's for Dinner?")

# Create and place the label and text entry for ingredients
ingredients_label = tk.Label(app, text="Enter ingredients (comma separated):")
ingredients_label.pack(pady=10)
ingredients_entry = tk.Entry(app, width=50)
ingredients_entry.pack(pady=10)

# Create and place the suggest button
suggest_button = tk.Button(app, text="Suggest a Dish", command=suggest_dish)
suggest_button.pack(pady=20)

# Run the application
app.mainloop()


