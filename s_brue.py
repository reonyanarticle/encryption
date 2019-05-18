#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def decrypt(str, key):
    plaintext = ""

    for ch in list(str):
        if 'A' <= ch <= 'Z':
            plaintext += chr((ord(ch) - ord('A') + key) % 26 + ord('A')).lower()
        else:
            plaintext += ch

    return plaintext

if __name__ == '__main__':
    ciphertext = input("暗号文を入力してください: ")

    for i in range(1, 26):
        print('{0:2d}'.format(i) + " : " + decrypt(ciphertext, i))

