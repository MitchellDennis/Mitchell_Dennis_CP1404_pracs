
from prac_06.guitar import Guitar

gibson = Guitar("Gibson L - 5 CES", 1922, 16035.40)

tanglewood = Guitar("Tanglewood", 2013, 4888.88)

print("Gibson get_age() - Expect 98. Got {}".format(gibson.get_age()))
print("Gibson is_vintage() - Expect true. Got {}".format(gibson.is_vintage()))

print("Tanglewood get_age() - Expect 7. Got {}".format(tanglewood.get_age()))
print("Gibson is_vintage() - Expect false. Got {}".format(tanglewood.is_vintage()))
