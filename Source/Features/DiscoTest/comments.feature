Feature: User Comments API calls
	The Users can
		Creates a new comment
		Get existing comment
		Update existing comment
		Delete existing comment

	Scenario: Get all comments
		Given I have the host=https://gorest.co.in/public-api/users
		When I do call for all comments
		Then I get all comments list

	Scenario: Get user comments
		When I have entered commentId=25
		Then I get that comment details

	Scenario: Create new comment
		When I have entered commentName=DiscoTestComment
		And commentDesciption=DiscoTestCommentDescription
		Then I am able to create appropriate new comment

	Scenario: Update comment
		When I have entered commentName=NewDiscoTestcomment
		And commentDesciption=NewDiscoTestcommentDescription
		Then I am able to update appropriate comment

	Scenario: Delete comment
		When I entered commentId=25
		Then I am ableto delete that comment
