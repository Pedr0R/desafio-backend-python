def flights():
    """
    List all flights.
    """
    for i in range(len(flights)):
        print(f"{i}: {flights[i]}")

flights = ['Flight 1', 'Flight 2', 'Flight 3']

while True:
  input('insert your command')
  if input == '/list':
    flights()