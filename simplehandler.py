from xml.sax.handler import ContentHandler

class ArticleHandler(ContentHandler):
  """A handler to deal with articles in XML"""

  def startElement(self, name, attrs):
    print "Start element:",name

  def endElement(self, name):
    print "End element:",name

def main():
  import sys
  
  from xml.sax  import make_parser
  
  ch = ArticleHandler()
  saxparser = make_parser()
  
  saxparser.setContentHandler(ch)
  saxparser.parse(sys.argv[1])

if __name__ == '__main__':
  main()

# call as
# python simplehandler.py article.xml
