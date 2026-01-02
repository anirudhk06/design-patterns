from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    @abstractmethod
    def accept(self, visitor):
        raise NotImplementedError("Sub classes must be implement accept() method.")


class FoodItem(Item):
    def accept(self, visitor: "ItemVisitor"):
        visitor.visit_food_item(self)


class ElectronicsItem(Item):
    def accept(self, visitor: "ItemVisitor"):
        visitor.visit_electronics_item(self)


class MedicineItem(Item):
    def accept(self, visitor: "ItemVisitor"):
        visitor.visit_medicine_item(self)


class ItemVisitor(ABC):
    @abstractmethod
    def visit_food_item(self, item: Item):
        raise NotImplementedError(
            "Sub classes must be implement visit_food_item() method."
        )

    @abstractmethod
    def visit_electronics_item(self, item: Item):
        raise NotImplementedError(
            "Sub classes must be implement visit_electronics_item() method."
        )

    @abstractmethod
    def visit_medicine_item(self, item: Item):
        raise NotImplementedError(
            "Sub classes must be implement visit_medicine_item() method."
        )


class TaxVisitor(ItemVisitor):
    def __init__(self):
        self.total_tax = 0.0

    def visit_food_item(self, item: Item):
        self.total_tax += item.price * 0.5

    def visit_electronics_item(self, item: Item):
        self.total_tax += item.price * 0.18

    def visit_medicine_item(self, item: Item):
        pass


class InvoiceVisitor(ItemVisitor):
    def __init__(self):
        self.lines = []

    def visit_food_item(self, item: Item):
        self.lines.append(f"FoodItem: {item.name} - ₹{item.price}")

    def visit_electronics_item(self, item: Item):
        self.lines.append(f"ElectronicsItem: {item.name} - ₹{item.price}")

    def visit_medicine_item(self, item: Item):
        self.lines.append(f"MedicineItem: {item.name} - ₹{item.price}")

    def get_invoice(self) -> str:
        return "\n".join(self.lines)


def main() -> None:
    items: list[Item] = [
        FoodItem("Bread", 100),
        ElectronicsItem("Phone", 50000),
        MedicineItem("Paracetamol", 50),
    ]

    tax_visitor = TaxVisitor()
    invoice_visitor = InvoiceVisitor()

    for item in items:
        item.accept(tax_visitor)
        item.accept(invoice_visitor)

    print("Total Tax:", f"${tax_visitor.total_tax}")
    print(invoice_visitor.get_invoice())


if __name__ == "__main__":
    main()
