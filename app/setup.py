import json
import logging
import sys
from ast import literal_eval
from datetime import datetime

from database import base
from database.model import ModelMatches

# Load logging configuration
log = logging.getLogger(__name__)
logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


if __name__ == '__main__':
    log.info('Create database {}'.format(base.db_name))
    base.Base.metadata.create_all(base.engine)

    log.info('Insert match data in database')
    with open('database/data/match.json', 'r') as file:
        data = json.load(file)
        for record in data:
            record['match_date'] = datetime.strptime(
                record['match_date'], '%Y-%m-%d')
            match = ModelMatches(**record)
            base.db_session.add(match)
        base.db_session.commit()
