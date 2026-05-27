# بايثون العرب - الدرس 21
# قيم كثيرة تعتبر False داخل if لكنها ليست نفس الشيء

values = [None, False, 0, "", []]

for value in values:
    print(repr(value), "bool:", bool(value), "type:", type(value))
