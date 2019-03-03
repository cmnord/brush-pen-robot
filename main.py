# font = {
#     'A': {'path': [(0, 0, 0), ], 'width': 20, 'height': 50},
#     ...
# }

def main(text, out_file):
    with open(out_file) as f:
        base_x = 0
        base_y = 0
        for c in text:
            path = font[c]['path']
            width = font[c]['width']
            height = font[c]['height']

            for x, y, thickness in path:
                f.write("G1 X%f Y%f Z%f;\n" % base_x + x, base_y + y, thickness)

            base_x += width

if __name__ == "__main__":
    main()