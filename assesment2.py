purchase_history = {}
def add_purchase(customer, item):
    if customer not in purchase_history:
        purchase_history[customer] = []
    purchase_history[customer].append(item)
    print(f"{item} added to {customer}'s purchase history.")

def show_history(customer):
    if customer in purchase_history:
        print(f"Purchase history of {customer}: {purchase_history[customer]}")
    else:
        print(f"No history found for {customer}.")
def recommend_product(customer):
    if customer not in purchase_history or len(purchase_history[customer]) == 0:
        print("No purchases yet. Recommendation: Popular Item - 'Headphones'")
    else:
        from collections import Counter
        items = purchase_history[customer]
        most_common_item = Counter(items).most_common(1)[0][0]
        print(f"Recommended for {customer}: {most_common_item}")

add_purchase("Alice", "Laptop")
add_purchase("Alice", "Mouse")
add_purchase("Alice", "Mouse")
add_purchase("Bob", "Phone")
show_history("Alice")
show_history("Bob")
show_history("Charlie")
recommend_product("Alice")
recommend_product("Bob")
recommend_product("Charlie")
