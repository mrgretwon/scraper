from sqlalchemy.orm import sessionmaker
from .models import Data, db_connect, create_data_table


class TeonitePipeline(object):

    def __init__(self):
        """
        Creating session
        and table in database
        """
        engine = db_connect()
        create_data_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """
        Save scraped data to database

        """
        session = self.Session()
        data = Data(**item)

        try:
            session.add(data)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
