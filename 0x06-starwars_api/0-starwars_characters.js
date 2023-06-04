#!/usr/bin/node
const request = require('request');

function getCharacters(movieId) {
  const filmUrl = `https://swapi.dev/api/films/${movieId}/`;
  return new Promise((resolve, reject) => {
    request(filmUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const filmData = JSON.parse(body);
        const characterUrls = filmData.characters;
        const characterNames = [];

        function fetchCharacter(url) {
          return new Promise((resolve, reject) => {
            request(url, (error, response, body) => {
              if (error) {
                reject(error);
              } else {
                const characterData = JSON.parse(body);
                resolve(characterData.name);
              }
            });
          });
        }

        const characterPromises = characterUrls.map(fetchCharacter);
        Promise.all(characterPromises)
          .then((characters) => {
            resolve(characters);
          })
          .catch((error) => {
            reject(error);
          });
      }
    });
  });
}

function printCharacters(movieId) {
  const movieTitleUrl = `https://swapi.dev/api/films/${movieId}/`;
  request(movieTitleUrl, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const movieData = JSON.parse(body);
      const movieTitle = movieData.title;

      console.log(`Characters from ${movieTitle}:`);

      getCharacters(movieId)
        .then((characters) => {
          characters.forEach((character) => {
            console.log(character);
          });
        })
        .catch((error) => {
          console.error(error);
        });
    }
  });
}

// Example usage
const movieId = 3; // Return of the Jedi
printCharacters(movieId);

