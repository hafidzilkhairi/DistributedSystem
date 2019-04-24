#!/usr/bin/env python3

import threading
import hashlib

fileDaftarPassword = 'wordlist.txt'
apakahKetemu = False
password = ''
berhasil = ''

def create_threads(passwords):
    #bagi password dataset ke 4 thread
    password_list_split_points = [
        #biar integer
        (0, len(passwords) // 4),
        (len(passwords) // 4 + 1, len(passwords) // 2),
        (len(passwords) // 2 + 1, 3 * (len(passwords) // 4)),
        (3 * (len(passwords) // 4) + 1, len(passwords) - 1),
    ]
    #ngisi password ke thread
    thread_list = [threading.Thread(
        target=run_cracker,
        args=(
            passwords[split_point[0]: split_point[1]]
                    )
    ) for split_point in password_list_split_points]
    return thread_list


def run_cracker(*passwords):
    global apakahKetemu
    for password in passwords:
        if apakahKetemu:
            break
        # Passwords still contain last \n char which has to be stripped.
        if tebakPassword(password.rstrip()):
            # This is set to True only once. No need for sync mechanisms.
            apakahKetemu = True


def tebakPassword(passwords):
    # print('[*] Trying password: "{}" ...'.format(passwords))
    global password
    global berhasil
    tebakan = hashlib.md5(passwords.encode('utf-8')).hexdigest()
    if password == tebakan:
        berhasil = passwords
        return True
    else:
        return False


if __name__ == '__main__':
    with open(fileDaftarPassword) as password_file:
        passwords = password_file.readlines()
    password = str(input('Masukkan hash password: '))
    thread_list = create_threads(passwords)

    for thread in thread_list:
        print('[*] Running thread: {}.'.format(thread.getName()))
        thread.start()

    for thread in thread_list:
        print('[*] Wating for {} to join.'.format(thread.getName()))
        thread.join()
    print('Password: ',berhasil)
