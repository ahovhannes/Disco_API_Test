
## Installing dependencies

```sh
pip install requests
pip install behave
```

## Run place

- ``` cd Disco_API_Test/Source ```

## Run User Microservice features

- ``` behave Features/DiscoTest/users.feature --no-capture ```
- ``` behave Features/DiscoTest/todos.feature --no-capture ```
- ``` behave Features/DiscoTest/posts.feature --no-capture ```
- ``` behave Features/DiscoTest/comments.feature --no-capture ```
- or
- ``` behave Features/DiscoTest/users.feature ```
- ``` behave Features/DiscoTest/todos.feature ```
- ``` behave Features/DiscoTest/posts.feature ```
- ``` behave Features/DiscoTest/comments.feature ```

## Run Data processing features

- ``` behave Features/DiscoTest/data_processing.feature --no-capture ```
- or
- ``` behave Features/DiscoTest/data_processing.feature ```

## Run All features

- ``` behave Features/DiscoTest/ --no-capture ```
- or
- ``` behave Features/DiscoTest/ ```


