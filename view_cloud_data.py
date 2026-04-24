from database_logic import session, Product, Order

def check_my_cloud_storage():
    print("--- CONNECTING TO AIVEN CLOUD ---")
    
    # 1. Check Shoes (Inventory)
    print("\n[INVENTORY TABLE]")
    shoes = session.query(Product).all()
    for s in shoes:
        print(f"ID: {s.id} | Shoe: {s.name} | Price: ₱{s.price}")

    # 2. Check Orders (Transactions)
    print("\n[ORDERS TABLE]")
    orders = session.query(Order).all()
    if not orders:
        print("No orders saved yet!")
    for o in orders:
        print(f"Order #{o.id} | Product: {o.product_name} | Qty: {o.quantity} | Total: ₱{o.total_price}")

if __name__ == "__main__":
    check_my_cloud_storage()