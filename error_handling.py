error_codes = {
    ## -- todo
    '01x001': 'Invalid version.',
    '01x002': 'User not found.',
    '01x003': 'Error validating user_id.',
    '01x004': 'Invalid Request: user_id must be a valid UUID.',
    '01x005': 'Invalid Request: user_id is required.',
    '01x006': 'Error retrieving task list.',
    '01x007': 'Error validating task_ids.',
    '01x008': 'Invalid task id. Task_ids must contain valid integer values.',
    ## -- weather
    # common
    '02x001': 'Invalid version.',
    '02x002': 'User not found.',
    '02x003': 'Error validating user_id.',
    '02x004': 'Invalid Request: user_id must be a valid UUID.',
    '02x005': 'Invalid Request: user_id is required.',
    # weather specific
    '02x006': 'Invalid Request: location must be in the format <latitude>,<longitude>.',
    '02x007': 'Invalid Request: location is required and cannot be empty.',
    '02x008': 'Invalid Request: location cannot contain more than one latitude, longitude pair.',
    '02x009': 'Invalid Request: non-numeric {arg} provided',
    '02x010': 'Invalid Request: Latitude must be between -90 and 90.',
    '02x011': 'Invalid Request: Longitude must be between -360 and 360.',
    '02x012': 'Error validating location.',
    '02x013': 'Error retrieving weather data.',
    '02x014': 'Invalid Request: unitcode must be one of the following: si-std, us-std.',
    '02x015': 'Invalid Request: metar must be a valid station id.',
    '02x016': 'Invalid Request: map_click.' # TODO expand upon this error.
}


def get_error(error_key, **kwargs):
    '''
        Helper function that returns error codes in a common format.
    '''
    return {error_key: error_codes.get(error_key, '').format(**kwargs)}
