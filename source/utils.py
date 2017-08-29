def import_API_key(api_key_file):
    with open(api_key_file) as f:
        api_key_candidate = f.readline().strip()

    if len(api_key_candidate) > 1 and \
       len(api_key_candidate) < 64 and \
       ' ' not in api_key_candidate:
        return api_key_candidate

    else:
        raise ValueError('Invalid API key: {}'.format(api_key_file))        




