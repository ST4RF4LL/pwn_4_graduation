# coding:utf-8
import re
mappings = {0x04: "a",  0x05: "b",  0x06: "c", 0x07: "d", 0x08: "e", 0x09: "f", 0x0A: "g",  0x0B: "h", 0x0C: "i",  0x0D: "j", 0x0E: "k", 0x0F: "l",
            0x10: "m", 0x11: "n", 0x12: "o",  0x13: "p", 0x14: "q", 0x15: "r", 0x16: "s", 0x17: "t", 0x18: "u", 0x19: "v", 0x1A: "w", 0x1B: "x", 0x1C: "y", 0x1D: "z",
            0x1E: "1", 0x1F: "2", 0x20: "3", 0x21: "4", 0x22: "5",  0x23: "6", 0x24: "7", 0x25: "8", 0x26: "9", 0x27: "0", 0x28: "\n", 0x2a: "\b",  0X2B: "\t",
            0x2C: " ",  0x2D: "-", 0x2E: "=", 0x2F: "[",  0x30: "]",  0x31: "\\", 0x32: "`", 0x33: ";",  0x34: "'", 0x36: ",",  0x37: "."}
shift_mappings = {0x04: "A",  0x05: "B",  0x06: "C", 0x07: "D", 0x08: "E", 0x09: "F", 0x0A: "G",  0x0B: "H", 0x0C: "I",  0x0D: "J", 0x0E: "K", 0x0F: "L",
                  0x10: "M", 0x11: "N", 0x12: "O",  0x13: "P", 0x14: "Q", 0x15: "R", 0x16: "S", 0x17: "T", 0x18: "U", 0x19: "V", 0x1A: "W", 0x1B: "X", 0x1C: "Y", 0x1D: "Z",
                  0x1E: "!", 0x1F: "@", 0x20: "#", 0x21: "$", 0x22: "%",  0x23: "^", 0x24: "&", 0x25: "*", 0x26: "(", 0x27: ")", 0x28: "\n", 0x2a: "\b",  0X2B: "\t",
                  0x2C: " ",  0x2D: "_", 0x2E: "+", 0x2F: "{",  0x30: "}",  0x31: "|", 0x32: "~", 0x33: ":",  0x34: "\"", 0x36: "<",  0x37: ">"}

with open('./blue.pcapng', 'rb') as file:
    text = file.read()
    result = []
    temp = 0
    done = 0
    while 1:
        temp = text.find(
            b"\x02\x00\x21\x0e\x00\x0a\x00\x42\x00\xa1\x01", temp+1)
        if temp == -1:
            break
        else:
            result.append(temp)
    flag = ""
    for i in result:
        shift_key = text[i+11]
        value_key = int(text[i+13])
        if value_key != 0 and text[i+14] == 0:
            try:
                if shift_key == 0x2:
                    flag += shift_mappings[value_key]
                elif shift_key == 0x00:
                    flag += mappings[value_key]
            except:
                break
    start = flag.find("flag")
    start = flag.find("flag",start+1)
    end = flag.find("}")
    flag = flag[start:end+1]
    print(flag)
