import datetime

class DataDay:
    @staticmethod
    def get_today():
        return datetime.date.today()

    @staticmethod
    def get_tomorrow():
        return DataDay.get_today() + datetime.timedelta(days=1)

    @staticmethod
    def get_delivery_day_today():
        return DataDay.get_today().strftime('%d')

    @staticmethod
    def get_delivery_day_tomorrow():
        return DataDay.get_tomorrow().strftime('%d')