import os


APIKey = "" # Get your LAPI Key from https://ivle.nus.edu.sg/LAPI/default.aspx, you need to log-in first

viewstate = """/wEPDwULLTEzODMyMDQxNjEPZBYCAgEPZBYEAgEPD2QWAh4Gb2
            5ibHVyBQ91c2VySWRUb1VwcGVyKClkAgkPD2QWBB4Lb25tb3VzZW9
            2ZXIFNWRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdsb2dpbmltZzEn
            KS5zcmM9b2ZmaW1nLnNyYzE7Hgpvbm1vdXNlb3V0BTRkb2N1bWVud
            C5nZXRFbGVtZW50QnlJZCgnbG9naW5pbWcxJykuc3JjPW9uaW1nLn
            NyYzE7ZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18
            WAQUJbG9naW5pbWcx"""

ivlelogin = "https://ivle.nus.edu.sg/api/login/?apikey="

hosturl = "https://ivle.nus.edu.sg/api/Lapi.svc/"

downloadurl = "https://ivle.nus.edu.sg/api/downloadfile.ashx"

filepath = "" # e.g: D:\NUS\SEM6

exclude = [""] #e.g "CS2103-CS2103T"

scriptdir = os.path.dirname(os.path.realpath(__file__))

credentialdir = os.path.join(scriptdir, "credentials")

authfile = os.path.join(credentialdir, "auth.json")
