import logging
import datetime
import webbrowser

x=datetime.datetime.now().strftime("%Y%m%d")
logging.basicConfig(filename="log_%s.txt"%x, level=logging.DEBUG, format="%(asctime)s %(message)s")
logging.debug("Debug logging test...")
logging.info("Program is working as expected")
logging.warning("Warning, the program may not function properly")
logging.error("The program encountered an error")
logging.critical("The program crashed")

GEN_HTML = "index.html"

f=open(GEN_HTML,'w')
message = """
<html>
    <head>
        <title>Loggin File on %s</title>
    </head>
    <body>
        <h1>DEBUG: Debug logging test...</h1>
        <h1>INFO: Program is working as expected</h1>
    </body>
</html>
"""%(x)

f.write(message)
f.close()

webbrowser.open(GEN_HTML,new=1)


