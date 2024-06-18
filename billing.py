def calculate_bill(items):
    total = sum(item['price'] * item['quantity'] for item in items)
    gst = total * 0.05  
    discount = total * 0.10 
    final_total = total + gst - discount
    return total, gst, discount, final_total
def generate_bill_summary(supermarket_name, user_info, items, total, gst, discount, final_total):
    summary = f"--- {supermarket_name} Bill Summary ---\n"
    summary += f"Username: {user_info['username']}\n"
    summary += f"Phone Number: {user_info['phone_number']}\n"
    summary += f"Date: {user_info['date']}\n\n"
    summary += "Items Purchased:\n"
    for item in items:
        summary += f"{item['name']}: ${item['price']} x {item['quantity']}\n"
    summary += f"\nSubtotal: ${total}\n"
    summary += f"GST (5%): ${gst}\n"
    summary += f"Discount (10%): ${discount}\n"
    summary += f"Total: ${final_total}\n\n"
    summary += "Thank you for shopping with us!"
    return summary
