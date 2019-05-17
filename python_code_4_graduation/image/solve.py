#/usr/bin/python3
#coding:utf-8
from PIL import Image
import argparse
import monkeyhex
def image_opt(input):
    im = Image.open(input)
    pix = im.load()
    width,height = im.size#74*58
    text = ""
    flag = ""
    for y in range(height):
        for x in range(width):
            r, g, b = pix[(x,y)]
                # print(bin(key))
            text += str(r&1)
    # print(text)

    for i in range(0,len(text),8):
        temp = text[i:i+8]
        # print(temp)
        flag += chr(int(temp,2))
    flag = flag.rstrip('\x00')
    print(flag)
def main():
    parser = argparse.ArgumentParser(description="this script is used for LSB image making")
    parser.add_argument('input',help="select the source image")

    args = parser.parse_args()
    INPUT = args.input
    
    image_opt(INPUT)


if __name__ == "__main__":
    main()