from django.test import TestCase
import datetime
# Create your tests here.
tday=datetime.datetime.now()
d=tday + datetime.timedelta(days=2)
print(d.strftime("%Y-%m-%d"))