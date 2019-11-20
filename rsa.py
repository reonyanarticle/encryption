from math import gcd


# 最小公倍数の関数
def lcm(p, q):
    return (p * q) // gcd(p, q)


# 秘密鍵と公開鍵の作成関数
def generate_keys(prime1, prime2):
    composites_num = prime1 * prime2
    lcm_num = lcm(prime1 - 1, prime2 - 1)

    for i in range(2, lcm_num):
        if gcd(i, lcm_num) == 1:
            encrypt_num = i
            break

    for i in range(2, lcm_num):
        if (encrypt_num * i) % lcm_num == 1:
            decrypt_num = i
            break

    return (encrypt_num, composites_num), (decrypt_num, composites_num)


# 平文を暗号化させる関数
def encrypt(plain_text, public_key):

    encrypt_num, composites_num = public_key
    plain_integers = [ord(char) for char in plain_text]
    encrypted_integers = [pow(i, encrypt_num, composites_num)
                          for i in plain_integers]
    encrypted_text = ''.join(chr(i) for i in encrypted_integers)

    return encrypted_text


# 暗号文を復元化する関数
def decrypt(encrypted_text, private_key):

    decrypt_num, composites_num = private_key
    encrypted_integers = [ord(char) for char in encrypted_text]
    decrypted_intergers = [pow(i, D, N) for i in encrypted_integers]
    decrypted_text = ''.join(chr(i) for i in decrypted_intergers)

    return decrypted_text


# Unicodeエラーを防ぐための関数
def sanitize(encrypted_text):
    return encrypted_text.encode('utf-8', 'replace').decode('utf-8')


if __name__ == '__main__':
    a, b = map(int, input("素数をふたつ用意してください: ").split())
    public_key, private_key = generate_keys(a, b)

    plain_text = input("暗号化したい文章を用意してください: ")
    encrypted_text = encrypt(plain_text, public_key)
    decrypted_text = decrypt(encrypted_text, private_key)

    print(f'''
    秘密鍵: {public_key}
    公開鍵: {private_key}

    平文:
    「{plain_text}」

    暗号文:
    「{sanitize(encrypted_text)}」

    平文 (復号化後):
    「{decrypted_text}」
    '''[1:-1])