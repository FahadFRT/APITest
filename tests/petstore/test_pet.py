# import pytest
#
#
# @pytest.mark.run(order=1)
# def test_pet_post(test_conf_pet_post):
#     assert test_conf_pet_post.json()['message'] == "1"
#
#
#
# @pytest.mark.run(order=2)
# def test_pet_get(test_conf_pet_get):
#     assert test_conf_pet_get.json()['name'] == "pet001"


# import beautifulsoup4
# f = open('reports/testng-results.html')
# soup = BeautifulSoup4.BeautifulSoup(f)
# f.close()
# g = open('testng-results.xml', 'w')
# print(g, soup.prettify())
# g.close()

import lxml
from lxml import html, etree

doc = html.fromstring(open('/home/muhammad/PycharmProjects/APITesting/reports/testng-results.html').read())
out = open('/home/muhammad/PycharmProjects/APITesting/reports/testng-results.xml', 'wb')
out.write(etree.tostring(doc))