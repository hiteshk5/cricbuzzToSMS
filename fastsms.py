#Importing Keys and other important stuff
from keys import API_KEY, numbers, url
from scrapper import message
my_data = {
"route" : "v3",
"sender_id" : "TXTIND", 
"message" : "This is a test message'",
"language" : "english",
"flash" : 0,
"numbers" : numbers,

}

headers = {
"authorization":API_KEY,
"Content-Type":"application/json"
}
