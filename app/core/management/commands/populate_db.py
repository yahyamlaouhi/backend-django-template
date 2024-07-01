# yourapp/management/commands/populate_db.py

import random
from django.db import IntegrityError
from django.conf import settings
from django.core.management.base import BaseCommand
from faker import Faker

from item.models import Item
from order.models import Order, OrderItem
from user.models import Buyer, Seller

ITEMS = [
    {
        "name": "Item 1",
        "description": "Description for Item 1",
        "price": 19.99,
        "is_available": True,
    },
    {
        "name": "Item 2",
        "description": "Description for Item 2",
        "price": 29.99,
        "is_available": True,
    },
    {
        "name": "Item 3",
        "description": "Description for Item 3",
        "price": 39.99,
        "is_available": True,
    },
    {
        "name": "Item 4",
        "description": "Description for Item 4",
        "price": 49.99,
        "is_available": True,
    },
    {
        "name": "Item 5",
        "description": "Description for Item 5",
        "price": 59.99,
        "is_available": True,
    },
    {
        "name": "Item 6",
        "description": "Description for Item 6",
        "price": 69.99,
        "is_available": True,
    },
    {
        "name": "Item 7",
        "description": "Description for Item 7",
        "price": 79.99,
        "is_available": True,
    },
    {
        "name": "Item 8",
        "description": "Description for Item 8",
        "price": 89.99,
        "is_available": True,
    },
]

fake = Faker("fr_FR")
PASSWORD = "mypassword"


class Command(BaseCommand):
    help = "Populate the database with initial data"

    def handle(self, *args, **kwargs):
        print("Populate DB")
        self.create_sellers(10)
        print("Seller Has Been Created")
        self.create_buyers(10)
        print("Buyer Has Been Created")
        self.create_items(3)
        print("Items Has Been Created")
        self.create_orders(5)
        print("Orders Has Been Created")

    def create_sellers(self, count):
        for i in range(count):
            email = f"seller{i}@gmail.com"
            try:
                seller = Seller.objects.create(
                    email=email,
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    phone_number=fake.phone_number(),
                    gender=random.choice(["Male", "Female"]),
                    address=fake.address(),
                )
                seller.set_password(PASSWORD)
                seller.save()
            except IntegrityError as e:
                print("Seller Already Exists")
                return

    def create_buyers(self, count):
        for i in range(count):
            email = f"buyer{i}@gmail.com"
            try:
                buyer = Buyer.objects.create(
                    email=email,
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    phone_number=fake.phone_number(),
                    gender=random.choice(["Male", "Female"]),
                    address=fake.address(),
                )
                buyer.set_password(PASSWORD)
                buyer.save()
            except IntegrityError as e:
                print("Buyer Already Exists")
                return

    def create_items(self, seller_num, items=ITEMS):
        sellers = Seller.objects.all()[:seller_num]
        for seller in sellers:
            for item in items:
                try:
                    item = Item.objects.create(
                        name=item["name"],
                        description=item["description"],
                        price=item["price"],
                        seller=seller,
                    )
                    item.save()
                except IntegrityError as e:
                    print("Item Already Exists")
                    return

    def create_orders(self, order_count):
        buyers = Buyer.objects.all()
        items = Item.objects.all()
        for _ in range(order_count):
            try:
                buyer = random.choice(buyers)
                seller = random.choice(Seller.objects.all())
                address = fake.address()
                total_paid = 0
                order = Order.objects.update_or_create(
                    buyer=buyer,
                    seller=seller,
                    address=address,
                    currency=settings.CURRENCY["TND"],
                    status=random.choice(Order.STATUS)[0],
                )
            except IntegrityError as e:
                print("Order Already Exists")
                return

            # Add items to order
            for _ in range(
                random.randint(1, 5)
            ):  # Each order will have between 1 to 5 items
                item = random.choice(items)
                quantity = random.randint(1, 10)
                OrderItem.objects.update_or_create(
                    order=order, item=item, quantity=quantity
                )
                total_paid += item.price * quantity

            order.total_paid = total_paid
            order.save()
