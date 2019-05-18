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
    key = input("鍵を入力してください : ")
    plaintext = decrypt(ciphertext, int(key))

    print("平文は : " + plaintext)
