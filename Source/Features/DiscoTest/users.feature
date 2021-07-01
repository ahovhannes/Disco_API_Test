Feature: Users API calls
	It is possible
		Creates a new User
		Get all existing Users
		Get existing User
		Update existing User
		Delete existing User

	Scenario: Get all users
		Given I have the host=https://gorest.co.in/public-api/users
		When I do call for all users
		Then I get all users list

	Scenario: Get user
		When I have entered userId=25
		Then I get that user details

	Scenario: Create user
		When I have entered userName=DiscoTestUser
		And userEmail=Disco.test@gmail.com
		And gender=Male and status=Active
		Then I am able to create appropriate new user

	Scenario: Update user
		When I have entered userName=NewDiscoTestUser
		And userEmail=NewDisco.test@gmail.com
		And gender=Male and status=Active
		Then I am able to update user info

	Scenario: Delete user
		When I have entered userId=25
		Then I am ableto delete that user

