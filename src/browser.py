from selenium import webdriver
import time
import Account as account

class Browser:

	followers = []
	follow = []

	def __init__(self,link):
		self.link = link
		self.browser = webdriver.Chrome()
		Browser.goInstagram(self)

	def goInstagram(self):
		self.browser.get(self.link)
		time.sleep(2)
		Browser.login(self)
		Browser.getFollowers(self)
		self.browser.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button").click()
		Browser.getFollow(self)
		self.browser.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button").click()
		Browser.getUnfollowing(self)

	def getUnfollowing(self):
		i = 1
		for item in self.follow:
			if item not in self.followers:
				print(str(i) + " => " +item)
				i+= 1

	def getFollowers(self):
		self.browser.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[2]/a").click()
		time.sleep(4)

		Browser.scrollDown(self)

		array = self.browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")
		for username in array:
			self.followers.append(str(username.text))

	def getFollow(self):
		self.browser.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[3]/a").click()
		time.sleep(4)

		Browser.scrollDown(self)

		array = self.browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")
		for username in array:
			self.follow.append(str(username.text))

	def scrollDown(self):
		jsCommand = """
		page = document.querySelector(".isgrP");
		page.scrollTo(0,page.scrollHeight);
		var pageEnd = page.scrollHeight;
		return pageEnd;
		"""
		pageEnd = self.browser.execute_script(jsCommand)
		while True:
			son = pageEnd
			time.sleep(1)
			pageEnd = self.browser.execute_script(jsCommand)
			if son == pageEnd:
				break


	def login(self):
		username = self.browser.find_element_by_name("username")
		password = self.browser.find_element_by_name("password")

		username.send_keys(account.username)
		password.send_keys(account.password)

		self.browser.find_element_by_css_selector("#loginForm > div > div:nth-child(3) > button").click()
		time.sleep(4)
		input("Press enter to continue")
		self.browser.get(self.link+"/"+account.username)
		time.sleep(3)
