import os

# Class representing an item
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    # Method to calculate total price of the item
    def total_price(self):
        return self.price * self.quantity

# Class representing a receipt
class Receipt:
    def __init__(self, tax_rate=0.05, discount_rate=0.1):
        self.items = []  # List to store the items
        self.tax_rate = tax_rate  # Tax rate
        self.discount_rate = discount_rate  # Discount rate
    
    # Method to add item to the receipt
    def add_item(self, name, price, quantity):
        item = Item(name, price, quantity)
        self.items.append(item)
    
    # Method to calculate subtotal
    def calculate_subtotal(self):
        return sum(item.total_price() for item in self.items)
    
    # Method to calculate tax based on the subtotal
    def calculate_tax(self):
        return self.calculate_subtotal() * self.tax_rate
    
    # Method to calculate discount based on the subtotal
    def calculate_discount(self):
        return self.calculate_subtotal() * self.discount_rate
    
    # Method to calculate the total amount after applying tax and discount
    def calculate_total(self):
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()
        discount = self.calculate_discount()
        return subtotal + tax - discount
    
    # Method to generate the formatted receipt
    def generate_receipt(self):
        receipt_lines = []
        receipt_lines.append("===== Receipt =====")
        for item in self.items:
            receipt_lines.append(f"{item.name} - {item.quantity} @ {item.price:.2f} each = {item.total_price():.2f}")
        receipt_lines.append(f"Subtotal: {self.calculate_subtotal():.2f}")
        receipt_lines.append(f"Tax ({self.tax_rate*100}%): {self.calculate_tax():.2f}")
        receipt_lines.append(f"Discount ({self.discount_rate*100}%): -{self.calculate_discount():.2f}")
        receipt_lines.append(f"Total: {self.calculate_total():.2f}")
        receipt_lines.append("===================")
        return "\n".join(receipt_lines)
    
    # Method to save the receipt as a text file
    def save_receipt(self, filename="receipt.txt"):
        with open(filename, 'w') as file:
            file.write(self.generate_receipt())
        print(f"Receipt saved to {filename}")
    
    # Optional bonus: Method to save the receipt as a PDF using fpdf (requires 'fpdf' package)
    def save_as_pdf(self, filename="receipt.pdf"):
        from fpdf import FPDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        receipt_content = self.generate_receipt().split('\n')
        for line in receipt_content:
            pdf.cell(200, 10, txt=line, ln=True)
        pdf.output(filename)
        print(f"Receipt saved to {filename}")

# Main function to handle user input and interactions
def main():
    receipt = Receipt()  # Creating an instance of the Receipt class
    
    # Input loop for adding items to the receipt
    while True:
        name = input("Enter the item name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
        price = float(input("Enter the price of the item: "))
        quantity = int(input(f"Enter the quantity of {name}: "))
        
        receipt.add_item(name, price, quantity)  # Adding item to the receipt
    
    # Display the receipt
    print("\n" + receipt.generate_receipt())
    
    # Ask if the user wants to save the receipt
    save_option = input("Would you like to save the receipt? (yes/no): ")
    if save_option.lower() == 'yes':
        file_type = input("Save as text file or PDF? (txt/pdf): ")
        if file_type.lower() == 'txt':
            filename = input("Enter filename (default: receipt.txt): ") or "receipt.txt"
            receipt.save_receipt(filename)
        elif file_type.lower() == 'pdf':
            filename = input("Enter filename (default: receipt.pdf): ") or "receipt.pdf"
            receipt.save_as_pdf(filename)

if __name__ == "__main__":
    main()
