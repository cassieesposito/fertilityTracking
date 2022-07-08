import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import sqlite3

PASSPHRASE = b"My Key"
DATABASE = ":memory:"


def main():
    salt = b"1234567890123456"
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(PASSPHRASE))
    fernet = Fernet(key)

    try:
        conn = connect(DATABASE)
        cur = conn.cursor()
    except sqlite3.Error as e:
        print(e)

    try:
        # with open("sample.sql", "r") as f:
        #     q = f.read()
        with open("encryptedDump.sql", "rb") as f:
            sql = f.read()

        q = fernet.decrypt(sql).decode("utf-8").rstrip()

        cur.executescript(q)
        conn.commit()
        cur.execute("SELECT * from people;")
        for row in cur.fetchall():
            print(row)

        dump = ""

        for line in conn.iterdump():
            dump += line + "\n"

        print(dump)

        dump += " " * ((1024 * 1024) - len(dump))

        dump = dump.encode("utf-8")

        encrypted = fernet.encrypt(dump)
        with open("encryptedDump.sql", "wb") as f:
            f.write(encrypted)

        conn.close()
    except sqlite3.Error as e:
        print(e)

    return


def connect(database):
    try:
        conn = sqlite3.connect(database)
        return conn
    except sqlite3.Error as e:
        print(e)


if __name__ == "__main__":
    main()
