from datadog import initialize, api

options = {
    'api_key': '<YOUR_API_KEY>',
    'app_key': '<YOUR_APP_KEY>'
}

initialize(**options)
board_id = 2551
board_title = "My Screenboard"
description = "An informative screenboard."
width = 1024
widgets = [{
    "type": "image",
    "height": 20,
    "width": 32,
    "y": 7,
    "x": 32,
    "url": "https://path/to/image.jpg"
}]
template_variables = [{
    "name": "host1",
    "prefix": "host",
    "default": "host:my-host"
}]

api.Screenboard.update(board_id,
                       board_title=board_title,
                       description=description,
                       widgets=widgets,
                       template_variables=template_variables,
                       width=width)
