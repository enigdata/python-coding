from threading import Thread

# To construct a thread, we must extend the Thread class and implement the run method

class InputReader(Thread):
    def run(self):
        self.line_of_text = input() 

print("Enter some text and press enter: ")
thread = InputReader()
thread.start() # A thread only starts running in concurrent mode when we call the start method.

count = result = 1 
while thread.is_alive():
    result = count * count
    count += 1 

print("calculated squares up to {0}*{0} = {1}".format(count, result))
print('while you typed "{}"'.format(thread.line_of_text))

### on the join method
import time 
from urllib.request import urlopen
from xml.etree import ElementTree

CITIES = {
    "Charlottetown": ("PE", "s0000583"),
    "Edmonton": ("AB", "s0000045"),
    "Fredericton": ("NB", "s0000250"),
    "Halifax": ("NS", "s0000318"),
    "Iqaluit": ("NU", "s0000394"),
    "Québec City": ("QC", "s0000620"),
    "Regina": ("SK", "s0000788"),
    "St. John's": ("NL", "s0000280"),
    "Toronto": ("ON", "s0000458"),
    "Victoria": ("BC", "s0000775"),
    "Whitehorse": ("YT", "s0000825"),
    "Winnipeg": ("MB", "s0000193"),
    "Yellowknife": ("NT", "s0000366"),
}

class TempGetter(Thread):
    def __init__(self, city):
        super().__init__() #call super is necessary to ensure that the Thread is properly initialized
        self.city = city
        self.province, self.code = CITIES[self.city]

    def run(self):
        url = (
            "http://dd.weatheroffice.ec.gc.ca/citypage_weather/xml/"
            f"{self.province}/{self.code}_e.xml"
        )

        with urlopen(url) as stream:
            xml = ElementTree.parse(stream)
            self.temperature = xml.find("currentConditions/temperature").text

threads = [TempGetter(c) for c in CITIES]
start = time.time()
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

## Data we construct in one thread is accessible from other running threads. 
#  After the 10 threads have been started, we loop over them again, calling the join() method on each.
#  This method says wait for the thread to complete before doing anything. 
# We call this ten times in sequence; this for loop won't exit until all ten threads have completed.



    


