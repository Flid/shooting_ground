import json

DATA_TYPE_YANDEX_TANK = 'yandex-tank'


def convert_from_yandex_tank(data):
    data = json.loads(data)

    response_times = data['data']['overall']['interval_real']['q']
    response_times_quantiles = [
        [str(item) + '%' for item in response_times['q']],
        [int(item / 1000) for item in response_times['value']],
    ]
    rps = data['stats']['metrics']['reqps']
    instances = data['stats']['metrics']['instances']

    return {
        'response_times_quantiles': response_times_quantiles,
        'instances': instances,
        'rps': rps,
    }


CONVERTERS = {
    DATA_TYPE_YANDEX_TANK: convert_from_yandex_tank,
}
