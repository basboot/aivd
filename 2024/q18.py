import numpy as np
from PIL import Image

doorloper = """stroopwatermaestrospu
ugdiafragmakampalakap
paosslokresumerenrudy
panstationduplodonsdo
rmiegeuldafnelolahelp
toonoorlogqatluwnonqu
ebeceliacorsoadelelef
osnoeenmrkoiroeionodo
loplateaujuniorsoloqi
hfonzinznemmarisknouq
uinoajaretegoegscrabb
ledanlrdduplexsenseii
kamaggiirisisatcpbitn
rpurpusaalnnluxquocia
oalmelodjwozoscaroudi
octyrfteaarmegaperver
shusubtexasopeloldtem
pexoslomolwnwaceauraa
ugmalawiprooirupsiamn
nootourenergietestpad"""

import numpy as np

def string_to_numpy_array(input_string):
    # Split the input string into rows based on newlines
    rows = input_string.strip().split('\n')

    # Map each character to 1 or 0, and construct a list of rows
    char_map = lambda char: 1 if 'a' <= char <= 'm' else 0 if 'n' <= char <= 'z' else None
    mapped_rows = [[char_map(char) for char in row if char.isalpha()] for row in rows]

    # Convert to a 2D NumPy array
    return np.array(mapped_rows, dtype=int)


array = string_to_numpy_array(doorloper)
print(array)


print(array)

# Convert the array to a format suitable for an image
# Multiply by 255 to convert 0/1 to 0/255 for black and white
image_data = (array * 255).astype(np.uint8)

# Create a PIL image
image = Image.fromarray(image_data, mode='L')  # 'L' mode for grayscale

# Save or show the image
image.save("output_image.png")  # Save as PNG
image.show()  # Display the image



