# c

from PIL import Image, ImageOps

im = Image.open('q18raster.png')

pix = ImageOps.grayscale(im)

grid = []
values= []

for x in range(45):
    row = []
    for y in range(33):
        px = int(x * 47.7) + 30
        py = int(y * 47.7) + 10
        value = pix.getpixel((px, py))
        assert value == 53 or value == 103, "not a legal value"
        if value == 103:
            row.append(1)
            values.append(1)
        else:
            row.append(0)
            values.append(0)
        pix.putpixel((px, py), (255))

    grid.append(row)

print(grid)

print("rows", len(grid))
print("cols", len(grid[0]))
print("total", len(grid) * len(grid[0]))

# ---
for row in grid:
    print(row)


values_out_off_order = []

for i in range(len(values)):
    if i % 2 == values[i] % 2:
        # print(values[i])
        values_out_off_order.append(values[i])
print(values)
print(len(values_out_off_order))
print(values_out_off_order)

def bits_to_value(bits):
    result = 0
    for bit in bits:
        result = result << 1 # (1 if bit == 0 else 1)
        result = result | bit
    return result

for i in range(0, len(values), 8):
    print(bits_to_value(values[i:i + 8]), end=" - ")
    print(chr(bits_to_value(values[i:i + 8])))

pix.show()

print(im.size)
# print pix[x,y]  # Get the RGBA Value of the a pixel of an image