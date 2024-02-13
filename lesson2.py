METERS_PER_YARD = 0.9144
METERS_PER_MILE = 1609.34
METERS_PER_INCH = 0.0254


meter = float(input("Enter how much meters: "))

choice = input("Choose unit of measurement('miles', 'inches', 'yards'): ")
# miles
if choice == 'miles':
    miles = meter / 1609.34
    print(miles)
elif choice == 'inches':
    inches = meter / 0.0254
    print(inches)
elif choice == 'yards':
    yards = meter / 0.9144
    print (yards)
