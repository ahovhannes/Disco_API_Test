#
# DiscoTest step functions
#

import os
import sys
import json
from enum import Enum
from behave import given, when, then
from TestFunctions.FunctionApi.Function_Api import bddApi
from TestFunctions.FunctionUrl.Function_Url import bddUrl
from TestFunctions.FunctionRandom.Function_Random import bddRandom
from TestFunctions.FunctionStrings.Function_Generate_Strings import generatedStrings

errorFromNewLine = "\n"
generatedStrings = generatedStrings()
space8 = generatedStrings.generateNsymbols(" ", 8)

class ParameterValues(Enum):
    novalue = "novalue"
    allvalues = "allvalues"



# ----------------- users.feature -----------------

@given(u'I have the host={host}')
def users_given(context, host):
    context.host = host
    print(space8+"host="+str(host))

@when(u'I do call for all users')
def users_when_all_users(context):
    #
    #Creating Api objects
    context.bddApi = bddApi()
    #
    #Doing api call
    host    = context.host
    headers = {'Content-Type': 'application/json'}
    context.result = context.bddApi.do_api_call('get', host, headers)
    
@then(u'I get all users list')
def users_then_all_users(context):
    print(space8+"api_call_result="+str(context.result))


@when(u'I have entered userId={userId}')
def users_when_userId(context, userId):
    context.userId = userId

@then(u'I get that user details')
def users_then_user_details(context):
    print(space8+'... Geting details for the user with userId=' +str(context.userId) )


@when(u'I have entered userName={userName}')
def users_when_name(context, userName):
    context.userName = userName

@when(u'userEmail={userEmail}')
def users_when_email(context, userEmail):
    context.userEmail = userEmail

@when(u'gender={gender} and status={status}')
def users_when_gender_status(context, gender, status):
    context.gender = gender
    context.status = status

@then(u'I am able to create appropriate new user')
def users_then_new_user(context):
    print(space8+'... Cheching new created user existence in DB')


@then(u'I am able to update user info')
def users_then_update_user(context):
    print(space8+'... Checking if user info were updated')


@then(u'I am ableto delete that user')
def users_then_delete_user(context):
    print(space8+'... Checking if user were deleted from DB')
    print('... Checking if user were deleted from DB')



# ----------------- posts.feature -----------------

@when(u'I do call for all posts')
def step_impl(context):
    pass

@then(u'I get all posts list')
def step_impl(context):
    pass

@when(u'I have entered postId=25')
def step_impl(context):
    pass

@then(u'I get that posts details')
def step_impl(context):
    pass

@when(u'I have entered postName=DiscoTestPost')
def step_impl(context):
    pass

@when(u'postDesciption=DiscoTestPostDescription')
def step_impl(context):
    pass

@then(u'I am able to create appropriate new post')
def step_impl(context):
    pass

@when(u'I have entered postName=NewDiscoTestPost')
def step_impl(context):
    pass

@when(u'postDesciption=NewDiscoTestPostDescription')
def step_impl(context):
    pass

@then(u'I am able to update appropriate post')
def step_impl(context):
    pass

@when(u'I entered postId=25')
def step_impl(context):
    pass

@then(u'I am ableto delete that post')
def step_impl(context):
    pass



# ----------------- comments.feature -----------------

@when(u'I do call for all comments')
def step_impl(context):
    pass

@then(u'I get all comments list')
def step_impl(context):
    pass

@when(u'I have entered commentId=25')
def step_impl(context):
    pass

@then(u'I get that comment details')
def step_impl(context):
    pass

@when(u'I have entered commentName=DiscoTestComment')
def step_impl(context):
   pass

@when(u'commentDesciption=DiscoTestCommentDescription')
def step_impl(context):
    pass

@then(u'I am able to create appropriate new comment')
def step_impl(context):
    pass

@when(u'I have entered commentName=NewDiscoTestcomment')
def step_impl(context):
    pass

@when(u'commentDesciption=NewDiscoTestcommentDescription')
def step_impl(context):
    pass

@then(u'I am able to update appropriate comment')
def step_impl(context):
    pass

@when(u'I entered commentId=25')
def step_impl(context):
    pass

@then(u'I am ableto delete that comment')
def step_impl(context):
    pass



# ----------------- todos.feature -----------------

@when(u'I do call for all todos')
def step_impl(context):
    pass

@then(u'I get all todos list')
def step_impl(context):
    pass

@when(u'I have entered todoId=25')
def step_impl(context):
    pass

@then(u'I get that todo details')
def step_impl(context):
    pass

@when(u'I have entered todoName=DiscoTestTodo')
def step_impl(context):
    pass

@when(u'todoDesciption=DiscoTestTodoDescription')
def step_impl(context):
    pass

@then(u'I am able to create appropriate new todo')
def step_impl(context):
    pass

@when(u'I have entered todoName=NewDiscoTesttodo')
def step_impl(context):
    pass

@when(u'todoDesciption=NewDiscoTesttodoDescription')
def step_impl(context):
    pass

@then(u'I am able to update appropriate todo')
def step_impl(context):
    pass

@when(u'I entered todoId=25')
def step_impl(context):
    pass

@then(u'I am ableto delete that todo')
def step_impl(context):
    pass



# ----------------- data_processing.feature -----------------

@when(u'I input dataIn={dataIn}')
def step_impl(context, dataIn):
    context.dataIn = dataIn

@when(u'do action={action}')
def step_impl(context, action):
    context.action = action

@then(u'we will have succeeded dataOut={dataOut}')
def step_impl(context, dataOut):
    context.dataOut = dataOut
    print('... Doing ' +str(context.action)+ ' on ' +str(context.dataIn))
    print('... Checking, if the result is '  +str(dataOut))

