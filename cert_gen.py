import os
from OpenSSL import crypto


def create_self_signed_cert() -> None:
    """
    Creates two files - selfsigned certificate and private key for my program to secure connection
    in relative folder 'cert'
    """
    k = crypto.PKey()
    k.generate_key(crypto.TYPE_RSA, 4196)  # размер может быть 2048, 4196

    #  Создание сертификата
    cert = crypto.X509()
    # cert.get_subject().C = "US"  # указываем свои данные
    # cert.get_subject().ST = "New-York"  # указываем свои данные
    # cert.get_subject().L = "New-York"  # указываем свои данные
    # cert.get_subject().O = "SimpleFileTransfer"  # указываем свои данные
    cert.get_subject().OU = "SimpleFileTransfer"  # указываем свои данные
    cert.get_subject().CN = "SimpleFileTransfer.local"  # указываем свои данные
    cert.set_serial_number(1000)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(10 * 365 * 24 * 60 * 60)  # срок "жизни" сертификата
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(k)
    cert.sign(k, 'sha1')

    if not os.path.isdir('cert'):
        os.mkdir('cert')

    with open(f'cert/cert.crt', "wb") as f:
        f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))

    with open(f'cert/cert_private_key.key', "wb") as f:
        f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, k))
