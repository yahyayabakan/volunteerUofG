from django.test import TestCase
from volunteerUofG.models import User, Volunteer, Charity, Opportunity
# Create your tests here.

class VolunteerModelTest(TestCase):
   
    def test_first_name(self):
        user = User(first_name = 'James', last_name = 'Bond', email = "jamesbond@gmail.com")
        user.save()
        first_name = user.first_name
        self.assertEqual(first_name, 'James')
    
    def test_last_name(self):
        user = User(first_name = 'James', last_name = 'Bond', email = "jamesbond@gmail.com")
        user.save()
        last_name = user.last_name
        self.assertEqual(last_name, 'Bond')

    def test_email(self):
        user = User(first_name = 'James', last_name = 'Bond', email = "jamesbond@gmail.com")
        user.save()
        email = user.email
        self.assertEqual(email, 'jamesbond@gmail.com')

    def test_volunteer_interested_id(self):
        user_test = User(first_name = 'James', last_name = 'Bond', email = "jamesbond@gmail.com")
        user_test.save()
        volunteer = Volunteer(user = user_test, interested_in = 'Sports', availability = 'Weekends', introduce_yourself = 'I am an engineering student')
        interested_in = volunteer.interested_in
        self.assertEqual(interested_in, 'Sports')

    def test_volunteer_availability(self):
        user_test = User(first_name = 'James', last_name = 'Bond', email = "jamesbond@gmail.com")
        user_test.save()
        volunteer = Volunteer(user = user_test, interested_in = 'Sports', availability = 'Weekends', introduce_yourself = 'I am an engineering student')
        availability = volunteer.availability
        self.assertEqual(availability, 'Weekends')

    def test_volunteer_introduce_yourself(self):
        user_test = User(first_name = 'James', last_name = 'Bond', email = "jamesbond@gmail.com")
        user_test.save()
        volunteer = Volunteer(user = user_test, interested_in = 'Sports', availability = 'Weekends', introduce_yourself = 'I am an engineering student')
        introduce_yourself = volunteer.introduce_yourself
        self.assertEqual(introduce_yourself, 'I am an engineering student')

    def test_charity_address(self):
        user_test = User(first_name = 'James', last_name = 'Bond', email = "jamesbond@gmail.com")
        user_test.save()
        charity = Charity(user = user_test, address = 'Glasgow', phone = '7590910759', website = 'http://actionfoundation.com', description = 'As a charity, we help refugees')
        address = charity.address
        self.assertEqual(address, 'Glasgow')

    def test_charity_phone(self):
        user_test = User(first_name = 'James', last_name = 'Bond', email = "jamesbond@gmail.com")
        user_test.save()
        charity = Charity(user = user_test, address = 'Glasgow', phone = '7590910759', website = 'http://actionfoundation.com', description = 'As a charity, we help refugees')
        phone = charity.phone
        self.assertEqual(phone, '7590910759')

    def test_charity_website(self):
        user_test = User(first_name = 'James', last_name = 'Bond', email = "jamesbond@gmail.com")
        user_test.save()
        charity = Charity(user = user_test, address = 'Glasgow', phone = '7590910759', website = 'http://actionfoundation.com', description = 'As a charity, we help refugees')
        website = charity.website
        self.assertEqual(website, 'http://actionfoundation.com')

    def test_charity_description(self):
        user_test = User(first_name = 'James', last_name = 'Bond', email = "jamesbond@gmail.com")
        user_test.save()
        charity = Charity(user = user_test, address = 'Glasgow', phone = '7590910759', website = 'http://actionfoundation.com', description = 'As a charity, we help refugees')
        description = charity.description
        self.assertEqual(description, 'As a charity, we help refugees')

    def test_opportunity_title(self):
        user_test = User(first_name = 'James', last_name = 'Bond', email = "jamesbond@gmail.com")
        user_test.save()
        charity = Charity(user = user_test, address = 'Glasgow', phone = '7590910759', website = 'http://actionfoundation.com', description = 'As a charity, we help refugees')
        opportunity = Opportunity(title = 'Food Bank', creator = charity, url = 'https://wwww.foodbank.com', description = 'We provide free food for homeless', skills = 'Delivery service', location='Glasgow', time='Everyday')
        title = opportunity.title
        self.assertEqual(title, 'Food Bank')

    def test_opportunity_url(self):
        user_test = User(first_name = 'James', last_name = 'Bond', email = "jamesbond@gmail.com")
        user_test.save()
        charity = Charity(user = user_test, address = 'Glasgow', phone = '7590910759', website = 'http://actionfoundation.com', description = 'As a charity, we help refugees')
        opportunity = Opportunity(title = 'Food Bank', creator = charity, url = 'https://wwww.foodbank.com', description = 'We provide free food for homeless', skills = 'Delivery service', location='Glasgow', time='Everyday')
        url = opportunity.url
        self.assertEqual(url, 'https://wwww.foodbank.com')

    def test_opportunity_description(self):
        user_test = User(first_name = 'James', last_name = 'Bond', email = "jamesbond@gmail.com")
        user_test.save()
        charity = Charity(user = user_test, address = 'Glasgow', phone = '7590910759', website = 'http://actionfoundation.com', description = 'As a charity, we help refugees')
        opportunity = Opportunity(title = 'Food Bank', creator = charity, url = 'https://wwww.foodbank.com', description = 'We provide free food for homeless', skills = 'Delivery service', location='Glasgow', time='Everyday')
        description = opportunity.description
        self.assertEqual(description, 'We provide free food for homeless')

    def test_opportunity_skills(self):
        user_test = User(first_name = 'James', last_name = 'Bond', email = "jamesbond@gmail.com")
        user_test.save()
        charity = Charity(user = user_test, address = 'Glasgow', phone = '7590910759', website = 'http://actionfoundation.com', description = 'As a charity, we help refugees')
        opportunity = Opportunity(title = 'Food Bank', creator = charity, url = 'https://wwww.foodbank.com', description = 'We provide free food for homeless', skills = 'Delivery service', location='Glasgow', time='Everyday')
        skills = opportunity.skills
        self.assertEqual(skills, 'Delivery service')

    def test_opportunity_location(self):
        user_test = User(first_name = 'James', last_name = 'Bond', email = "jamesbond@gmail.com")
        user_test.save()
        charity = Charity(user = user_test, address = 'Glasgow', phone = '7590910759', website = 'http://actionfoundation.com', description = 'As a charity, we help refugees')
        opportunity = Opportunity(title = 'Food Bank', creator = charity, url = 'https://wwww.foodbank.com', description = 'We provide free food for homeless', skills = 'Delivery service', location='Glasgow', time='Everyday')
        location = opportunity.location
        self.assertEqual(location, 'Glasgow')   

    def test_opportunity_location(self):
        user_test = User(first_name = 'James', last_name = 'Bond', email = "jamesbond@gmail.com")
        user_test.save()
        charity = Charity(user = user_test, address = 'Glasgow', phone = '7590910759', website = 'http://actionfoundation.com', description = 'As a charity, we help refugees')
        opportunity = Opportunity(title = 'Food Bank', creator = charity, url = 'https://wwww.foodbank.com', description = 'We provide free food for homeless', skills = 'Delivery service', location='Glasgow', time='Everyday')
        time = opportunity.time
        self.assertEqual(time, 'Everyday')