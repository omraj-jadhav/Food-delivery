from food_delivery import Customer, DeliveryPartner, MenuItem, Restaurant


# 1. Register customer Priya
print("========== 1. REGISTER CUSTOMER ==========")
priya = Customer("Priya", "9876543210", "Bangalore")
print("Customer registered successfully.")
priya.display_profile()


# 2. Register delivery partner Rajesh
print("\n========== 2. REGISTER DELIVERY PARTNER ==========")
rajesh = DeliveryPartner("Rajesh", "9876543211", "Bike")
print("Delivery partner registered successfully.")
rajesh.display_profile()


# 3. Create Bawarchi restaurant and add Biryani and Kebab
print("\n========== 3. CREATE RESTAURANT ==========")
bawarchi = Restaurant("Bawarchi", "MG Road")

biryani = MenuItem("Biryani", 250, False)
kebab = MenuItem("Kebab", 200, False)

bawarchi.add_item(biryani)
bawarchi.add_item(kebab)

print("Restaurant:", bawarchi._name)
print("Location:", bawarchi._location)
print("Menu:")

for item in bawarchi.get_menu():
    print("-", item.name, "₹" + str(item.price))


# 4. Top up Priya's wallet
print("\n========== 4. WALLET TOP-UP ==========")

print("Adding ₹500...")
priya.add_to_wallet(500)
print("Wallet balance:", priya._wallet_balance)

print("Attempting to add -₹100...")
try:
    priya.add_to_wallet(-100)
except ValueError as e:
    print("Top-up rejected:", e)

print("Final wallet balance:", priya._wallet_balance)


# 5. Priya places order for Biryani and Kebab
print("\n========== 5. PLACE ORDER ==========")

items = [biryani, kebab]
order = priya.place_order(bawarchi, items)

print("Order ID:", order._order_id)
print("Order Status:", order._status)


# 6. Print bill details and estimated delivery time
print("\n========== 6. BILL DETAILS ==========")

subtotal = sum(item.price for item in order._items)
gst = subtotal * 0.05
packaging_fee = 20
total = order.calculate_bill()
estimated_time = order.estimated_time()

print("Subtotal: ₹", subtotal)
print("GST (5%): ₹", gst)
print("Packaging Fee: ₹", packaging_fee)
print("Total: ₹", total)
print("Estimated Delivery Time:", estimated_time, "minutes")


# 7. Rajesh accepts the order, wrong OTP, then correct OTP
print("\n========== 7. DELIVERY ==========")

print("Rajesh accepting the order...")
rajesh.accept_order(order)
print("Order Status:", order._status)

print("\nTrying wrong OTP: 9999")
if not order.verify_otp(9999):
    print("Wrong OTP. Delivery not completed.")

print("\nDelivering with correct OTP: 1234")
if rajesh.deliver(order, 1234):
    print("Delivery completed successfully.")

print("Order Status:", order._status)


# 8. Notify Priya and Rajesh
print("\n========== 8. NOTIFICATIONS ==========")

priya.notify("Order delivered")
rajesh.notify("Order delivered")

print("\n========== DEMO COMPLETED ==========")
