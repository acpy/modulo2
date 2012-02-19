# coding: utf-8

import web
import calendar
import time

urls = (
    '/(\d{4})', 'Ano',
    '/', 'Ano'
)
app = web.application(urls, globals())

class Ano(object):
    def GET(self, ano=None):
        if ano is not None:
            try:
                ano = int(ano)
            except ValueError: # ano invalido
                ano = None     # ignorar
        if ano is None:        # default:
            ano = time.localtime()[0]  # ano atual
        web.header('Content-Type', 'text/html; charset=utf-8')
        html = '<h1>Calendário Perpétuo</h1>'
        html += '<a href="/{0}">&lt;&lt;{0}</a>'.format(ano-1)
        html += ' | '
        html += '<a href="/{0}">{0}&gt;&gt;</a>'.format(ano+1)
        html += calendar.HTMLCalendar().formatyear(ano, 4)
        return html

if __name__ == '__main__':
    app.run()
