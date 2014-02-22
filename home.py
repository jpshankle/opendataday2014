import cherrypy
class CorruptionData(object):
    def index(self):
        return "Corruption Data"
    index.exposed = True

cherrypy.quickstart(CorruptionData())
