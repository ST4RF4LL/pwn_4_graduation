#/usr/bin/python3
#coding:utf-8
import base64
from PIL import Image
import argparse

def image_opt(input,output,flag):
    im = Image.open(input)
    pix = im.load()
    width,height = im.size#74*58
    new_img = Image.new("RGB",(width,height))
    new_pix = new_img.load()
    extracted_bits = []
    flag = list(flag)
    # print(flag)

    for y in range(height):
        for x in range(width):
            r, g, b = pix[(x,y)]
            # print("old",bin(r),bin(g),bin(b))
            try:
                key = int(flag[y*width+x])
                print(y*height+x)

                # print(bin(key))
                r = (r&0xFE)|key
                g = (g&0xFE)|key
                b = (b&0xFE)|key
                # print(key)
            except :
                r = r&0xFE
                g = g&0xFE
                b = b&0xFE
            # print("new",bin(r),bin(g),bin(b))
            new_pix[(x,y)] = (r,g,b)
    new_img.save(output)


def flag_opt(flag):
    flag = list(flag)
    new_flag = ""
    for i in flag:
        # print((bin(ord(i))[2:]).rjust(8,'0'))
        new_flag += bin(ord(i))[2:].rjust(8,'0')
    # print(new_flag)
    return new_flag

def main():
    parser = argparse.ArgumentParser(description="this script is used for LSB image making")
    parser.add_argument('-i','--input',help="select the source image")
    parser.add_argument('-o','--output',help="select the output image")
    parser.add_argument('-f','--flag',help="input the string you want to write into image")
    args = parser.parse_args()
    INPUT = args.input
    OUTPUT = args.output
    FLAG = args.flag
    FLAG = flag_opt(FLAG)
    image_opt(INPUT,OUTPUT,FLAG)


if __name__ == "__main__":
    main()