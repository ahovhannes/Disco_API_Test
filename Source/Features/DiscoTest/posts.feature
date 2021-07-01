Feature: User Posts API calls
	The Users can
		Creates a new post
		Get existing post
		Update existing post
		Delete existing post

	Scenario: Get all posts
		Given I have the host=https://gorest.co.in/public-api/users
		When I do call for all posts
		Then I get all posts list

	Scenario: Get user posts
		When I have entered postId=25
		Then I get that posts details

	Scenario: Create new post
		When I have entered postName=DiscoTestPost
		And postDesciption=DiscoTestPostDescription
		Then I am able to create appropriate new post

	Scenario: Update post
		When I have entered postName=NewDiscoTestPost
		And postDesciption=NewDiscoTestPostDescription
		Then I am able to update appropriate post

	Scenario: Delete post
		When I entered postId=25
		Then I am ableto delete that post
