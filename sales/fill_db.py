from salesapp.models import Product, ProductType, Bill, Order, Person

customer1 = Person.objects.create(first_name="John", last_name="Doe", newsletter_abo=True, email_address="john.doe@example.com", account=100.0)
customer2 = Person.objects.create(first_name="Jane", last_name="Smith", newsletter_abo=False, email_address="jane.smith@example.com", account=200.0)
customer3 = Person.objects.create(first_name="Alice", last_name="Johnson", newsletter_abo=True, email_address="alice.johnson@example.com", account=300.0)

product1 = Product.objects.create(name="Product A", price=10.0)
product2 = Product.objects.create(name="Product B", price=20.0)
product3 = Product.objects.create(name="Product C", price=30.0)

bill1 = Bill.objects.create(total_amount=50.0, is_paid=False)
bill2 = Bill.objects.create(total_amount=100.0, is_paid=True)
bill3 = Bill.objects.create(total_amount=150.0, is_paid=False)

order1 = Order.objects.create(customer=customer1, bill=bill1)
order2 = Order.objects.create(customer=customer2, bill=bill2)
order3 = Order.objects.create(customer=customer3, bill=bill3)

ProductType.objects.create(order=order1, product=product1, type_name="Wood")
ProductType.objects.create(order=order1, product=product2, type_name="Iron")

ProductType.objects.create(order=order2, product=product1, type_name="Wood")
ProductType.objects.create(order=order2, product=product3, type_name="Plastic")

ProductType.objects.create(order=order3, product=product1, type_name="Wood")
ProductType.objects.create(order=order3, product=product2, type_name="Iron")
ProductType.objects.create(order=order3, product=product3, type_name="Plastic")


# delete all


ProductType.objects.all().delete()
Order.objects.all().delete()
Bill.objects.all().delete()
Person.objects.all().delete()
Product.objects.all().delete()