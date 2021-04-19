library(jsonlite)
library(httr)
library(xmlparsedata)
library(xml2)

#prompt for username and password.  Should put in dialog box instead
Username = readline(prompt=,"Username: ");
Password = readline(prompt=,"Password: ");

Endpoint = "https://api-ciq.marketintelligence.spglobal.com/gdsapi/rest/v3/clientservice.json"

TestBody = '{"inputRequests":[{"Function":"GDSP","Mnemonic":"IQ_TOTAL_REV","Identifier":"MSFT:"},{"function":"GDSHE","identifier":"IBM:NYSE","mnemonic":"IQ_EBITDA","properties":{"PeriodType":"IQ_FY-4","restatementTypeId":"LC"}},
           {"function": "GDST","identifier":"IBM:NYSE","mnemonic":"IQ_MARKETCAP","properties":{"frequency":"Monthly","startDate":"01/01/2018"}}]}'

CIQAPI = POST(url = Endpoint,config = authenticate(Username,Password,type = 'any'),body = TestBody,verbose(),add_headers('content-type'= 'application/json'))

get2json = content(CIQAPI, as = "parsed")

#Try the query, if error print error
tryCatch({
    parse2json = (toJSON(get2json))},
    error = function(e) {
      str(e);
      print("HTML returned");
      htmlerr <- xml2::as_list(get2json)
      print(unlist(htmlerr$html$head$title))
      print(unlist(htmlerr$html$body$p))
    })      
if (exists('parse2json')) {print(parse2json)}

      
      