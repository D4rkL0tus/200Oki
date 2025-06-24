"""
===============================================================
    COPYRIGHT OF INFORMATION SYSTEMS SERVICES 2025
    
    MIT LICENSE 

    IF YOU USE THIS SOFWTARE YOU ARE HEREBY 
    THE ONE RESPOSONSIBLE FOR ANYTHING AND EVERYTHING
    THAT HAPPENS WHILST USING THIS SOFTWARE.
    INFORMATION SYSTEMS SERVICES OR NON OTHER THAN YOU
    ARE THE ONE RESPONSIBLE FOR ANY ISSUES THAT ARRISE
    SUCH AS BUT NOT LIMITED TO DAMAGES, LAWSUITS, ETC.

===============================================================
"""

import requests
import threading
import time
import argparse

# class for defining the commands used within the application
class CommandProcessors:
    def __init__(self, DomainFile, DomainContents):
        self.DomainFile = ""
        self.DomainContents = None

    def OpenFile(self):
        with open(self.DomainFile, "r") as file:
            self.DomainContents = [line.strip() for line in file if line.strip()]
            for line in self.DomainContents:
                pass

    def RequestMaker(self, domain, OutputFile):
        results = []
        

        for domain in self.DomainContents:
            URL = f"https://{domain}"
            try:
                time.sleep(8)
                GET_R = requests.get(URL)
                if GET_R.status_code == 200:
                    result = (f"{domain} RX STATUS 200")
                else:
                    result = (f"{domain} RX STATUS {GET_R.status_code}")
            except requests.RequestException as e:
                result = (f"RX FAILED FOR DOMAIN {domain}", {e})
            
            print(result)
            results.append(result)

        with open(OutputFile, "w") as file:
            for line in results:
                file.write(line + "\n")
            



def main():
    # init of the parser
    ARG_PARSER = argparse.ArgumentParser(description="ARGS FOR PROGRAM")

    # Adding Arguments
    ARG_PARSER.add_argument("--document", help="Specifiy the file that contains the subdomains to be scanned for web content", required=True)    
    ARG_PARSER.add_argument("--check", help="Check the Domain status", action="store_true")
    ARG_PARSER.add_argument("--output", help="Location to store outputfile at")
    # Parse the args
    ARGS = ARG_PARSER.parse_args()

    if ARGS.document:
        # init of filename
        CP = CommandProcessors(ARGS.document, None)
        CP.DomainFile = ARGS.document
        CP.OpenFile()
         
    if ARGS.check and ARGS.output:
        CP.RequestMaker(ARGS.document, ARGS.output)
if __name__ == '__main__':
    main()  