#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def encrypt(str, key):
    ciphertext = ""

    for ch in list(str):
        if 'a' <= ch <= 'z':
            ciphertext += chr((ord(ch) - ord('a') - key) % 26 + ord('a')).upper()
        else:
            ciphertext += ch

    return ciphertext

if __name__ == '__main__':
    plaintext = input("平文を入力してください : ")
    key = input("鍵を入力してください : ")
    ciphertext = encrypt(plaintext, int(key))

    print("暗号文は : " + ciphertext)

