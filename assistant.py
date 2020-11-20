#!/usr/bin/env python

from time import sleep
from datetime import datetime
import click
from bbc_feeds import news as n


@click.group()
def assistant():
    ''

@assistant.command()
def news():
    body = ''
    loop = 1
    for article in n().world(limit=5):
        body = body + str(loop) + '. ' + article['title'] + '. '
        loop = loop + 1
    click.echo(body)

@assistant.command()
@click.argument('C', type=click.FLOAT)
def CtoF(c):
    F = (c * 9/5) + 32
    F = (c * (9/5)) + 32
    F = round(F)
    click.echo(F)

@assistant.command()
def check_time():
    click.echo(datetime.now().strftime('%H'))

assistant().run()