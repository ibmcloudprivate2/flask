#!/usr/bin/env python3

import connexion


def post_greeting(name: str) -> str:
    return 'Hello {name}'.format(name=name)

if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, port=5000, specification_dir='swagger/')
    app.add_api('converter-api.yaml', arguments={'title': 'Hello World Example'})
    app.run()