DATA_TYPES = ['HUM', 'TEMP', 'LIGHT', 'PRESS', 'PREC']

AGGREGATES = ['HUM_MIN',
              'HUM_MAX',
              'HUM_MEAN',
              'HUM_MEDIAN',

              'TEMP_MIN',
              'TEMP_MAX',
              'TEMP_MEAN',
              'TEMP_MEDIAN',

              'LIGHT_MIN',
              'LIGHT_MAX',
              'LIGHT_MEAN',
              'LIGHT_MEDIAN',

              'PRESS_MIN',
              'PRESS_MAX',
              'PRESS_MEAN',
              'PRESS_MEDIAN',

              'PREC_MIN',
              'PREC_MAX',
              'PREC_MEAN',
              'PREC_MEDIAN']

START_DATE = '2022-01-01'

# START_DATE + DAY_SHIFT = END_DATE
DAY_SHIFT = 1

# REFRESH INTERVAL BETWEEN DATA POINTS, E.G. "2022-01-01 12:00:00", "2022-01-01 12:03:00"
REFRESH_INTERVAL = '3min'

# send_data() will be triggered when "]" pressed
KEYBOARD_PRESS = "]"
