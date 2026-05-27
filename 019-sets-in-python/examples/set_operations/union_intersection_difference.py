# بايثون العرب - الدرس 19
# union و intersection و difference في مثال واحد

frontend = {"HTML", "CSS", "JavaScript"}
backend = {"Python", "SQL", "JavaScript"}

print("All skills:", frontend.union(backend))
print("Common skills:", frontend.intersection(backend))
print("Only frontend:", frontend.difference(backend))
print("Only backend:", backend.difference(frontend))
