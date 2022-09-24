class Apple:
    @staticmethod
    def general_information():
        with open('Apple_wiki.txt', 'r') as gen_info:
            information = gen_info.read()
        return information

    @staticmethod
    def quantity_of_employees():
        return 80000

    @staticmethod
    def founders_company():
        return ['Steve Jobs', 'Steve Wozniak', 'Ronald Wayne']

    @staticmethod
    def revenue():
        return '365.82 billion $ USD on 2021 year'

    @staticmethod
    def first_company_product():
        return 'Apple I, it\'s first company product, demonstrated in April 1976 '

    @staticmethod
    def company_value():
        return 'Performance indicators As of October 31, 2021, the company\'s value was $2.41 trillion.' \
               ' As of December 8, 2021, the company\'s market value reached $2.86 trillion.'

    @staticmethod
    def number_of_stores():
        return 520

    @staticmethod
    def best_selled_product():
        return 'The best-selling product in the history of the company is not an iPhone, but an adapter' \
               ' cable from 3.5 mm to lighting'


if __name__ == '__main__':
    pass
