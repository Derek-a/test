class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fount = open('output.html','w',encoding='utf-8')

        # <head><meta charset="utf-8"></head>
        fount.write("<meta charset=\'utf-8\'>")

        fount.write("<html>")
        fount.write("<body>")
        fount.write("<table>")


        for data in self.datas:
            fount.write("<tr>")
            fount.write("<td>%s</td>"% data['url'])
            fount.write("<td>%s</td>" % data['title'])
            fount.write("<td>%s</td>" % data['summary'])
            fount.write("</tr>")

        fount.write("</table>")
        fount.write("</body>")
        fount.write("</html>")

        fount.close()