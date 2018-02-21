#!/usr/bin/env python
# -*- coding: utf-8 -*-

def run():
    from flask_platform import app
    app.run(host='0.0.0.0',port=5000)


if __name__ == "__main__":
    run()
