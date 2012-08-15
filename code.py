import web
render = web.template.render('templates/')

urls = (
    '/(.*)', 'index'
)

class index:
    def GET(self, n):
    	return render.index()

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()