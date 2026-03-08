def calculate_total(price, quantity):
    if quantity < 0:
        raise ValueError("Quantity cannot be negative")
    return price * quantity


def apply_discount(total, discount):
    return total - (total * discount / 100)


if __name__ == "__main__":
    total = calculate_total(100, 2)
    final_price = apply_discount(total, 10)
    print("Final price:", final_price)
