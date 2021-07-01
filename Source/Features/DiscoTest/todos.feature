Feature: User Todos API calls
	The Users can
		Creates a new todo
		Get existing todo
		Update existing todo
		Delete existing todo

	Scenario: Get all todos
		Given I have the host=https://gorest.co.in/public-api/users
		When I do call for all todos
		Then I get all todos list

	Scenario: Get user todos
		When I have entered todoId=25
		Then I get that todo details

	Scenario: Create new todo
		When I have entered todoName=DiscoTestTodo
		And todoDesciption=DiscoTestTodoDescription
		Then I am able to create appropriate new todo

	Scenario: Update todo
		When I have entered todoName=NewDiscoTesttodo
		And todoDesciption=NewDiscoTesttodoDescription
		Then I am able to update appropriate todo

	Scenario: Delete todo
		When I entered todoId=25
		Then I am ableto delete that todo
