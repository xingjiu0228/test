import urllib2

def run(**args):
    print "In downloadfile_url"
    url = "http://images.mofcom.gov.cn/tfs/201610/20161008202527339.docx"
    try:
        f = urllib2.urlopen(url) 
        data = f.read()
        fname = url.split("/")[-1]
        with open(fname, "wb") as code:     
            code.write(data)
    except Exception as err:
        print str(err)

run()
