import hashlib


class MarsURLEncoder:

    MASK = 'https://ma.rs/'

    def __init__(self):
        self.db = {}

    def encode(self, long_url: str):
        """Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol."""
        md5 = hashlib.md5()
        encoded_string = long_url.encode()
        md5.update(encoded_string)
        hash_md5 = md5.hexdigest()
        if hash_md5 in self.db:
            md5.update(encoded_string)
            hash_md5 = md5.hexdigest()
        self.db[f'{self.MASK}{hash_md5}'] = long_url
        return f'{self.MASK}{hash_md5}'

    def decode(self, short_url):
        """Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную."""
        return self.db[short_url]


if __name__ == '__main__':
    url_encoder = MarsURLEncoder()

    test_encode_1 = 'https://tsup.ru/mars/marsohod-1/01-09-2023/daily_job.html'
    test_encode_2 = 'https://tsup.ru/mars/asdasdasdasd-1/01-09-2023/daily_job.html'
    test_encode_1 = url_encoder.encode(test_encode_1)
    test_encode_2 = url_encoder.encode(test_encode_2)
    print(url_encoder.db)

    print(f'\nДостаем нужную строку из словаря db с ключом {test_encode_1} - {url_encoder.decode(test_encode_1)}')

    print(f'\n\nДостаем нужную строку из словаря db с ключом {test_encode_2} - {url_encoder.decode(test_encode_2)}')
