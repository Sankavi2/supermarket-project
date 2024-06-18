from user import get_user_info
from items import get_items
from billing import calculate_bill, generate_bill_summary
from mail import send_email
def main():
    supermarket_name = "*****kavi Supermarket*****"
    print(f"Welcome to {supermarket_name}")
    user_info = get_user_info()
    items = get_items()
    total, gst, discount, final_total = calculate_bill(items)
    print(f"\n--- {supermarket_name}")
    print( "--Bill Summary--")
    print(f"Username: {user_info['username']}")
    print(f"Phone Number: {user_info['phone_number']}")
    print(f"Date: {user_info['date']}")
    print("\nItems Purchased:")
    for item in items:
        print(f"{item['name']}: ${item['price']} x {item['quantity']}")
    print(f"\nSubtotal: ${total}")
    print(f"GST (5%): ${gst}")
    print(f"Discount (10%): ${discount}")
    print(f"Total: ${final_total}")
    print("\nThank you for shopping with us!")
    email = input("\nEnter your email address to receive the bill: ")
    bill_summary = generate_bill_summary(supermarket_name, user_info, items, total, gst, discount, final_total)
    send_email(email, f"{supermarket_name} Bill", bill_summary)
if __name__ == "__main__":
    main()
