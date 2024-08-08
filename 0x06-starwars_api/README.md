# Star Wars Characters Project

This project involves interacting with an external API to fetch and display information about Star Wars characters based on the movie ID provided as an argument. To complete this project, you should understand several key concepts related to web programming, API interaction, and asynchronous programming in JavaScript.

## Key Concepts

### 1. HTTP Requests in JavaScript
- **Objective**: Learn how to make HTTP requests to external services.
- **Tools**: Use the `fetch` API (or alternatives like `axios`) in Node.js.
- **Resources**: 
  - [A Complete Guide to Making HTTP Requests in Node.js](https://nodejs.dev/learn/making-http-requests-with-nodejs)
  - `fetch` Example:
    ```javascript
    fetch('https://swapi.dev/api/people/1/')
      .then(response => response.json())
      .then(data => console.log(data))
      .catch(error => console.error('Error:', error));
    ```

### 2. Working with APIs
- **Objective**: Understand the basics of RESTful APIs and how to interact with them.
- **Key Points**:
  - Make GET requests to fetch data.
  - Parse JSON data returned by APIs.
- **Resources**:
  - [Working with APIs in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Introduction)
  - Example:
    ```javascript
    const url = 'https://swapi.dev/api/films/1/';
    fetch(url)
      .then(response => response.json())
      .then(data => console.log(data.characters))
      .catch(error => console.error('Error:', error));
    ```

### 3. Asynchronous Programming
- **Objective**: Manage asynchronous operations using callbacks, promises, and `async/await`.
- **Key Points**:
  - Handle API response data asynchronously.
  - Use `async/await` for cleaner, more readable code.
- **Resources**:
  - [Asynchronous Programming in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous)
  - Example:
    ```javascript
    async function fetchCharacters(movieId) {
      try {
        const response = await fetch(`https://swapi.dev/api/films/${movieId}/`);
        const movieData = await response.json();
        console.log(movieData.characters);
      } catch (error) {
        console.error('Error:', error);
      }
    }
    fetchCharacters(1);
    ```

### 4. Command Line Arguments in Node.js
- **Objective**: Access command-line arguments passed to a Node.js script using `process.argv`.
- **Resources**:
  - [How to Parse Command Line Arguments in Node.js](https://nodejs.dev/learn/nodejs-command-line-arguments)
  - Example:
    ```javascript
    const movieId = process.argv[2];
    console.log(`Fetching characters for movie ID: ${movieId}`);
    ```

### 5. Array Manipulation and Iteration
- **Objective**: Iterate over arrays and manipulate data to format and display character names.
- **Key Points**:
  - Use array methods like `forEach`, `map`, or `reduce` to handle data.
- **Resources**:
  - [JavaScript Array Methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
  - Example:
    ```javascript
    const characters = ['Luke Skywalker', 'Darth Vader', 'Leia Organa'];
    characters.forEach(character => console.log(character));
    ```

## Summary

