from typing import List, Dict

Meal = Dict[str, object]


def create_meals() -> List[Meal]:
    # I added some traditional foods from my country
    return [
        {
            "name": "Zeytinyağli Yaprak Sarma",
            "ingredients": ["grape leaves", "rice", "onion", "olive oil", "herbs"],
            "categories": ["vegan", "traditional"]
        },
        {
            "name": "Mercimek Çorbasi",
            "ingredients": ["red lentils", "onion", "carrot", "spices"],
            "categories": ["vegan", "quick", "traditional"]
        },
        {
            "name": "Kuru Fasulye",
            "ingredients": ["white beans", "onion", "tomato paste", "olive oil"],
            "categories": ["traditional", "gluten-free"]
        },
        {
            "name": "İmam Bayildi",
            "ingredients": ["eggplant", "onion", "tomato", "olive oil", "garlic"],
            "categories": ["vegan", "traditional"]
        },
        {
            "name": "Tavuk Sis",
            "ingredients": ["chicken", "yogurt", "spices", "pepper"],
            "categories": ["grilled", "traditional"]
        },
        {
            "name": "Çoban Salatasi",
            "ingredients": ["tomato", "cucumber", "pepper", "olive oil"],
            "categories": ["vegan", "quick", "traditional"]
        }
    ]


def collect_multiple_values(label: str) -> List[str]:
    # I allow the user to enter multiple values for more precise filtering
    values = []
    print(f"Enter {label} values one by one. Type 'ok' when finished.")
    while True:
        value = input("> ").strip().lower()
        if value == "ok":
            break
        values.append(value)
    return values


def matches_all_ingredients(meal: Meal, queries: List[str]) -> bool:
    # I use AND logic so that all ingredient queries must match
    return all(
        any(q in ingredient.lower() for ingredient in meal["ingredients"])
        for q in queries
    )


def matches_all_categories(meal: Meal, queries: List[str]) -> bool:
    # I use AND logic here to ensure all selected categories apply
    return all(
        any(q in category.lower() for category in meal["categories"])
        for q in queries
    )


def matches_name(meal: Meal, queries: List[str]) -> bool:
    # I keep name matching simple and readable
    return all(q in meal["name"].lower() for q in queries)


def search_meals(
    meals: List[Meal],
    search_filters: Dict[str, List[str]]
) -> List[Meal]:

    results = []

    for meal in meals:
        match = True

        # I apply each selected filter step by step
        if "name" in search_filters:
            match &= matches_name(meal, search_filters["name"])

        if "ingredient" in search_filters:
            match &= matches_all_ingredients(meal, search_filters["ingredient"])

        if "category" in search_filters:
            match &= matches_all_categories(meal, search_filters["category"])

        if match:
            results.append(meal)

    return results


def print_meals(meals: List[Meal]):
    # I print results in a simple, readable format
    if not meals:
        print("No meals found.")
        return

    for meal in meals:
        print(f"- {meal['name']}")
        print(f"  Ingredients: {', '.join(meal['ingredients'])}")
        print(f"  Categories: {', '.join(meal['categories'])}")
        print()


def main():
    meals = create_meals()
    print("Meal Search Demo")
    print("Type 'exit' at any time to quit.\n")

    while True:
        search_filters = {}

        print("Choose a filter to add: name | ingredient | category")
        print("Type 'ok' when you are done adding filters.\n")

        while True:
            search_type = input("Filter type: ").strip().lower()

            if search_type == "exit":
                print("Exiting SmartCater. Goodbye.")
                return

            # I use 'ok' to indicate that the user finished selecting filters
            if search_type == "ok":
                break

            if search_type not in {"name", "ingredient", "category"}:
                print("Invalid filter type.\n")
                continue

            # I collect multiple values for the chosen filter
            values = collect_multiple_values(search_type)

            if values:
                search_filters[search_type] = values
                print(f"{search_type} filter added.\n")

        if not search_filters:
            print("No filters provided.\n")
            continue

        results = search_meals(meals, search_filters)

        print("\nSearch Results:")
        print_meals(results)
        print("-" * 40)


if __name__ == "__main__":
    main()
