import arrow

from st2common.util import isotime
from st2common.runners.base_action import Action


class GetWeekBoundariesTimestampsAction(Action):
    def run(self, date=None):
        if date:
            dt = isotime.parse(date)
            dt = arrow.get(dt)
        else:
            # No date provided, use current date
            dt = arrow.utcnow()

        start_timestamp = dt.floor('week').timestamp
        end_timestamp = dt.ceil('week').timestamp

        return (True, (start_timestamp, end_timestamp))
