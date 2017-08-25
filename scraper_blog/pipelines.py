from sqlalchemy.orm import sessionmaker
from models import Dane, db_connect, create_dane_table


class TeonitePipeline(object):
    """Teonite pipeline for storing scraped items in the database"""

    def __init__(self):
        """
        Inicjalizacja polaczenia z baza i
        stworzenie tabeli dane
        """
        engine = db_connect()
        create_dane_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """
        Zapisuje zebrane itemy przez spidera w bazie.

        This method is called for every item pipeline component.

        """
        session = self.Session()
        dane = Dane(**item)

        try:
            session.add(dane)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
