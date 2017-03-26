class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data )

    def output_html(self):
        fout = open('maya.html', 'w', encoding='utf-8')
        fout.write("<head><meta http-equiv='content-type' content='text/html;charset=utf-8'></head>")
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table border="1">')
        # <th width="5%">Url</th>
        fout.write('''<tr style="color:red" width="90%">
                    <th>Theme</th>
                    <th width="80%">Content</th>
                    </tr>''')
        for data in self.datas:
            fout.write('<tr>\n')
            # fout.write('\t<td>%s</td>' % data['url'])
            fout.write('\t<td align="center"><a href=\'%s\'>%s</td>' % (data['url'], data['title']))
            fout.write('\t<td>%s</td>\n' % data['summary'])
            fout.write('</tr>\n')
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        fout.close()
