from splinter import Browser
import pdfkit
browser = Browser()
browser.visit('https://confluence.gelbergroup.com')
browser.find_by_id('login-link').click()
browser.fill('os_username', 'craab')
browser.fill('os_password', 'cha9.coa5')
browser.find_by_name('login').click()
options = {
	"cookie": browser.cookies.all().items(),
	"page-height": '1000px',
	"page-width": '1000px'
	}
pdfkit.from_url("https://confluence.gelbergroup.com/display/public/Seating+Chart", "c:/out.pdf", options=options)

