from abc import ABC, abstractmethod


class Medicine(ABC):
    def __init__(self, name: str, quantity: int, price: float) -> None:
        if not isinstance(name, str):
            raise TypeError("name must be str")
        if not isinstance(quantity, int) or isinstance(quantity, bool):
            raise TypeError("quantity must be int")
        if not isinstance(price, (int, float)) or isinstance(price, bool):
            raise TypeError("price must be float")

        self.name = name
        self.quantity = quantity
        self.price = float(price)

    @abstractmethod
    def requires_prescription(self) -> bool:
        ...

    @abstractmethod
    def storage_requirements(self) -> str:
        ...

    def total_price(self) -> float:
        return self.quantity * self.price

    @abstractmethod
    def info(self) -> str:
        ...


class Antibiotic(Medicine):
    def requires_prescription(self) -> bool:
        return True

    def storage_requirements(self) -> str:
        return "8–15°C, темне місце"

    def info(self) -> str:
        rx = "Так" if self.requires_prescription() else "Ні"
        return (
            f"Антибіотик: {self.name} | Кількість: {self.quantity} | "
            f"Ціна за од.: {self.price:.2f} | Разом: {self.total_price():.2f} | "
            f"Рецепт: {rx} | Зберігання: {self.storage_requirements()}"
        )


class Vitamin(Medicine):
    def requires_prescription(self) -> bool:
        return False

    def storage_requirements(self) -> str:
        return "15–25°C, сухо"

    def info(self) -> str:
        rx = "Так" if self.requires_prescription() else "Ні"
        return (
            f"Вітамін: {self.name} | Кількість: {self.quantity} | "
            f"Ціна за од.: {self.price:.2f} | Разом: {self.total_price():.2f} | "
            f"Рецепт: {rx} | Зберігання: {self.storage_requirements()}"
        )


class Vaccine(Medicine):
    def requires_prescription(self) -> bool:
        return True

    def storage_requirements(self) -> str:
        return "2–8°C, холодильник"

    def total_price(self) -> float:
        return super().total_price() * 1.10

    def info(self) -> str:
        rx = "Так" if self.requires_prescription() else "Ні"
        return (
            f"Вакцина: {self.name} | Кількість: {self.quantity} | "
            f"Ціна за од.: {self.price:.2f} | Разом (+10%): {self.total_price():.2f} | "
            f"Рецепт: {rx} | Зберігання: {self.storage_requirements()}"
        )