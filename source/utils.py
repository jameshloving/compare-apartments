def import_API_key(api_key_file):
    """
    !@brief Import a Google Maps API key from a file

    This function accepts the name of a file containing a Google Maps API key. If
    that file contains a valid key, this function will return that key. Otherwise,
    this function raises a ValueError.

    @param api_key_file String-formatted name of file containing Google Maps API key
    @return String-formatted Google Maps API key
    """

    with open(api_key_file) as f:
        api_key_candidate = f.readline().strip()

    if len(api_key_candidate) > 1 and \
       len(api_key_candidate) < 64 and \
       ' ' not in api_key_candidate:
        return api_key_candidate

    else:
        raise ValueError('Invalid API key: {}'.format(api_key_file))        



def str_time_to_int_minutes(str_time):
    """
    !@brief Get the integer number of minutes from a string-formatted time

    This function accepts a string-formatted time, e.g., "1 hour 14 minutes", and
    returns the number of minutes in that time, e.g., 74.

    @warning No value checking is performed.

    @param str_time String-formatted time of the format "x hours x minutes"
    @return Integer number of minutes in time
    """

    if "hour" not in string:
        return int(str_time.split()[0])

    else:
        return int(str_time.split()[0])*60 + int(str_time.split()[2])
