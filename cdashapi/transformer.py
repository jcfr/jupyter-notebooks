import collections
from datetime import timedelta
import re

class Transformer(object):

    def __init__(self, data):
        self._data = data
        self._transformed_data = collections.OrderedDict()
        self._debug = False

    @staticmethod
    def _collect_step_values(data, step_name, key, update=lambda value: value):
        values = []
        for submission in data:
            if step_name in submission and key in submission[step_name]:
                values.append(update(submission[step_name][key]))
            else:
                values.append(update(None))
        return values

    _DURATION_REGEX = re.compile(r'((?P<hours>\d+?)h )?((?P<minutes>\d+?)m )?((?P<seconds>\d+?)s)?')

    @staticmethod
    def parse_duration(time_str):
        """Adapted from http://stackoverflow.com/questions/4628122/how-to-construct-a-timedelta-object-from-a-simple-string
        """
        parts = Transformer._DURATION_REGEX.match(time_str)
        if not parts:
            return
        parts = parts.groupdict()
        time_params = {}
        for (name, param) in parts.items():
            if param:
                time_params[name] = int(param)
        return timedelta(**time_params)

    def data(self):
        return self._data

    def __call__(self, orient='columns'):
        return self.transformed_data(orient)

    def transformed_data(self, orient='columns'):
        orients = ['columns', 'records']
        if orient not in orients:
            raise Exception("'orient' parameter set to invalid value '%s'."
                            "Acceptable values are %s." % (orient, ", ".join(orients)))
        if orient == 'records':
            for values in zip(*(self._filtered_df.values())):
                record = {}
                for (idx, column) in enumerate(a.keys()): record.update({column: str(values[idx])})
                records.append(record)
            return records
        else:
            return self._transformed_data

    def __repr__(self):
        return self.stats().__repr__() if len(self.stats()) > 0 else self.data().__repr__()

    def sites(self, update=lambda text:text):
        self._transformed_data['sites'] = [update(submission['site']) for submission in self.data()]
        return self

    def labels(self, update=lambda text:text):
        self._transformed_data['labels'] = [update(submission['label']) for submission in self.data()]
        return self

    def names(self, update=lambda text:text):
        self._transformed_data['names'] = [update(submission['buildname']) for submission in self.data()]
        return self

    def start_times(self, update=lambda value:value):
        self._transformed_data['start_times'] = [update(submission['builddatefull']) for submission in self.data()]
        return self

    _update_timedelta = lambda value: Transformer.parse_duration(value) if value else timedelta()

    def configure_times(self, update=lambda value:value):
        self._transformed_data['configure_times'] = update(
            Transformer._collect_step_values(self.data(), 'configure', 'time', Transformer._update_timedelta))
        return self

    def build_times(self, update=lambda value:value):
        self._transformed_data['build_times'] = update(
            Transformer._collect_step_values(self.data(), 'compilation', 'time', Transformer._update_timedelta))
        return self

    def test_times(self, update=lambda value:value):
        self._transformed_data['test_times'] = update(
            Transformer._collect_step_values(self.data(), 'test', 'time', Transformer._update_timedelta))
        return self

    def configure_warnings(self, update=lambda value:value):
        self._transformed_data['configure_warnings'] = update(
            Transformer._collect_step_values(self.data(), 'configure', 'warning', lambda value: value if value else 0))
        return self

    def configure_errors(self, update=lambda value:value):
        self._transformed_data['configure_errors'] = update(
            Transformer._collect_step_values(self.data(), 'configure', 'error', lambda value: value if value else 0))
        return self

    def build_warnings(self, update=lambda value:value):
        self._transformed_data['build_warnings'] = update(
            Transformer._collect_step_values(self.data(), 'compilation', 'warning', lambda value: value if value else 0))
        return self

    def build_errors(self, update=lambda value:value):
        self._transformed_data['build_errors'] = update(
            Transformer._collect_step_values(self.data(), 'compilation', 'error', lambda value: value if value else 0))
        return self

