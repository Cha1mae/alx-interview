#!/usr/bin/node
const request = require('request');

function getCharacterName(url) {
  request(url, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      console.log(JSON.parse(body).name);
    }
  });
}

function getCharactersOfMovie(movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;
  request(url, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const characters = JSON.parse(body).characters;
      characters.forEach((characterUrl) => {
        getCharacterName(characterUrl);
      });
    }
  });
}

const movieId = process.argv[2];
getCharactersOfMovie(movieId);
