import sys

class BFP:
    def __init__(self, file_):
        self.site = filter(None, open(file_, 'rb').read().split("\n")) #Hack to get rid of blank lines

    def main(self):
        to_exe = ""
        nest = 0
        for x in self.site:
            indent = False
            unindent = False
        
            if "{" in x:
                x = x.replace("{", ":")
                indent = True
            elif "}" in x:
                nest -= 1
                x = x.replace("}", "")
                unindent = True
            
            to_exe += (" "*nest)+x+"\n"
            if unindent:
                if nest != 0:
                    nest -= 1 #This is here so that the conditional statement itself doesn't get indented.
            
            elif indent:
                nest += 1
     
        exec(to_exe)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage: python "+sys.argv[0]+" <file.bfp>"
    else:
        BFP(sys.argv[1]).main()

