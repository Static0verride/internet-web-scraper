import BlackWidow



domain = 'corp.brocade.com'
# html = {"http://connect.brocade.com/engcs/EN/documents/Release%20Documents/Forms/Docs.aspx"}
# html = {"https://my.brocade.com/wps/myportal/myb/home/search?query=Brocade+icx&category=resource-library"}
html = {"http://connect.brocade.com/portal/Education/toi/laferrari/SitePages/Home.aspx"}
# html = {"http://cmweb/"}
# html = {"https://flightdeck.brocade.com/"}
# html = {"https://swdocs/sre_released_docs/ironware/FastIron/"}
# html = {"http://connect.brocade.com/engcs/EN/documents/Release%20Documents/FI%2007.3.x%20(Corvo)/Corvo_FI73x_FuncSpec_V01.pdf"}
# htmlt = {"http://connect.brocade.com/cs/hr/HROperations/HR365/HR%20365%20Documents/PUBLISHED/LEARNING%20AND%20DEVELOPMENT/Learning%20-%20Brocade%20Essentials/Brocade%20Essentials%20-%20Overview.pdf"}
my_header = {'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'}
username = 'jmendez'
password = 'qwertzxc1'
domain = 'corp.brocade.com'

link = html.pop()
my_spider = BlackWidow(link, password, username, domain, )